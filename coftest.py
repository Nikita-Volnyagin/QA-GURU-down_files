import shutil
import zipfile
import pytest
import os
from script_os import TMP_DIR, RESOURCES_DIR, ARCHIVE_DIR, FILES_LIST


@pytest.fixture
def create_archive():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)
    with zipfile.ZipFile(ARCHIVE_DIR, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in FILES_LIST:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree(RESOURCES_DIR)