"""init-db

Revision ID: 68ae11fbc5d1
Revises: 
Create Date: 2026-05-27 15:26:57.255415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68ae11fbc5d1'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE users (
            id TEXT PRIMARY KEY,
            username VARCHAR(255),
            firstname VARCHAR(255),
            lastname VARCHAR(255)
        );
        CREATE TABLE types (
            id TEXT PRIMARY KEY,
            type VARCHAR(255)
        );
        CREATE TABLE maps (
            id TEXT PRIMARY KEY,
            summary_polyline TEXT
        );
        CREATE TABLE activities (
            id TEXT PRIMARY KEY,
            user_id TEXT REFERENCES users(id),
            name TEXT,
            start_date TIMESTAMP,
            type_id TEXT REFERENCES types(id),
            distance REAL,
            moving_time REAL,
            average_speed REAL,
            max_speed REAL,
            total_elevation_gain REAL,
            average_heartrate REAL,
            max_heartrate REAL,
            map_id TEXT REFERENCES maps(id),
            intensity_score REAL,
            target INTEGER
        );
        INSERT INTO types (id, type)
        VALUES 
            ('Ride', 'Ride'),
            ('Run', 'Run');
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE activities;
        DROP TABLE users;
        DROP TABLE maps;
        DROP TABLE types;
    """)
