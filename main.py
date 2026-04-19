from fastapi import FastAPI, Request, HTTPException, status
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


# {post_id} tells FastAPI that this is a path parameter and part of the url
# it is a variable and it should be captured and passed to the method.
# The type int for post_id in the method is important as this helps
# FastAPI to automatically validate the input
@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
