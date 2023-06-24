import vlc
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title("Video Player")
root.geometry("800x600")

video_frame = ttk.Frame(root)
video_frame.place(x=5, y=5, width=790, height=490)

media_player = vlc.MediaPlayer()
play_button = ttk.Button(root, text="PLAY", command=lambda: media_player.play())
play_button.place(x=5, y=500, width=100)
