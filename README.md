# Blog Post in Django (Django Templates)

This is a small, educational Django project that implements a simple blog with user registration (email-based), login, and CRUD operations for posts. It uses Django templates (DTL), SQLite for development, and crispy-forms with Bootstrap for form rendering.

## Quick summary

- Framework: Django 5.2.7 (see `requirements.txt`)
- UI: Bootstrap (via CDN) and `django-crispy-forms` with the `bootstrap4` pack
- Database: SQLite (`db.sqlite3` in the repo root)
- App: single app named `posts` implementing Posts and Profile models

## Main features (from the code)

- Post model with title, content, timestamps, and an author (ForeignKey to Django `User`). Posts are listed on the home page and can be created, edited, deleted by authenticated users (only the post author can edit/delete).
- Profile model that stores a one-to-one link to `User` and a unique email. Registration creates a Profile.
- Registration flow generates a username automatically (format `user_<n>`) and uses the provided email for login.
- Login is email-based: the `Profile` is looked up by email and then the linked `User`'s password is checked.
- Auth-protected views: `create`, `edit`, `delete`, and `myposts` require login.

## Models (exact fields)

- Posts
  - `title: CharField(max_length=200)`
  - `content: TextField()`
  - `created_at: DateTimeField(auto_now_add=True)`
  - `updated_at: DateTimeField(auto_now=True)`
  - `author: ForeignKey(User, on_delete=models.CASCADE)`

- Profile
  - `user: OneToOneField(User, on_delete=models.CASCADE)`
  - `email: EmailField(unique=True)`

## Forms

- `CreatePostForm` / `EditPostForm` — ModelForms for `Posts` with `title` and `content` fields.
- `RegisterForm` — extends `UserCreationForm`, collects `email`, `password1`, `password2`; creates `User` and `Profile` (email stored on profile).
- `LoginForm` — simple form with `email` and `password`.

## URL routes (from `posts/urls.py`)

- `/` — Home, lists posts. (name: `posts-home`)
- `/post/<int:pk>/` — Post detail page. (name: `detail`)
- `/post/new/` — Create a new post (login required). (name: `create-post`)
- `/post/<int:pk>/edit/` — Edit a post (login required, author only). (name: `edit`)
- `/post/<int:pk>/delete/` — Delete a post (login required, author only). (name: `delete-post`)
- `/register/` — Register a new account (creates User + Profile). (name: `register`)
- `/login/` — Login using email and password. (name: `login`)
- `/logout/` — Logout endpoint. (name: `logout`)
- `/myposts/` — List posts authored by the logged-in user (login required). (name: `myposts`)

The project `blogpost/urls.py` includes `posts.urls` at the root and exposes the Django admin at `/admin/`.

## Templates and static

- Templates (under `posts/templates/posts/`): `base.html`, `home.html`, `detail.html`, `create.html`, `edit.html`, `delete.html`, `login.html`, `register.html`, `myposts.html`.
- Static CSS (under `posts/static/posts/main.css`) for basic styling. Bootstrap is loaded from CDN in the base template.

## Dependencies (from `requirements.txt`)

- Django==5.2.7
- asgiref==3.10.0
- crispy-bootstrap4==2025.6
- django-crispy-forms==2.4
- sqlparse==0.5.3
- tzdata==2025.2

Install with:

```powershell
pip install -r requirements.txt
```

## Development setup (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations (creates the SQLite DB if not present):

```powershell
python manage.py migrate
```

4. (Optional) Create a superuser for /admin/:

```powershell
python manage.py createsuperuser
```

5. Run the development server:

```powershell
python manage.py runserver
```

6. Open http://127.0.0.1:8000/ in your browser.

Note: There are no automated tests included in this repository yet.

## Admin

The `Posts` and `Profile` models are registered in `posts/admin.py`, so after creating a superuser you can manage posts and profiles via `/admin/`.

## Security / constraints in code

- DEBUG = True in `blogpost/settings.py` — this is intended for development only.
- Email is used as the unique identifier in `Profile` and for login; usernames are auto-generated during registration (format `user_<n>`).
- Views that edit or delete posts check that `post.author == request.user` and return HTTP 403 otherwise.

---

