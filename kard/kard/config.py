from pathlib import Path
from dotenv import load_dotenv, dotenv_values

import os

import logging

env_path = Path().absolute() / "kard"/".env"
load_dotenv(env_path)
# conf = dotenv_values(dotenv_path=env_path)
# logging.warning(conf, env_path)

DB_URL = f"postgresql+psycopg2://{os.environ.get('PG_USER')}:{os.environ.get('PG_PASSWORD')}@{os.environ.get('PG_HOST')}:{os.environ.get('PG_PORT')}/{os.environ.get('PG_DATABASE')}"
