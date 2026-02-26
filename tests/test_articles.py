"""
Tests for article utility functions.
"""
import os
import pytest
from utils import save_article, get_article, delete_article, list_articles
from config import ARTICLES_DIR

def test_save_and_get_article():
    """
    Test saving and retrieving an article.
    """
    title = "Test Article"
    content = "Test content"
    date = "2026-02-25"
    filename = save_article(title, content, date)
    article = get_article(filename)
    assert article["title"] == title
    assert article["date"] == date
    assert "Test content" in article["content"]
    delete_article(filename)

def test_delete_article():
    """
    Test deleting an article.
    """
    title = "Delete Article"
    content = "Content"
    date = "2026-02-25"
    filename = save_article(title, content, date)
    assert os.path.exists(os.path.join(ARTICLES_DIR, filename))
    assert delete_article(filename)
    assert not os.path.exists(os.path.join(ARTICLES_DIR, filename))

def test_list_articles():
    """
    Test listing articles.
    """
    title = "List Article"
    content = "Content"
    date = "2026-02-25"
    filename = save_article(title, content, date)
    articles = list_articles()
    assert any(a["filename"] == filename for a in articles)
    delete_article(filename)
