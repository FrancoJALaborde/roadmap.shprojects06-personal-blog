"""
Utility functions for article management.
"""
import os
import markdown
from datetime import datetime
from typing import List, Dict

from config import ARTICLES_DIR

def list_articles() -> List[Dict]:
    """
    List all available articles.
    Returns:
        List[Dict]: List of article metadata and content.
    """
    articles = []
    for filename in os.listdir(ARTICLES_DIR):
        if filename.endswith(".md"):
            path = os.path.join(ARTICLES_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                # First line: title, second line: date, rest: content
                title = lines[0].strip("# ").strip()
                date = lines[1].strip()
                content = "".join(lines[2:])
                articles.append({
                    "filename": filename,
                    "title": title,
                    "date": date,
                    "content": content
                })
    articles.sort(key=lambda x: x["date"], reverse=True)
    return articles

def get_article(filename: str) -> Dict:
    """
    Retrieve an article by its filename.
    Args:
        filename (str): The article filename.
    Returns:
        Dict: Article metadata and HTML content, or None if not found.
    """
    path = os.path.join(ARTICLES_DIR, filename)
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        title = lines[0].strip("# ").strip()
        date = lines[1].strip()
        content = "".join(lines[2:])
        html_content = markdown.markdown(content)
        return {
            "filename": filename,
            "title": title,
            "date": date,
            "content": html_content
        }

def save_article(title: str, content: str, date: str, filename: str = None) -> str:
    """
    Save a new or existing article.
    Args:
        title (str): Article title.
        content (str): Article content.
        date (str): Publication date.
        filename (str, optional): Filename to overwrite. If None, a new file is created.
    Returns:
        str: The filename used.
    """
    if not filename:
        filename = f"{title.lower().replace(' ', '_')}_{date}.md"
    path = os.path.join(ARTICLES_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n{date}\n{content}")
    return filename

def delete_article(filename: str) -> bool:
    """
    Delete an article.
    Args:
        filename (str): The article filename.
    Returns:
        bool: True if deleted, False if not found.
    """
    path = os.path.join(ARTICLES_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
