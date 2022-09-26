from logging import basicConfig, ERROR, INFO

from utils import cli
basicConfig(level=INFO)
if __name__ == "__main__":
    cli.cli()
