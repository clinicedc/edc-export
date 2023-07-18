from __future__ import annotations

import os
import shutil
import sys
from typing import TYPE_CHECKING

from edc_utils import get_utcnow

if TYPE_CHECKING:
    from datetime import datetime

    from django.contrib.auth.models import User


class FilesArchiver:
    """Archives a folder of CSV files using make_archive."""

    def __init__(
        self,
        path: str = None,
        exported_datetime: datetime = None,
        user: User = None,
        date_format: str = None,
        verbose: bool | None = None,
    ):
        self.exported_datetime: datetime = exported_datetime or get_utcnow()
        formatted_date = self.exported_datetime.strftime(date_format)
        self.archive_filename: str = shutil.make_archive(
            os.path.join(path, f"{user.username}_{formatted_date}"), "zip", path
        )
        if verbose:
            sys.stdout.write(f"\nExported archive to {self.archive_filename}.\n")
