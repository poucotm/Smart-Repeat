# -*- coding: utf8 -*-
# -----------------------------------------------------------------------------
# Author : yongchan jeon (Kris) poucotm@gmail.com
# File   : Smart Repeat.py
# Create : 2017-08-28 22:28:38
# Editor : sublime text3, tab size (4)
# -----------------------------------------------------------------------------

import sublime, sublime_plugin
import sys, imp

mods = ['Smart Repeat.core.engine']
for mod in sys.modules:
    if any(mod == m for m in mods):
        imp.reload(sys.modules[mod])

from .core.engine import *

def plugin_loaded():
    from package_control import events

    if events.install('Smart Repeat'):
        print('Installed %s' % events.install('Smart Repeat'))

def plugin_unloaded():
    from package_control import events

    if events.remove('Smart Repeat'):
        print('Removing %s' % events.remove('Smart Repeat'))
