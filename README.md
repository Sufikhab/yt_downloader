# 🎬 YT_DOWNLOADER

**Empower Your Media, Download Faster, Play Anywhere**

![last-commit](https://img.shields.io/github/last-commit/Sufikhab/yt_downloader)
![repo-top-language](https://img.shields.io/github/languages/top/Sufikhab/yt_downloader)
![repo-language-count](https://img.shields.io/github/languages/count/Sufikhab/yt_downloader)

---

## 🛠️ Built with the tools and technologies:

- Markdown  
- Python  
- Tkinter  
- yt_dlp  

---

## 📚 Table of Contents

- [Overview](#overview)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
- [Usage](#usage)  
- [Testing](#testing)  

---

## 🔍 Overview

**yt_downloader** is an intuitive graphical tool designed to simplify YouTube video downloads for developers and end-users alike.  
It leverages `yt_dlp` to handle media retrieval efficiently, providing a seamless experience from URL input to download completion.

---

### 🚀 Why yt_downloader?

This project streamlines media access by offering a robust, user-friendly interface for downloading YouTube videos.  
Its core features include:

- 🖥️ **Graphical User Interface** – Enables easy input of video URLs and manages downloads visually.  
- 🚀 **Background Downloading** – Executes downloads asynchronously, ensuring a smooth user experience.  
- 📊 **Progress Visualization** – Offers real-time status updates and visual progress indicators.  
- 🔧 **yt_dlp Integration** – Utilizes a powerful media extraction library for reliable downloads.  
- 🔄 **Modular Architecture** – Serves as a core component within larger media management systems.  

---

## 🧰 Getting Started

### ✅ Prerequisites

This project requires the following dependencies:

- Programming Language: **Python 3.7+**
- Package Manager: **Conda (or pip)**

---

### 📦 Installation

Build `yt_downloader` from the source and install dependencies:

#### 1. Clone the repository:

```bash
git clone https://github.com/Sufikhab/yt_downloader
```

#### 2. Navigate to the project directory:

```bash
cd yt_downloader
```

#### 3. Install the dependencies:

Using **conda**:

```bash
conda env create -f conda.yml
```

Or using **pip**:

```bash
pip install yt-dlp
```

---

## ▶️ Usage

Run the project with:

Using **conda**:

```bash
conda activate yt_downloader
python app.py
```

Or using **pip/venv**:

```bash
python app.py
```

Once launched:

1. Paste a YouTube video URL into the entry box.  
2. Click the **📥 Download Video** button.  
3. Watch the progress bar.  
4. Your video will be saved into the `downloads/` folder.

---

## 🧪 Testing

`yt_downloader` uses the `pytest` test framework. Run the test suite with:

Using **conda**:

```bash
conda activate yt_downloader
pytest
```

---

⬆ [Return to top](#yt_downloader)
