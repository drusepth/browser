# browser

A browser for Doing Stuff.

# Design decisions

* As I use a tiling WM on a laptop, screen real estate is prime. Browser UI should be hidden by default and temporarily shown by keyboard shortcuts, leaving the maximum number of pixels for page content.
* This is a browser built around completing tasks and everything associated with that. You'll find lots of functionality around to-do lists, and not so much functionality around arbitrary extensions and other fun fluff.

# Keyboard shortcuts

The default mod-key is `ctrl`.

* `mod`+`t` - Open a new tab
* `mod`+`l` - Highlight the URL bar
* `mod`+`w` - Close the current tab
* `mod`+`r` - Refresh the current page
* `mod`+`left` - Navigate backwards a page
* `mod`+`right` - Navigate forwards a page
* `mod`+`f` - Find words on the current page
* `mod`+`q` - Quit

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