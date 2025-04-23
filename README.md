
---

```markdown
# 🧠 Hyperion Django App

This is a Django web application that includes user authentication, a blog, and a polling system.

## 🔐 Features

- **User Authentication**
  - Secure login and registration system
  - Protected views using Django's built-in decorators and mixins

- **Blog Section**
  - Displays blogs on topics I find interesting
  - Built with Django's `ListView` and `DetailView`
  - Only accessible to authenticated users

- **Polls Section**
  - Users can vote on polls about topics I care about
  - Displays results after voting
  - Built using Django models and views with voting logic

## 🚀 Tech Stack

- Python 3.11
- Django 4.x
- SQLite (default database)
- HTML/CSS (Django templates)
- Docker & Dockerfile support (optional)
- Sphinx (for auto-generating documentation)

## 📦 Setup Instructions

### Clone the Repo

```bash
git clone https://github.com/your-username/hyperion-django-app.git
cd hyperion-django-app
```

### Create Virtual Environment & Install Dependencies

```bash
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### Start the Development Server

```bash
python manage.py runserver
```

Access the site at: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Running with Docker

```bash
docker build -t django-hyperion .
docker run -p 8000:8000 django-hyperion
```

---

## 📖 Documentation

You can generate HTML documentation using Sphinx:

```bash
cd docs
make html
```

Then open `docs/build/html/index.html` in your browser.

---

## ✍️ Author

**Malaika Nkosi**  
Email: [malaikankosi7@gmail.com](mailto:malaikankosi7@gmail.com)
