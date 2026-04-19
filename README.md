# Blogging App

A full-featured blogging REST API built with **FastAPI** following along with the
[FastAPI Course by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI).

> 🚧 Work in progress — actively being built as I work through the course.

---

## Tech Stack

- **Python** + **uv** (package manager)
- **FastAPI**
- **Jinja2** — HTML templating

---

## Project Structure

```
blogging-app/
├── static/
│   ├── css/
│   ├── icons/
│   ├── js/
│   └── profile_pics/
├── templates/
│   ├── layout.html
│   └── home.html
├── notes/
├── main.py
├── pyproject.toml
└── uv.lock
```

---

## Getting Started

### Prerequisites
- Python 3.x
- [uv](https://astral.sh/uv)

### Run locally

```bash
git clone https://github.com/archihalder/blogging-app.git
cd blogging-app
uv run fastapi dev main.py
```

---

## Notes

Personal learning notes are in the [`notes/`](./notes) folder.

---

## Reference

**FastAPI Course** by [Corey Schafer](https://www.youtube.com/@coreyms)