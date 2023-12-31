"""
Tests for importing optional tmtoolkit.corpus module.

.. codeauthor:: Markus Konrad <markus.konrad@wzb.eu>
"""

from importlib.util import find_spec

import pytest


def test_import_corpus():
    if any(find_spec(pkg) is None for pkg in ('spacy', 'bidict', 'loky')):
        with pytest.raises(RuntimeError, match='^the required package'):
            from temptmtoolkit import corpus
        with pytest.raises(RuntimeError, match='^the required package'):
            from temptmtoolkit.corpus import Corpus
    else:
        from temptmtoolkit import corpus
        from temptmtoolkit.corpus import Corpus
        import spacy
        import bidict
        import loky
