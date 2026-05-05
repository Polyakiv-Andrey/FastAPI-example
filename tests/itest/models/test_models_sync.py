from alembic.autogenerate import compare_metadata
from alembic.runtime.migration import MigrationContext
from sqlalchemy import make_url
from sqlalchemy.ext.asyncio import create_async_engine

from src.models import Base


async def test_database_schema_matches_models(setup_database):
    url = make_url(setup_database).set(drivername="postgresql+asyncpg")
    engine = create_async_engine(url)

    async with engine.connect() as connection:

        def check_diff(sync_conn):
            context = MigrationContext.configure(sync_conn)
            diff = compare_metadata(context, Base.metadata)
            return diff

        diff = await connection.run_sync(check_diff)
    assert diff == []
    await engine.dispose()
