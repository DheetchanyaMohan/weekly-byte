from pathlib import Path
import shutil
import argparse

# To run: 
# python organize.py ~/Downloads (or)
# python organize.py "C:\Users\YourName\Downloads"

# 1. Set up CLI parsing

parser = argparse.ArgumentParser(description="Organize files in a folder by extension.")
parser.add_argument("path", help="Path to the folder to organize")
args = parser.parse_args()


# 2. Get folder from command-line argument

folder = Path(args.path).expanduser().resolve()

if not folder.exists() or not folder.is_dir():
    print(f"Error: '{folder}' is not a valid folder.")
    exit(1)


# 3. Define extension mapping

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],
    "Spreadsheets": [".xlsx", ".csv"],
}


# 4. Organize files

for file in folder.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        moved = False

        for category, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                target_dir = folder / category
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(target_dir / file.name))
                moved = True
                break

        if not moved:
            other_dir = folder / "Others"
            other_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(other_dir / file.name))

print(f"✅ Organized files in: {folder}")
