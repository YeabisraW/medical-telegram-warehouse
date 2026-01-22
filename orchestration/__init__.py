from dagster import Definitions, load_assets_from_modules
from . import assets  # This looks for assets.py in the same folder

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)