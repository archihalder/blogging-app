from fastapi import FastAPI, Request  # Jinja2 templates require Request parameter
from fastapi.staticfiles import StaticFiles
# required for using static files like css or icons

from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

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


# the hrefs url_for('home') is looking for this name
@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Blog Home"}
    )


@app.get("/api/posts")
def get_posts():
    return posts
