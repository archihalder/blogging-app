from fastapi import FastAPI, Request  # Jinja2 templates require Request parameter
from fastapi.staticfiles import StaticFiles
# required for using static files like css or icons

from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# we need to mount the static files on to our fastapi app
# this takes three parameters
#   1. takes the url path where static files are stored
#   2. StaticFiles instance that points to the static files directory
#   3. we use name parameter to reference "static" in our templates
#       this means we can use "/static/css/main.css" in our templates

templates = Jinja2Templates(directory="templates")
# looks for template files in our templates directory

posts: list[dict] = [
    {
        "id": 1,
        "author": "Archi Halder",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 19, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is great and awesome",
        "content": "Python is great for machine learning and data analysis",
        "date_posted": "April 15, 2026",
    },
]


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Blog Home"}
    )


# templates is a Jinja2Templates instance
# calling TemplateResponse does three things:
#   1. finds home.html inside the templates directory
#   2. processes any jinja2 syntax in the html file
#   3. returns a full html response to the browser
# the third parameter is the context, so we gave the template
# access to the list of dictionaries "posts"

# the request object is passed because Jinja2Templates needs it
# to build things like request.url_for() inside the template


@app.get("/api/posts")
def get_posts():
    return posts
