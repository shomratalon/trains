# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from ..utils import PY32

if PY32:
    from .thread_extractor import ThreadExtractor as Extractor
else:
    from .gevent_extractor import GeventExtractor as Extractor
