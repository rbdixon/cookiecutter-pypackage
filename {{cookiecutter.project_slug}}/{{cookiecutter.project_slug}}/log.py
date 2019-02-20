import sys
import logging

from coloredlogs import ColoredFormatter

__all__ = ['configure_logging']

FORMAT = '%(levelname)8s [%(name)24s]: %(message)s'
LOG_FIELD_STYLES = {
    'asctime': {'color': 'green'},
    'hostname': {'color': 'magenta'},
    'levelname': {'color': 'green', 'bold': True},
    'name': {'color': 'blue'},
    'programname': {'color': 'cyan'},
}


def configure_logging(level=logging.INFO):
    # Turn on logging
    root = logging.getLogger()
    root.setLevel(level)

    # Colors and formats
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    formatter = ColoredFormatter(fmt=FORMAT, field_styles=LOG_FIELD_STYLES)
    ch.setFormatter(formatter)
    root.addHandler(ch)
