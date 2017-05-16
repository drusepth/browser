# browser

A browser for Doing Stuff.

# Design decisions

* As I use a tiling WM on a laptop, screen real estate is prime. Browser UI should be hidden by default and temporarily shown by keyboard shortcuts, leaving the maximum number of pixels for page content.
* This is a browser built around completing tasks and everything associated with that. You'll find lots of functionality around to-do lists, and not so much functionality around arbitrary extensions and other fun fluff.

# Keyboard shortcuts

The default mod-key is `ctrl`.

* `mod`+`t` - Open a new tab
* `mod`+`u` - Highlight the URL bar
* `mod`+`w` - Close the current tab
* `mod`+`r` - Refresh the current page
* `mod`+`left` - Navigate backwards a page
* `mod`+`right` - Navigate forwards a page
* `mod`+`f` - Find words on the current page
* `mod`+`l` - Toggle showing to-do list
* `mod`+`q` - Quit

# Expected keyboard shortcuts

These shortcuts don't exist yet, but are listed for planning purposes.

* `mod`+# - Switch to tab # (number keys)
* `alt`+# - Switch context to todo item # (number keys)
* `mod`+`a` - Associate current tab with current todo item
* `mod`+`d` - Remove current tab's association with current todo item
* `mod`+`h` - Hide all tabs not associated with the current todo item
* `mod`+`j` - Show all tabs
* `mod`+`enter` - Mark current todo item as complete
* `mod`+`p` - Start/stop time tracking for the current todo item

# Still to do

* TODO list management
  - Creating todo items
  - Editing todo items
  - Deleting todo items
  - Marking todo items complete
  - Associating current tab with a todo item
  - Opening all tabs related to a todo item
  - Closing all tabs related to a todo item
  - Time tracking on todo items