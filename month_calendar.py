import calendar
from rich.console import Console
from rich.table import Table
from datetime import date

now = date.today()
month = now.month
year = now.year

if month<10:
    monthf = f"{month:02}"

def color_calendar(y,m):
    
    console = Console()
    months = calendar.monthcalendar(y, m)
    month_nam = calendar.month_name[m]
    
    table = Table(title=f"[bold cyan]{month_nam}  [bold cyan]{y}", show_lines=True)
    
    table.add_column("Mon", justify="center", style="green")
    table.add_column("Tue", justify="center", style="green")
    table.add_column("Wed", justify="center", style="green")
    table.add_column("Thu", justify="center", style="green")
    table.add_column("Fri", justify="center", style="red")
    table.add_column("Sat", justify="center", style="yellow")
    table.add_column("Sun", justify="center", style="green")
    
    for week in months:
        table.add_row(*[str(day) if day != 0 else "" for day in week])

    console.print(table)
    console.print("\n")
    console.print(f"{now.day}-{monthf}-{year}", justify="center")

color_calendar(year, month)


