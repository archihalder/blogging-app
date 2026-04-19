# Jinja2 Templates

These are blocks of code inside HTML files that can be used to replace/fetch code from a FastAPI service and they help render the HTML dynamically.

There are a few template types in this:
- `{{ ... }}` for expressions
- `{% ... %}` for statements
- `{# ... #}` for comments

## How is it linked to a REST API using FastAPI?

First we import a module `from fastapi.templating import Jinja2Templates`.
This requires a `Request` module from `fastapi` as well. So, we import that too.
Then we create a Jinja2Template instance, which looks for "templates" in a given directory.
And it works like this.

```python
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Blog Home"}
    )
```
`templates` is a Jinja2Templates instance.
Calling TemplateResponse does three things:
  1. finds home.html inside the templates directory
  2. processes any jinja2 syntax in the html file
  3. returns a full html response to the browser
The third parameter is the context, so we gave the template
access to the list of dictionaries "posts"

the `request` object is passed because Jinja2Templates needs it
to build things like `request.url_for()` inside the template

## How to use static files such as CSS, icons, favicons or images in these templates?

We can link CSS, icons, favicons and images using `href` and provide their path.
But later in our development if we decide to update our routes, it becomes challenging.
To tackle this, we use `StaticFiles`. This is a module that needs to be imported.
We mount this on our FastAPI app, like this.

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

We need to mount the static files on to our fastapi app.
This takes three parameters:
  1. takes the url path where static files are stored
  2. StaticFiles instance that points to the static files directory
  3. the `name` parameter lets us reference this mount by name in `url_for()` calls inside templates

Now, we can use `url_for` to connect these static files to our html and get dynamic routing.
```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', path='css/main.css') }}">
```

## Why to use `url_for()` for static files? What would happen if we don't use it?

Let's say yoou have this hardcoded in your template:

```html
<link rel="stylesheet" href="/static/style.css">
```

And your app mounts static files at `/static`. Everything works fine.
Now you decide to reorganize and change the mount point to `/assets`:

```python
app.mount("/assets", StaticFiles(directory="static"), name="static")
```

Your CSS is now at `/assets/style.css`, but your template still says `/static/style.css`. That file no longer exists at that path — the browser gets a `404`, the stylesheet doesn't load, and your page breaks.
You'd have to manually hunt down every hardcoded `/static/...` reference across every template and update them one by one.

With `url_for` instead:

```html
<link rel="stylesheet" href="{{ request.url_for('static', path='/style.css') }}">
```

When you change the mount point to `/assets`, `url_for('static', ...)` automatically resolves to `/assets/style.css` because it looks up the mount by **name**, not by path. You change one line in your Python file and every template updates for free.

## We can use `url_for()` for navigation links too

Like I mentioned above, `url_for()` looks for the **name**, not the path. So, for a `nav` element if we pass `href="{{ url_for('home') }}"`, it will look for the route named `home`, which is the method name.

```python
@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Blog Home"}
    )
```

In this example, if we didn't have the `name` parameter for the routes, `url_for()` will take the method name `home`. But there's a bug here. If we click on Home Page, the url will go to `/posts` not `/` because of the decorator execution order in Python. Decorators run bottom-up (closest to the function first), so `/posts` gets registered before `/`.

To clear this confusion, we add `name` parameter to the routes. And now, `url_for()` will look for these `name` parameter.
