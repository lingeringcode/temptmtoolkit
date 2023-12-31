"""
tmtoolkit – Text Mining and Topic Modeling Toolkit for Python

Markus Konrad <markus.konrad@wzb.eu>
"""

from importlib.util import find_spec
import logging

__title__ = 'tmtoolkit'
__version__ = '0.11.2'
__author__ = 'Markus Konrad'
__license__ = 'Apache License 2.0'

logger = logging.getLogger(__title__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.WARNING)   # set default level


from . import bow, topicmod, tokenseq, types, utils

if not any(find_spec(pkg) is None for pkg in ('spacy', 'bidict', 'loky')):
    from . import corpus
