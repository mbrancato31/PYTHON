from pathlib import Path

# absolute path
# c:\program files\microsoft
# relative path

path = Path()
for file in path.glob('*'):
    print(file)