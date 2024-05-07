import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def extract_audio():
    input_path = entry_path.get()
    if input_path:
        video = mp.VideoFileClip(input_path)
        output_path = input_path.replace(".mp4", "_audio.mp3")
        video.audio.write_audiofile(output_path)
        tk.messagebox.showinfo("Success", "Audio extracted successfully!")

root = tk.Tk()
root.title("Extract Audio from Video")

label = tk.Label(root, text="Select a video file (.mp4):")
label.pack(pady=5)

entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)

button_browse = tk.Button(root, text="Browse", command=select_file)
button_browse.pack(pady=5)

button_extract = tk.Button(root, text="Extract Audio", command=extract_audio)
button_extract.pack(pady=5)

root.mainloop()
