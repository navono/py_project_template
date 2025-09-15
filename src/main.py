import click
from .app import start
from .utils import Config, CustomizeLogger

@click.group()
def cli():
    """Py Project Temp CLI"""
    pass

@cli.command()
def run():
    """Run the application"""
    import asyncio
    
    # Initialize logging
    gen_config = Config().get_config()
    logger = CustomizeLogger.make_logger(gen_config["log"])
    
    click.echo("Starting application...")
    asyncio.run(start())

@cli.command()
@click.option('--level', default='info', help='Log level (debug, info, warning, error, critical)')
@click.option('--path', default='./logs', help='Log directory path')
def logs(level, path):
    """Configure logging settings"""
    click.echo(f"Setting log level to: {level}")
    click.echo(f"Log directory: {path}")
    # Here you could implement actual log configuration

@cli.command()
def config():
    """Show current configuration"""
    config = Config().get_config()
    click.echo("Current configuration:")
    for section, settings in config.items():
        click.echo(f"\n[{section}]")
        if isinstance(settings, dict):
            for key, value in settings.items():
                click.echo(f"  {key}: {value}")
        else:
            click.echo(f"  {settings}")

@cli.command()
@click.argument('message')
def echo(message):
    """Echo a message with logging"""
    gen_config = Config().get_config()
    logger = CustomizeLogger.make_logger(gen_config["log"])
    logger.info(f"Echo: {message}")
    click.echo(f"Message: {message}")

@cli.command()
def help():
    """Show available commands"""
    click.echo("Available commands:")
    click.echo("  run     - Start the application")
    click.echo("  logs    - Configure logging settings")
    click.echo("  config  - Show current configuration")
    click.echo("  echo    - Echo a message with logging")
    click.echo("  help    - Show this help message")

if __name__ == "__main__":
    cli()