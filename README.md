# Personal Blog – Filesystem-based Flask Application (Matrix Style)

## Description

Project url: https://roadmap.sh/projects/personal-blog

This repository contains a simple personal blog web application built with **Python** and **Flask**.  
It allows you to write, publish, edit, and delete articles, with a clear separation between guest (public) and admin (private) sections.  
Articles are stored as Markdown files in the filesystem.  
The application features a "Matrix" movie-inspired visual style (green neon on black) applied via CSS.

---

## Features

- Guest Section
  - Home page: List all published articles
  - Article page: View article content and publication date

- Admin Section
  - Login/logout with basic authentication
  - Dashboard: Manage articles (add, edit, delete)
  - Add/Edit article forms

- Storage: Articles saved as Markdown files in `/articles`
- No JavaScript required
- Matrix-style UI (green-on-black, monospaced font)
- Unit and integration tests with `pytest`
- English docstrings and comments

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/FrancoJALaborde/personal_blog_matrix.git
cd personal_blog_matrix
```

### 2. Create and Activate a Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## Running the Application

1. Ensure the `articles/` directory exists.  
   The app will create it automatically if missing.

2. Start the Flask server:

```bash
python app.py
```

3. Open your browser and visit:  
   http://127.0.0.1:5000/

---

## Admin Access

- Default credentials:  
  - Username: `admin`  
  - Password: `password`

You can change these in `config.py`.

---

## Project Structure

```bash
personal_blog/
│
├── app.py                # Main Flask application
├── config.py             # Configuration (credentials, paths, secret key)
├── utils.py              # Article management utilities
├── requirements.txt      # Python dependencies

├── README.md             # This documentation
│
├── articles/             # Markdown files for articles
│
├── templates/            # Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   ├── article.html
│   ├── dashboard.html
│   ├── add_article.html
│   ├── edit_article.html
│   └── login.html
│
├── static/
│   └── style.css         # Matrix-style CSS
│
└── tests/                # Automated tests
    ├── test_app.py
    └── test_articles.py
```

---

## Running the Tests

1. Ensure your virtual environment is activated.
2. Run all tests with:

```bash
pytest tests/
```

- Tests cover utility functions and main application flows (home, login, dashboard, etc.).

---

## Customization

- Matrix Style:  
  The UI uses `static/style.css` for the Matrix look.  
  You can further customize colors, fonts, or add more effects as desired.

- Admin Credentials:  
  Change `ADMIN_USERNAME` and `ADMIN_PASSWORD` in `config.py`.

- Session Secret:  
  Change `SESSION_SECRET_KEY` in `config.py` for production use.

---

## Notes

- This project is for educational purposes and does not implement advanced security (e.g., password hashing, CSRF protection).
- Do **not** use hardcoded credentials in production.
- No JavaScript is required; all logic is handled server-side.

