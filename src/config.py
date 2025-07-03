import os

from utils import helpers

for key, value in os.environ.items():
    globals()[key] = helpers.auto_cast(value)
