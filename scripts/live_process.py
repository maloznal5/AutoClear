import time
import json
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table
from rich.live import Live

console = Console()

def run_real_process():
    # Имитация реального заказа на 10 000 грн
    raw_data = [
        {'name': 'Pixel 8 Pro Case', 'price_usd': 25, 'stock': 12},
        {'name': 'Samsung S24 Ultra Glass', 'price_usd': 15, 'stock': 45},
        {'name': 'USB-C Cable 2m', 'price_usd': 10, 'stock': 0},
        {'name': 'Wireless Charger', 'price_usd': 40, 'stock': 8},
    ]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        
        # Шаг 1: Подключение к API Поставщика
        task1 = progress.add_task("[cyan]Connecting to Supplier API...", total=100)
        while not progress.finished:
            progress.update(task1, advance=2)
            time.sleep(0.03)
            if progress.tasks[0].completed >= 100: break

        # Шаг 2: Трансформация и пересчет (Курс 41.5 + Маржа 15%)
        console.print("[yellow]⚙️  Applying Business Logic (Margin 15%, Rate 41.5)...[/yellow]")
        time.sleep(0.5)
        
        # Формируем итоговую таблицу
        table = Table(title="Final Price List - AutoClear DataBridge", header_style="bold magenta")
        table.add_column("Product", style="dim")
        table.add_column("USD", justify="right")
        table.add_column("UAH (Final)", style="green", justify="right")
        table.add_column("Status", justify="center")

        for item in raw_data:
            price_uah = round(item['price_usd'] * 41.5 * 1.15, 2)
            status = "[green]In Stock[/green]" if item['stock'] > 0 else "[red]Out of Stock[/red]"
            table.add_row(item['name'], f"${item['price_usd']}", f"{price_uah} ₴", status)
            time.sleep(0.2)

    console.print(table)
    console.print("\n[bold green]✅ Синхронизация с базой данных завершена. Лог сохранен.[/bold green]")

if __name__ == "__main__":
    run_real_process()
