# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('drowser')

from drowser_lib import Window
from drowser.AboutDrowserDialog import AboutDrowserDialog
from drowser.PreferencesDrowserDialog import PreferencesDrowserDialog

# See drowser_lib.Window.py for more details about how this class works
class DrowserWindow(Window):
    __gtype_name__ = "DrowserWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(DrowserWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutDrowserDialog
        self.PreferencesDialog = PreferencesDrowserDialog

        # Code for other initialization actions should be added here.

