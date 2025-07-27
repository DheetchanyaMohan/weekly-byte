# 📅 Week 2 of 52 — 🗂️ File Organizer CLI Tool

This project is part of **my 52-week coding challenge**, where I’m building **one small project each weekend** to consistently refresh my skills, stay in touch with core development tools, and gradually grow in different domains — from scripting and system tools to machine learning and full-stack apps.

For Week 2, I decided to build a simple but useful automation script: a **file organizer**. It’s something I've often needed when my Downloads folder gets messy, and this weekend’s project gave me an opportunity to get more hands-on with Python's `pathlib`, `os`, `shutil`, and `argparse` modules — all key tools in the Python standard library.

---

# 🗂️ File Organizer CLI Tool

A lightweight Python script that organizes files in any directory by sorting them into subfolders based on file extension. Designed to be run from the terminal using a folder path argument. Great for keeping folders like `Downloads`, `Desktop`, or project directories tidy with minimal effort.

---

## 🚀 Features

- 🔎 Scans any folder passed via command-line argument
- 🗃️ Categorizes files into common types like Images, Documents, Archives, Scripts, etc.
- 📁 Automatically creates destination folders (if they don’t exist)
- ♻️ Moves files into their appropriate folders using `shutil`
- 🧼 Leaves your folder clean and neatly structured

---

## 📂 Project Structure

```
file-organizer/
├── organize.py # Main Python script
├── README.md # You're reading it!
└── test_folder/ # Sample folder for local testing
```

---

## 🧠 Concepts Practiced

- Using `argparse` to build a real CLI interface
- Working with `pathlib.Path` to handle file paths cleanly
- Moving files using `shutil.move()`
- Organizing logic using extension → category mapping
- Handling edge cases like unknown file types

---

## 🛠️ How to Use Locally

1. **Clone the repo:**

```
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
```

2. **Run the script with a target folder path:**

```bash
python organize.py "D:\Users\YourName\Downloads"
# or for macOS/Linux:
python organize.py ~/Downloads
```

3. **Your folder will be reorganized like this:**

```
Downloads/
├── Images/
├── Documents/
├── Music/
├── Archives/
├── Scripts/
├── Others/
```

## 🗂️ File Type Categories

| Category         | Extensions                                     |
|-----------------|-------------------------------------------------|
| 🖼️ Images       | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`        |
| 📽️ Videos       | `.mp4`, `.mkv`, `.mov`, `.avi`                 |
| 📄 Documents    | `.pdf`, `.docx`, `.txt`, `.pptx`, `.doc`       |
| 🎵 Music        | `.mp3`, `.wav`, `.aac`                         |
| 📦 Archives     | `.zip`, `.tar`, `.gz`, `.rar`, `.7z`           |
| 🧾 Spreadsheets | `.xlsx`, `.csv`                                |
| 💻 Scripts      | `.py`, `.js`, `.html`, `.css`, `.sh`, `.bat`   |
| ❓ Others       | Anything not covered by the above categories   |

## 🔧 Planned Improvements

- `--dry-run` option to preview without moving files
- Verbose logging for moved files
- Allow user-defined mapping via `config.json`
- Undo last organization run via log tracking

## 📜 License
MIT License — free to modify and distribute

