#!/usr/bin/env python3
"""Countdown Timer Script"""

# Import necessary modules
import os
import time

import click
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install


class CountDown:
    """CountDown class for a simple countdown timer."""

    def __init__(self) -> None:
        """Initialize the CountDown instance."""
        self.console = Console()
        self.fit = Panel.fit

    @staticmethod
    def checker(method):
        """Decorator to check and validate time values."""

        def wrapper(*args, **kwargs):
            """Wrapper function for time validation."""
            (self,) = args
            sec: int = kwargs.setdefault("sec", 0)
            _min: int = kwargs.setdefault("min", 0)
            hours: int = kwargs.setdefault("hours", 0)

            if not 0 <= sec < 60:
                raise ValueError("Seconds should be in the range [0, 59].")

            if not 0 <= _min < 60:
                raise ValueError("Minutes should be in the range [0, 59].")

            if not hours >= 0:
                raise ValueError("Hours should be a non-negative integer.")

            return method(self, sec=sec, _min=_min, hours=hours)

        return wrapper

    @checker
    def start(self, *, sec: int, _min: int, hours: int):
        """Start the countdown timer."""
        second: int = sec + _min * 60 + hours * 60 * 60

        while second > 0:
            sec, _min, hours = self.converter(second)
            if hours:
                clr = "green"
            elif _min:
                clr = "yellow"
            else:
                clr = "red"

            columns, rows = os.get_terminal_size()

            for _ in range(rows // 2):
                print()

            self.console.print(
                f"[bold blink]{sec:02}:{_min:02}:{hours:02}[/]",
                style=f"{clr} bold",
                justify="center",
                width=columns,
                end="\n",
            )
            second -= 1
            time.sleep(1)

            # Clear the console screen based on the operating system
            if os.name == "posix":
                os.system("clear")

            if not second:
                pass

    def converter(self, sec) -> tuple:
        """Convert total seconds into hours, minutes, and seconds."""
        # Convert to seconds
        seconds = sec % 60

        # Convert to minutes
        minutes = (sec // 60) % 60

        # Convert to hours
        hours = sec // 3600

        return seconds, minutes, hours


@click.command()
@click.option(
    "--seconds", default=30, help="Set the initial seconds for the countdown."
)
@click.option("--minutes", default=0, help="Set the initial minutes for the countdown.")
@click.option("--hours", default=0, help="Set the initial hours for the countdown.")
def main(seconds: int = 30, minutes: int = 0, hours: int = 0):
    """Main function to start the countdown timer."""
    # Install traceback for better error messages
    install()

    # Create an instance of the CountDown class
    count_down = CountDown()

    # Start the countdown timer with user-provided values
    count_down.start(sec=int(seconds), _min=int(minutes), hours=int(hours))


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
