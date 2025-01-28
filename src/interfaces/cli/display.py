"""CLI display components and utilities."""

import os
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

from ...config.settings import settings
from ...i18n.manager import i18n

console = Console()

class DisplayManager:
    """Manage CLI display components."""

    def __init__(self):
        """Initialize display manager."""
        self.console = Console()

    def clear_screen(self) -> None:
        """Clear the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def show_banner(self) -> None:
        """Display application banner."""
        self.clear_screen()
        self.console.print(
            Panel(
                r"""[bold red]●[bold yellow] ●[bold green] ●
[bold blue]                   _    _ _   _           
[bold blue]                  | |  | | | | |          
[bold blue]                  | |__|_  _|| |__        
[bold blue]                  |____| |_| |____|       
[bold purple]               ___        _  _        
[bold purple]              / __| _  _ (_)| |_  ___ 
[bold purple]              \__ \| || || ||  _|/ -_)
[bold purple]              |___/ \_,_||_| \__|\___|
                               

                     [bold white on blue]Coded by LavX""",
                width=55,
                style="bold bright_white",
            )
        )
    def show_status(self,
        credits: str,
        name: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> None:
        """Display status panel.
        
        Args:
            credits: Current credit balance
            name: Optional user name
            user_id: Optional user ID
        """
        if name and user_id:
            self.console.print(
                Panel(
                    f"""[bold white]{i18n.get_text('status.name')} :[bold green] {name}
[bold white]{i18n.get_text('status.link')} :[bold red] https://web.facebook.com/{user_id}""",
                    width=55,
                    style="bold bright_white",
                    title=f"[bold bright_white]>> [{i18n.get_text('status.facebook_connected')}] <<"
                )
            )
        
        self.console.print(
            Panel(
                f"[bold white]{i18n.get_text('status.coins')} :[bold red] {credits}",
                width=55,
                style="bold bright_white",
                title=f"[bold bright_white]>> [{i18n.get_text('status.status')}] <<"
            )
        )

    def show_menu(self) -> None:
        """Display main menu."""
        self.console.print(
            Panel(
                f"""[bold green]01[bold white]. {i18n.get_text('menu.exchange_profile')}
[bold green]02[bold white]. {i18n.get_text('menu.follow_mission')}
[bold green]03[bold white]. {i18n.get_text('menu.delete_links')}
[bold green]04[bold white]. {i18n.get_text('menu.exchange_page')}
[bold green]05[bold white]. {i18n.get_text('menu.twitter_likes')}
[bold green]06[bold white]. {i18n.get_text('menu.exit')}
[bold green]07[bold white]. {i18n.get_text('menu.switch_language')}""",
                width=55,
                style="bold bright_white",
                subtitle="╭─────",
                subtitle_align="left",
                title="[bold bright_white]>> [Menu] <<"
            )
        )

    def show_language_menu(self) -> None:
        """Display language selection menu."""
        self.console.print(
            Panel(
                f"""[bold white]1. {i18n.get_text('menu.language.english')}
2. {i18n.get_text('menu.language.indonesian')}""",
                width=55,
                style="bold bright_white",
                title=f"[bold bright_white]>> [{i18n.get_text('menu.language.select')}] <<",
                subtitle="╭─────",
                subtitle_align="left"
            )
        )

    def show_success(self, message: str, width: int = 55) -> None:
        """Display success message.
        
        Args:
            message: Success message
            width: Panel width
        """
        self.console.print(
            Panel(
                f"[bold green]{message}",
                width=width,
                style="bold bright_white",
                title=f"[bold bright_white]>> [{i18n.get_text('status.success')}] <<"
            )
        )

    def show_error(self, message: str, width: int = 55) -> None:
        """Display error message.
        
        Args:
            message: Error message
            width: Panel width
        """
        self.console.print(
            Panel(
                f"[bold red]{message}",
                width=width,
                style="bold bright_white",
                title=f"[bold bright_white]>> [{i18n.get_text('status.error')}] <<"
            )
        )

    def show_notice(self, message: str, width: int = 55) -> None:
        """Display notice message.
        
        Args:
            message: Notice message
            width: Panel width
        """
        self.console.print(
            Panel(
                f"[bold white]{message}",
                width=width,
                style="bold bright_white",
                title=f"[bold bright_white]>> [{i18n.get_text('status.wait')}] <<"
            )
        )

    def show_progress(self,
        message: str,
        success_count: int = 0,
        fail_count: int = 0
    ) -> None:
        """Display progress message.
        
        Args:
            message: Progress message
            success_count: Number of successful operations
            fail_count: Number of failed operations
        """
        self.console.print(
            f"[bold white]   ──>[bold white] {i18n.get_text('status.mission_progress')} [{i18n.get_text('status.success_count')}:-[bold green]{success_count}[bold white] {i18n.get_text('status.failed_count')}:-[bold red]{fail_count}[bold white]]     ",
            end="\r"
        )

    def prompt(self, message: str) -> str:
        """Show input prompt.
        
        Args:
            message: Prompt message
            
        Returns:
            str: User input
        """
        return self.console.input(f"[bold bright_white]   ╰─> {message}")

    def show_task_result(self,
        task_type: str,
        target_url: str,
        old_credits: str,
        new_credits: str
    ) -> None:
        """Display task result panel.
        
        Args:
            task_type: Type of task completed
            target_url: Target URL
            old_credits: Previous credit balance
            new_credits: New credit balance
        """
        self.console.print(
            Panel(
                f"""[bold white]{i18n.get_text('status.status')} :[bold green] {i18n.get_text('status.success')}...
[bold white]{task_type} :[bold red] {target_url}
[bold white]{i18n.get_text('status.coins')} :[bold green] {old_credits}[bold white] >[bold green] {new_credits}""",
                width=55,
                style="bold bright_white",
                title=f"[bold bright_white]>> [{i18n.get_text('status.success')}] <<"
            )
        )