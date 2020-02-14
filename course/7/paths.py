from pathlib import Path
from time import ctime
import shutil

# Path(r"C:\program files\...")
# Path()

# Path.home()
#
source = Path("python\\course\\7\\ecommerce\\__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target)
# target.write_text(source.read_text())


# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.txt")
# print(path)
# print(path.absolute)
# path = path.with_suffix(".txt")
# print(path)

# for p in path.iterdir():
#     print(p)

# paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.rglob("*.py")]
# print(py_files)


# print(ctime(path.stat().st_ctime))

# print(path.read_text)
# path.write_text(".....")
# path.write_bytes()
