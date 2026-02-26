"""
Main application for the personal blog.
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from utils import list_articles, get_article, save_article, delete_article
from config import ADMIN_USERNAME, ADMIN_PASSWORD, ARTICLES_DIR, SESSION_SECRET_KEY

app = Flask(__name__)
app.secret_key = SESSION_SECRET_KEY

# Ensure articles directory exists
if not os.path.exists(ARTICLES_DIR):
    os.makedirs(ARTICLES_DIR)

def is_logged_in() -> bool:
    """
    Check if the user is authenticated.
    Returns:
        bool: True if logged in, False otherwise.
    """
    return session.get("logged_in", False)

@app.route("/")
def home():
    """
    Render the home page with a list of articles.
    """
    articles = list_articles()
    return render_template("home.html", articles=articles)

@app.route("/article/<filename>")
def article(filename):
    """
    Render a single article page.
    Args:
        filename (str): The article filename.
    """
    article = get_article(filename)
    if not article:
        return "Article not found", 404
    return render_template("article.html", article=article)

@app.route("/admin/login", methods=["GET", "POST"])
def login():
    """
    Render and process the admin login form.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect credentials")
    return render_template("login.html")

@app.route("/admin/logout")
def logout():
    """
    Log out the admin user.
    """
    session.pop("logged_in", None)
    return redirect(url_for("home"))

@app.route("/admin/dashboard")
def dashboard():
    """
    Render the admin dashboard with article management options.
    """
    if not is_logged_in():
        return redirect(url_for("login"))
    articles = list_articles()
    return render_template("dashboard.html", articles=articles)

@app.route("/admin/add", methods=["GET", "POST"])
def add_article():
    """
    Render and process the add article form.
    """
    if not is_logged_in():
        return redirect(url_for("login"))
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        date = request.form["date"]
        save_article(title, content, date)
        return redirect(url_for("dashboard"))
    return render_template("add_article.html")

@app.route("/admin/edit/<filename>", methods=["GET", "POST"])
def edit_article(filename):
    """
    Render and process the edit article form.
    Args:
        filename (str): The article filename.
    """
    if not is_logged_in():
        return redirect(url_for("login"))
    article = get_article(filename)
    if not article:
        return "Article not found", 404
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        date = request.form["date"]
        save_article(title, content, date, filename)
        return redirect(url_for("dashboard"))
    return render_template("edit_article.html", article=article)

@app.route("/admin/delete/<filename>", methods=["POST"])
def delete_article_route(filename):
    """
    Process article deletion.
    Args:
        filename (str): The article filename.
    """
    if not is_logged_in():
        return redirect(url_for("login"))
    delete_article(filename)
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)
