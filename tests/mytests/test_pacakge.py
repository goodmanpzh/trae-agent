# import os

# api_key = os.environ.get("OPENAI_API_KEY")
# print(api_key)  # 输出: your-openai-api-key


from rich.console import Console

console = Console()

console.print("Hello, [bold red]World[/bold red]!")
console.print(f"[blue]Changed working directory to: /nana[/blue]")