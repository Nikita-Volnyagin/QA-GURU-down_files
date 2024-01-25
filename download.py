import os
import requests
from script_os import TMP_DIR


def test_download_pdf_file():
    content = requests.get(
        url='https://media.readthedocs.org/pdf/pytest/latest/pytest.pdf'
    ).content
    with open(os.path.join(TMP_DIR, "file_pdf.pdf"), 'wb') as file:
        file.write(content)


def test_download_csv_file():
    content = requests.get(
        url='https://cdn.wsform.com/wp-content/uploads/2020/06/color_srgb.csv'
    ).content
    with open(os.path.join(TMP_DIR, "file_csv.csv"), 'wb') as file:
        file.write(content)


def test_download_xlsx_file():
    content = requests.get(
        url='https://itsm365.com/documents_rus/web/Content/Resources/doc'
        '/import_ou_xlsx.xlsx'
    ).content
    with open(os.path.join(TMP_DIR, "file_xlsx.xlsx"), 'wb') as file:
        file.write(content)