"""CLI entry point for Horizon."""

import argparse
import asyncio
import smtplib
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .storage.manager import ConfigError, StorageManager
from .orchestrator import HorizonOrchestrator


console = Console()


def print_banner():
    """Print the application banner."""
    banner = r"""
[bold blue]
  _    _            _
 | |  | |          (_)
 | |__| | ___  _ __ _ ___  ___  _ __
 |  __  |/ _ \| '__| |_  / / _ \| '_ \
 | |  | | (_) | |  | |/ / | (_) | | | |
 |_|  |_|\___/|_|  |_/___| \___/|_| |_|
[/bold blue]
[cyan]  AI-Driven Information Aggregation System[/cyan]
    """
    console.print(banner)


def main():
    """Main CLI entry point."""
    print_banner()

    parser = argparse.ArgumentParser(description="Horizon - AI-Driven Information Aggregation System")
    parser.add_argument("--hours", type=int, help="Force fetch from last N hours")
    parser.add_argument("--email-test", action="store_true", help="运行邮箱诊断测试（仅测试 SMTP 连接，不发送正式摘要）")
    parser.add_argument("--to", type=str, help="与 --email-test 配合，指定测试邮件的收件地址")
    args = parser.parse_args()

    try:
        # Load environment variables from .env file
        load_dotenv()

        # Ensure we're in the project directory or use data/ in current dir
        data_dir = Path("data")

        # Initialize storage manager
        storage = StorageManager(data_dir=str(data_dir))

        # Load configuration
        try:
            config = storage.load_config()
        except FileNotFoundError:
            console.print("[bold red]❌ Configuration file not found![/bold red]\n")
            data_dir_path = data_dir if isinstance(data_dir, Path) else Path(data_dir)
            example_path = data_dir_path / "config.example.json"
            if example_path.exists():
                console.print(
                    f"Copy the example config and edit it:\n"
                    f"  [cyan]cp {example_path} {data_dir_path / 'config.json'}[/cyan]\n"
                )
            console.print(
                "Or run [bold cyan]uv run horizon-wizard[/bold cyan] to launch the interactive setup wizard.\n"
            )
            sys.exit(1)
        except ConfigError as e:
            console.print(f"[bold red]❌ Error loading configuration: {e}[/bold red]")
            sys.exit(1)
        except Exception as e:
            console.print(f"[bold red]❌ Error loading configuration: {e}[/bold red]")
            sys.exit(1)

        # 邮箱诊断模式
        if args.email_test:
            from .services.email import EmailManager
            if not config.email:
                console.print("[bold red]❌ 配置中未找到 email 配置项[/bold red]")
                sys.exit(1)
            manager = EmailManager(config.email, console=console)
            subscribers = storage.load_subscribers()
            # --to 参数优先级高于 subscribers.json
            test_recipients = []
            if args.to:
                test_recipients = [args.to]
            elif subscribers:
                test_recipients = [subscribers[0]]
            console.print(f"[cyan]📧 邮箱诊断模式[/cyan]")
            console.print(f"  email.enabled:       {config.email.enabled}")
            console.print(f"  smtp_server:         {config.email.smtp_server}:{config.email.smtp_port}")
            console.print(f"  email_address:       {config.email.email_address}")
            console.print(f"  sender_name:         {config.email.sender_name}")
            console.print(f"  smtp_username:       {config.email.smtp_username}")
            console.print(f"  password_env:        {config.email.password_env}")
            console.print(f"  password set:        {bool(manager.pwd)}")
            console.print(f"  imap_enabled:        {config.email.imap_enabled}")
            console.print(f"  imap_server:         {config.email.imap_server}:{config.email.imap_port}")
            console.print(f"  subscribers ({len(subscribers)}): {subscribers}")
            console.print(f"  test recipient:      {test_recipients[0] if test_recipients else '(无)'}")
            console.print("")
            # 测试 SMTP 连接
            console.print("[cyan]--- 测试 SMTP 连接 ---[/cyan]")
            try:
                with manager._create_smtp_connection() as server:
                    console.print("[green]  ✅ SMTP 连接成功！[/green]")
                    # 尝试发送一封测试邮件
                    if test_recipients:
                        test_addr = test_recipients[0]
                        console.print(f"[cyan]--- 发送测试邮件到 {test_addr} ---[/cyan]")
                        try:
                            from email.mime.text import MIMEText
                            test_msg = MIMEText("这是一封来自 Horizon 的测试邮件。如果你收到这封邮件，说明 SMTP 配置正确。")
                            test_msg["Subject"] = "[Horizon] 邮箱诊断测试"
                            test_msg["From"] = f"{config.email.sender_name} <{config.email.email_address}>"
                            test_msg["To"] = test_addr
                            server.send_message(test_msg)
                            console.print(f"[green]  ✅ 测试邮件已发送到 {test_addr}，请检查收件箱（含垃圾邮件）[/green]")
                        except Exception as e:
                            console.print(f"[red]  ❌ 发送测试邮件失败: {e}[/red]")
                    else:
                        console.print("[yellow]  ⏭ 无订阅者且未指定 --to，跳过发送测试邮件[/yellow]")
                        console.print("[yellow]  用法示例: uv run horizon --email-test --to someone@example.com[/yellow]")
            except smtplib.SMTPAuthenticationError:
                console.print("[red]  ❌ SMTP 认证失败 — 请检查 EMAIL_PASSWORD 环境变量（163 授权码，非登录密码）[/red]")
            except smtplib.SMTPServerDisconnected:
                console.print("[red]  ❌ SMTP 服务器断开连接 — 可能是 163 拦截，尝试更换 IP 或降低频率[/red]")
            except smtplib.SMTPException as e:
                console.print(f"[red]  ❌ SMTP 异常: {e}[/red]")
            except Exception as e:
                console.print(f"[red]  ❌ 连接失败: {e}[/red]")
            sys.exit(0)

        # Create and run orchestrator
        orchestrator = HorizonOrchestrator(config, storage)
        asyncio.run(orchestrator.run(force_hours=args.hours))

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]❌ Fatal error: {e}[/bold red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def print_config_template():
    """Print configuration template."""
    template = """
{
  "version": "1.0",
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY",
    "temperature": 0.3,
    "max_tokens": 4096
  },
  "sources": {
    "github": [
      {
        "type": "user_events",
        "username": "torvalds",
        "enabled": true
      }
    ],
    "hackernews": {
      "enabled": true,
      "fetch_top_stories": 30,
      "min_score": 100
    },
    "rss": [
      {
        "name": "Example Blog",
        "url": "https://example.com/feed.xml",
        "enabled": true,
        "category": "software-engineering"
      }
    ]
  },
  "filtering": {
    "ai_score_threshold": 7.0,
    "time_window_hours": 24,
    "max_items": null,
    "category_groups": {},
    "default_group": "other",
    "default_group_limit": null
  }
}

Also create a .env file with:
ANTHROPIC_API_KEY=your_api_key_here
GITHUB_TOKEN=your_github_token_here (optional but recommended)
"""
    console.print(template)


if __name__ == "__main__":
    main()
