import os

from pathlib import Path
from split_settings.tools import include

from management.config import settings


include(
    "components/*.py",
)

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    INSTALLED_APPS.append("debug_toolbar_force")

    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    MIDDLEWARE.append("debug_toolbar_force.middleware.ForceDebugToolbarMiddleware")
