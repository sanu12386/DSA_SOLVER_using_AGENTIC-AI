import sqlite3
import os
from datetime import datetime

# Ensure DB file is in the same directory as this file
DB_FILE = os.path.join(os.path.dirname(__file__), "runs.db")
print(f"[DEBUG] Using database at: {DB_FILE}")

def init_db():
    """Create the runs table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            question TEXT,
            sample_input TEXT,
            plan TEXT,
            approach TEXT,
            code TEXT,
            dry_run TEXT,
            output TEXT,
            complexity TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_run(question, sample_input, plan, approach, code, dry_run, output, complexity):
    """Insert a run into the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO runs (timestamp, question, sample_input, plan, approach, code, dry_run, output, complexity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        question, sample_input, plan, approach, code, dry_run, output, complexity
    ))
    conn.commit()
    conn.close()
    print("[DEBUG] Run saved successfully")

def fetch_history():
    """Fetch list of previous runs (id, timestamp, question)."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, timestamp, question FROM runs ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_run_by_id(run_id):
    """Fetch full run details by id."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, timestamp, question, sample_input, plan, approach, code, dry_run, output, complexity
        FROM runs WHERE id=?
    """, (run_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "timestamp": row[1],
            "question": row[2],
            "sample_input": row[3],
            "plan": row[4],
            "approach": row[5],
            "code": row[6],
            "dry_run": row[7],
            "output": row[8],
            "complexity": row[9],
        }
    return None







