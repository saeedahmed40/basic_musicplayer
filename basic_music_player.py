#importing libraries 
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")
        master.geometry("600x400")
        master.config(bg="black")
        master.resizable(True, True)

        mixer.init()
        self.current_file = None
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        self.play_button = Button(self.master, text="Play", command=self.play_button_clicked, bg="green", fg="white", font=font.Font(size=12))
        self.play_button.pack(pady=10)
        self.pause_button = Button(self.master, text="Pause", command=self.pause_button_clicked, bg="blue", fg="white", font=font.Font(size=12))
        self.pause_button.pack(pady=10)
        self.stop_button = Button(self.master, text="Stop", command=self.stop_button_clicked, bg="red", fg="white", font=font.Font(size=12))
        self.stop_button.pack(pady=10)
        self.load_button = Button(self.master, text="Load", command=self.load_button_clicked, bg="yellow", fg="black", font=font.Font(size=12))
        self.load_button.pack(pady=10)
        self.status_label = Label(self.master, text="Status: Not Playing", bg="black", fg="white", font=font.Font(size=12))
        self.status_label.pack(pady=10)

    def play_button_clicked(self):
        if self.current_file:
            if self.paused:
                mixer.music.unpause()
                self.paused = False
                self.status_label.config(text="Status: Playing")
            else:
                mixer.music.load(self.current_file)
                mixer.music.play()
                self.status_label.config(text="Status: Playing")
        else:
            self.status_label.config(text="Status: No file loaded")

    def pause_button_clicked(self):
        if mixer.music.get_busy():
            if not self.paused:
                mixer.music.pause()
                self.paused = True
                self.status_label.config(text="Status: Paused")
            else:
                self.play_button_clicked()
        else:
            self.status_label.config(text="Status: Not Playing")

    def stop_button_clicked(self):
        if mixer.music.get_busy():
            mixer.music.stop()
            self.paused = False
            self.status_label.config(text="Status: Stopped")
        else:
            self.status_label.config(text="Status: Not Playing")

    def load_button_clicked(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
        if file_path:
            self.current_file = file_path
            self.status_label.config(text=f"Status: Loaded {os.path.basename(file_path)}")
        else:
            self.status_label.config(text="Status: No file selected")
def main():
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
if __name__ == "__main__":
    main()