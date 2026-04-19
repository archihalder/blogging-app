# Getting started with FastAPI with uv

## How to install uv and FastAPI

for uv go to the installation page from astral.sh or use this
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

then to install fastapi, run this command
```bash
uv add "fastapi[standard]"
```

## Create a uv app

```bash
uv init fastapi_blog
```
this creates a directory named "fastapi_blog" in the current directory
this creates a template of how a uv project looks like
it initiates a git repository for this project, a toml file with a main.py as the starting point.

## Create a FastAPI app

We just need to import the fastapi module and call the FastAPI method

```python
from fastapi import FastAPI

app = FastAPI()
```

## How to run a FastAPI app

if we were using `pip` then we could have written
```bash
fastapi dev main.py
```

but since we are using `uv`, we can write
```bash
uv run fastapi dev main.py
```

this runs the fastapi using uv, and it's a bit faster

the app runs on the port `8000`. so the url is `http://127.0.0.1/8000` or `http://localhost:8000`

## Create routes using FastAPI

FastAPI requires decorators to create api routes

```python
@app.get("/api/posts")
def get_posts():
    return "Welcome to the posts"
```

it exposes our return item which is a string in this case to the endpoint `/api/posts`
so when we go this endpoint, `http://localhost:8000/api/posts`, we get to see our string

instead of the string, if we pass in a list of dictionaries, fastapi will translate that
into an array of jsons, which is very useful

## FastAPI docs

If we just append `/docs` to our url we get a swagger ui listing all our APIs
i.e., at `http://localhost:8000/docs`

There's also a newer version of this docs, and to access this we have to append `/redoc`
This new one is kind of weird, doesn't work like the swagger ui one.

I prefer the swagger ui 

## How to pass HTML as a response

First we have to import the module for this.
and then add `HTML_Response` to the response_class parameter inside the decorator

```python
@app.get("/", response_class=HTMLResponse)
def home():
    return f"<h1>{posts[0]['title']}</h1>"
```

this would return an html file, which gets easily rendered by the browswer

## Is passing HTML reponse a good idea?

It is helpful, but we don't want this api in the swagger ui
because in the swagger ui we prefer to get json as the response
So, in this case, we can ignore the apis which are not returning json
by setting the parameter `include_in_schema=False` inside our decorator

```python
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"
```

## How to have the same response in multiple APIs?

For this we just need to add another decortor on top of our method
and fastapi will take care of the rest

```python
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"
```

So, these both APIs `/` and `/posts` will show the same html response
but won't be visible in the swagger ui
