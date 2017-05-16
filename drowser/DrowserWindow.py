# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk, WebKit
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

        # Windows
        self.AboutDialog = AboutDrowserDialog
        self.PreferencesDialog = PreferencesDrowserDialog

        # UI Components
        self.button_refresh   = self.builder.get_object('btnRefresh')
        self.text_url_address = self.builder.get_object('txtUrlAddress')
        self.web_window       = self.builder.get_object('webWindow')    
        self.toolbar_actions  = self.builder.get_object('toolbarActions')
        self.label_status     = self.builder.get_object('lblStatus')

        self.webkit_view      = WebKit.WebView()
    
        # Add WebKit widget to web window
        self.web_window.add(self.webkit_view)
        self.webkit_view.show()
        
        # Theme toolbar
        context = self.toolbar_actions.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)
    
    def on_btnRefresh_clicked(self, widget):
        self.label_status.set_text('Refreshing')
        self.webkit_view.reload()

    def on_txtUrlAddress_activate(self, widget):
        url = widget.get_text()
        self.label_status.set_text('Navigating to ' + url)
        self.webkit_view.open(url)

