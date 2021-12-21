from dotenv import load_dotenv
import os


load_dotenv(dotenv_path=".env")


PG_CONFIG = dict(
    host=os.environ.get("PG_HOST", "localhost"),
    port=os.environ.get("PG_PORT", 5432),
    user=os.environ.get("PG_USER", "postgres"),
    password=os.environ.get("PG_PASSWORD", None),
    database=os.environ.get("PG_DATABASE", "srr"),
)
