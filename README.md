Forked from https://github.com/tastejs/todomvc/tree/gh-pages/examples/elm

Added a time-count feature and a server to view client states.

You can use it to track your work status as well as your colleagues'.

HOW TO DEPLOY
===
1. Install python and the [elm platform](http://elm-lang.org/install)
1. Create a folder hierarchy like this:
     - server
       - *todos-server.py* 
       - static
         - *index.html*
         - *elm.js*
         - *style.css*
         - *table_style.css*
       - data
       - templates
         - view_all.tmpl
         - view_one.tmpl
1. In *Todo.elm*, set the variable `todomvc_server_url` to your server url
2. Run `elm-make Todo.elm --output elm.js` to generate the new *elm.js* and replace the old one
2. In *todo-server.py*, set the arguments of `app.run()` to your host and port
4. Run `pip install flask` to install flask
5. Run `python todoserver.py`
5. Go to your server in web browser
