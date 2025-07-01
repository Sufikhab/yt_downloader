import os
import threading
import yt_dlp
import tkinter as tk
from tkinter import ttk, messagebox

DOWNLOAD_DIR = os.path.join(os.getcwd(), 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video():
    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning("Warning", "Please enter a YouTube video URL.")
        return

    status_label.config(text="📥 Downloading...", fg="yellow")
    progressbar.start()

    def do_download():
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                'noplaylist': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            status_label.config(text="✅ Download completed!", fg="lightgreen")
        except Exception as e:
            status_label.config(text=f"❌ Error: {e}", fg="red")
        finally:
            progressbar.stop()

    threading.Thread(target=do_download, daemon=True).start()

root = tk.Tk()
root.title("🚀 YouTube Video Downloader")
root.geometry("650x300")
root.configure(bg="#0f172a")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", foreground="#38bdf8", background="#0f172a", font=("Consolas", 14))
style.configure("TButton", font=("Consolas", 12), foreground="#ffffff", background="#0ea5e9")
style.configure("TEntry", font=("Consolas", 12), foreground="#00ff00", fieldbackground="#1e1e1e")
style.configure("TProgressbar", troughcolor="#1e1e1e", background="#14b8a6", thickness=20)

tk.Label(root, text="🔗 Enter YouTube Video URL", bg="#0f172a", fg="#38bdf8", font=("Orbitron", 16)).pack(pady=15)

url_entry = ttk.Entry(root, width=60)
url_entry.pack(pady=10)

download_btn = ttk.Button(root, text="📥 Download Video", command=download_video)
download_btn.pack(pady=10)

progressbar = ttk.Progressbar(root, mode='indeterminate', length=400)
progressbar.pack(pady=5)

status_label = tk.Label(root, text="", bg="#0f172a", fg="#ffffff", font=("Consolas", 12))
status_label.pack(pady=10)

tk.Label(root, text=f"💾 Saved to: {DOWNLOAD_DIR}", bg="#0f172a", fg="#94a3b8", font=("Consolas", 10)).pack(side=tk.BOTTOM, pady=10)

root.mainloop()
