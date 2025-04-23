import calendar
from rich.console import Console
from rich.table import Table

def colorful_calender(year):
    console = Console()
    months = [calendar.monthcalendar(year, m) for m in range(1, 13)]

    for month in range(12):
        month_name = calendar.month_name[month + 1]

        table = Table(title=f"[bold magenta]{month_name} \
                      {year}[/bold magenta]", show_lines=True)
        table.add_column("Mon", justify="center", style="yellow")
        table.add_column("Tue", justify="center", style="yellow")
        table.add_column("Wed", justify="center", style="yellow")
        table.add_column("Thu", justify="center", style="yellow")
        table.add_column("Fri", justify="center", style="yellow")
        table.add_column("Sat", justify="center", style="red")
        table.add_column("Sun", justify="center", style="red")

        for week in months[month]:
            table.add_row(*[str(day) if day != 0 else "" for day in week])

        console.print(table)
        console.print("\n") 

colorful_calender(2025)