'''Console script for {{cookiecutter.project_slug}}.'''

import sys
import click
import logging

from .log import configure_logging

log = logging.getLogger(__name__)


@click.group(invoke_without_command=True)
@click.option('--debug', is_flag=True, default=False, help='Enable debugging.')
@click.pass_context
def main(ctx, debug, args=None):
    '''Console script for {{cookiecutter.project_slug}}.'''

    if debug:
        configure_logging(level=logging.DEBUG)
    else:
        configure_logging()

    click.echo(
        'Replace this message by putting your code into '
        '{{cookiecutter.project_slug}}.cli.main'
    )
    click.echo('See click documentation at http://click.pocoo.org/')
    return 0


@main.command()
def cmd():
    'Do something.'
    pass


if __name__ == '__main__':
    sys.exit(
        main(auto_envvar_prefix='{{cookiecutter.project_slug|upper}}')
    )  # pragma: no cover
