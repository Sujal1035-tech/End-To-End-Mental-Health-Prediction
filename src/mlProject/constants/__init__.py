from pathlib import Path

# FIX: ROOT_DIR must go 2 levels up from src/mlProject/constants
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent

CONFIG_FILE_PATH = ROOT_DIR / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"
SCHEMA_FILE_PATH = ROOT_DIR / "schema.yaml"

