import sys
from gi.repository import Gtk, Gdk, WebKit

class BrowserTab(Gtk.VBox):
    def __init__(self, *args, **kwargs):
        super(BrowserTab, self).__init__(*args, **kwargs)

        self.url_bar = Gtk.Entry()
        self.url_bar.connect("activate", self._load_url)
        self.tasks_button = Gtk.Button("Tasks")
        self.webview = WebKit.WebView()
        self.show()

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)

        self._setup_find_dialog()

        url_box = Gtk.HBox()
        url_box.pack_start(self.url_bar, True, True, 0)
        url_box.pack_start(self.tasks_button, False, False, 0)

        self.pack_start(url_box, False, False, 0)
        self.pack_start(scrolled_window, True, True, 0)
        self.pack_start(self.find_box, False, False, 0)

        url_box.show_all()
        scrolled_window.show()

    def _load_url(self, widget):
        url = self.url_bar.get_text()
        if not "://" in url:
            url = "http://" + url
        self.webview.load_uri(url)

    def _setup_find_dialog(self):
        find_box = Gtk.HBox()
        close_button = Gtk.Button("Close")
        close_button.connect("clicked", lambda x: find_box.hide())
        self.find_entry = Gtk.Entry()
        self.find_entry.connect("activate",
                                lambda x: self.webview.search_text(self.find_entry.get_text(),
                                                                   False, True, True))
        prev_button = Gtk.Button("<")
        next_button = Gtk.Button(">")
        prev_button.connect("clicked",
                            lambda x: self.webview.search_text(self.find_entry.get_text(),
                                                               False, False, True))
        next_button.connect("clicked",
                            lambda x: self.webview.search_text(self.find_entry.get_text(),
                                                               False, True, True))
        find_box.pack_start(close_button, expand=False, fill=False, padding=0)
        find_box.pack_start(self.find_entry, expand=False, fill=False, padding=0)
        find_box.pack_start(prev_button, expand=False, fill=False, padding=0)
        find_box.pack_start(next_button, expand=False, fill=False, padding=0)
        self.find_box = find_box

class Browser(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(Browser, self).__init__(*args, **kwargs)

        # create notebook and tabs
        self.notebook = Gtk.Notebook()
        self.notebook.set_scrollable(True)

        # basic stuff
        self.tabs = []
        self.set_size_request(400, 400)

        # create a first, empty browser tab
        self.tabs.append((self._create_tab(), Gtk.Label("New Tab")))
        self.notebook.append_page(*self.tabs[0])

        self._setup_task_dialog()

        self.split_browser_container = Gtk.HBox()
        self.split_browser_container.pack_start(self.notebook, True, True, 0)
        self.split_browser_container.pack_start(self.tasks_box, False, False, 0)
        self.add(self.split_browser_container)

        # connect signals
        self.connect("destroy", Gtk.main_quit)
        self.connect("key-press-event", self._key_pressed)
        self.notebook.connect("switch-page", self._tab_changed)

        self.split_browser_container.show_all()
        self.show()

    def _setup_task_dialog(self):
        self.tasks_box = Gtk.VBox()
        self.tasks_box.set_size_request(360, 32)

        add_task_button = Gtk.Button("+ Task")
        self.tasks_box.pack_start(add_task_button, False, False, 0)
        add_task_button.show()

    def _tab_changed(self, notebook, current_page, index):
        if not index:
            return
        title = self.tabs[index][0].webview.get_title()
        if title:
            self.set_title(title)

    def _title_changed(self, webview, frame, title):
        current_page = self.notebook.get_current_page()

        counter = 0
        for tab, label in self.tabs:
            if tab.webview is webview:
                label.set_text(title)
                if counter == current_page:
                    self._tab_changed(None, None, counter)
                break
            counter += 1

    def _create_tab(self):
        tab = BrowserTab()
        tab.webview.connect("title-changed", self._title_changed)
        return tab

    def _current_tab_webview(self):
        return self.tabs[self.notebook.get_current_page()][0].webview

    def _close_current_tab(self):
        if self.notebook.get_n_pages() == 1:
            return
        page = self.notebook.get_current_page()
        current_tab = self.tabs.pop(page)
        self.notebook.remove(current_tab[0])

    def _open_new_tab(self):
        current_page = self.notebook.get_current_page()
        page_tuple = (self._create_tab(), Gtk.Label("New Tab"))
        self.tabs.insert(current_page + 1, page_tuple)
        self.notebook.insert_page(page_tuple[0], page_tuple[1], current_page+1)
        self.notebook.set_current_page(current_page+1)

    def _focus_url_bar(self):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].url_bar.grab_focus()

    def _raise_find_dialog(self):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].find_box.show_all()
        self.tabs[current_page][0].find_entry.grab_focus()

    def _toggle_task_list(self):
        pass

    def _key_pressed(self, widget, event):
        modifiers = Gtk.accelerator_get_default_mod_mask()
        mapping = {
            # Handling tabs
            Gdk.KEY_t:     self._open_new_tab,
            Gdk.KEY_w:     self._close_current_tab,

            # Current tab actions
            Gdk.KEY_r:     lambda: self._current_tab_webview().reload(),
            Gdk.KEY_Left:  lambda: self._current_tab_webview().go_back(),
            Gdk.KEY_Right: lambda: self._current_tab_webview().go_forward(),

            # In-page actions
            Gdk.KEY_f:     self._raise_find_dialog,

            # Taskbar cnotrol
            #Gdk.KEY_l:     self._toggle_task_list,

            # Global shortcuts
            Gdk.KEY_u:     self._focus_url_bar,
            Gdk.KEY_q:     Gtk.main_quit
        }

        if event.state & modifiers == Gdk.ModifierType.CONTROL_MASK \
          and event.keyval in mapping:
            mapping[event.keyval]()

if __name__ == "__main__":
    Gtk.init(sys.argv)
    browser = Browser()
    Gtk.main()