from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("python\\course\\7").rglob("*.*"):
#         zip.write(path)

with ZipFile("python\\course\\7\\files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("python/course/7/paths.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("python/course/7/extract")
