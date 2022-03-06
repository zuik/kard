from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from dotenv import load_dotenv
from pathlib import Path

import os
import logging

logger = logging.getLogger("alembic.env")


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from kard import models

target_metadata = models.Base.metadata


# overwrite alembic.ini db urls from the config file
env_path = Path(".").parent / ".env"

load_dotenv(env_path)

if os.environ.get("PG_HOST"):
    pg_url = f"postgresql+psycopg2://{os.environ.get('PG_USER')}:{os.environ.get('PG_PASSWORD')}@{os.environ.get('PG_HOST')}:{os.environ.get('PG_PORT')}/{os.environ.get('PG_DATABASE')}"
    config.set_section_option("alembic", "sqlalchemy.url", pg_url)
else:
    logger.warning(
        "Environment variable SETTINGS missing - use default alembic.ini configuration"
    )


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
