from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:16-alpine") as postgres:
        yield postgres


@pytest.fixture(scope="session")
def setup_database(postgres_container):
    raw_url = postgres_container.get_connection_url()
    db_url = "postgresql+asyncpg://" + raw_url.split("://")[1]

    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent.parent
    ini_path = str(project_root / "alembic.ini")
    script_location = str(project_root / "migrations")

    alembic_cfg = Config(ini_path)
    alembic_cfg.set_main_option("script_location", script_location)
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)

    command.upgrade(alembic_cfg, "head")

    return db_url
