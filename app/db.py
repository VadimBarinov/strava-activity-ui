import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection
from flask import (
    current_app,
    g,
    Flask,
)
from contextlib import contextmanager

class DatabaseHelper:
    def get_db(self) -> connection:
        if "db" not in g:
            g.db = psycopg2.connect(
                current_app.config["DATABASE_URL"],
                cursor_factory=RealDictCursor,
            )
        return g.db

    def close_db(self, e = None) -> None:
        db = g.pop("db", None)
        if db is not None:
            db.close()
    
    @contextmanager
    def get_db_cursor(self):
        conn = self.get_db()
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
    
    def init_app(self, app: Flask):
        app.teardown_appcontext(self.close_db)


database_helper: DatabaseHelper = DatabaseHelper()