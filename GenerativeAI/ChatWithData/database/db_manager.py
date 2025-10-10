import sqlite3
from pathlib import Path

from config.settings import DB_PATH


def init_db():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            author TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_text(title, genre, author, content):
    """Insert text content into the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO texts (title, genre, author, content) VALUES (?, ?, ?, ?)", 
                   (title, genre, author, content))
    conn.commit()
    conn.close()

def get_all_texts():
    """Retrieve all text content from the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, author, content FROM texts ORDER BY created_at DESC")
    data = cursor.fetchall()
    conn.close()
    return data

def get_texts_by_genre(genre):
    """Retrieve texts filtered by genre"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, author, content FROM texts WHERE genre = ? ORDER BY created_at DESC", (genre,))
    data = cursor.fetchall()
    conn.close()
    return data

def get_texts_by_author(author):
    """Retrieve texts filtered by author"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, author, content FROM texts WHERE author = ? ORDER BY created_at DESC", (author,))
    data = cursor.fetchall()
    conn.close()
    return data

def search_texts(search_term):
    """Search texts by title, author, or content"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, genre, author, content FROM texts 
        WHERE title LIKE ? OR author LIKE ? OR content LIKE ?
        ORDER BY created_at DESC
    """, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    data = cursor.fetchall()
    conn.close()
    return data

def get_text_count():
    """Get the total number of text entries"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM texts")
    count = cursor.fetchone()[0]
    conn.close()
    return count
