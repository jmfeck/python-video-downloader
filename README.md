# Python Video Downloader

This repository contains a Python script designed to easily download videos from various online sources by reading video URLs and parameters directly from an Excel file.

---

## 📁 Project Structure

```
python-video-downloader
├── input
│   └── video_links.xlsx
├── output
│   └── (downloaded files will appear here)
├── logs
│   └── (log files are generated here)
├── scripts
│   └── python_video_downloader.py
└── run_python_video_downloader.bat
```

---

## 🚀 Features

- **Batch video downloading** from multiple URLs
- Supports multiple video formats (e.g., mp4, mp3)
- Customizable video quality (best available by default)
- Option to download audio-only content
- Automatic file naming (uses video titles by default, customizable)
- Comprehensive logging of all operations and errors

---

## 🛠 Requirements

- Python 3.7+
- `yt-dlp`
- `pandas`
- `openpyxl`
- `ffmpeg` (required for audio extraction and video processing)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/jmfeck/python-video-downloader.git
```

2. Navigate into the cloned repository and install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install FFmpeg:

- **Windows:**
```bash
winget install ffmpeg
```

- **macOS:**
```bash
brew install ffmpeg
```

- **Linux (Debian/Ubuntu):**
```bash
sudo apt install ffmpeg
```

---

## 📗 Excel Input Format

Your Excel file (`video_links.xlsx`) located in the `input` folder must have a tab named exactly the same as the file name ("video_links"). It should follow this structure:

| Link (Required) | File Extension (Optional) | Quality (Optional)          | Audio Only (Optional) | Filename (Optional) |
|-----------------|---------------------------|-----------------------------|-----------------------|---------------------|
| URL             | mp4, mp3, wav, etc.       | best, 1080p, 720p, 480p, etc.| TRUE/FALSE           | custom filename     |

### Column details:

- **Link:** URL of the video to download (mandatory).
- **File Extension:** Desired file extension. Supported examples: `mp4`, `mp3`, `wav`. Defaults to `mp4`.
- **Quality:** Desired video quality/resolution. Examples include `best`, `bestvideo+bestaudio`, `1080p`, `720p`. Defaults to `bestvideo+bestaudio/best`.
- **Audio Only:** Set to `TRUE` if you only want audio without video. Defaults to `FALSE`.
- **Filename:** Custom file name without extension. Defaults to the original video title.

---

## ▶️ Usage

### Option 1: Using the batch file (Windows)

Run the provided batch file from the project's root directory:

```bash
run_python_video_downloader.bat
```

### Option 2: Direct Python execution

Alternatively, run the downloader script directly:

```bash
python scripts/python_video_downloader.py
```

The script will process all video links listed in the Excel file and store downloaded files in the `output` folder.

---

## 📌 Notes

- Make sure Excel files and sheet names match exactly.
- Ensure `ffmpeg` is installed for full functionality.
- Logs will be created with timestamps to assist in tracking operations and debugging.

---

## ✏️ Author

- **João Manoel Feck**
- Email: [joaomfeck@gmail.com](mailto:joaomfeck@gmail.com)
- GitHub: [github.com/jmfeck](https://github.com/jmfeck)

