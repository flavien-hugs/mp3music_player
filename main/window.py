# main.window.py

import os
import time
from pathlib import Path

import pygame
from tkinter import *
from tkinter import filedialog

from mutagen.mp3 import MP3
from main.helpers import about
from main.beatmaker import openBeatMaker


BASE_DIR = Path(__file__).resolve().parent.parent

path_song = BASE_DIR / "songs/"
path_image = BASE_DIR / "images/"

# Initialize pygame mixer
pygame.mixer.init()

main = Tk()
main.title('🎵 Sundance Music Player 🎵')

# -----------
# Init Window
# -----------

# obtenir la dimension de l'écran
wn_width, wn_height = 960, 540
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - wn_width/2)
center_y = int(screen_height/2 - wn_height/2)

# Define the position of the window in the center of the screen
main.geometry(f'{wn_width}x{wn_height}+{center_x}+{center_y}')
main.minsize(wn_width, wn_height)
main.maxsize(screen_height, screen_width)

# -----------------------------
# Init Menu and Command
# -----------------------------

menubar = Menu(
    main,
    background='#ccc',
    foreground='black',
    activebackground='white',
    activeforeground='black'
)
main.config(menu=menubar)

add_song_menu = Menu(menubar)
menubar.add_cascade(
    label="Fichier",
    menu=add_song_menu
)
add_song_menu.add_command(
    label="Ouvrir un fichier",
    command=lambda: addSong()
)

beatmaker_song_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(
    label="BeatMaker",
    menu=beatmaker_song_menu
)
beatmaker_song_menu.add_command(
    label="Open BeatMaker",
    command=lambda: openBeatMaker(main)
)

karaoke_song_menu = Menu(menubar)
menubar.add_cascade(
    label="Karaoke",
    menu=karaoke_song_menu
)
karaoke_song_menu.add_command(
    label="Sélectionner plusieurs fichier à ouvrir",
    command=lambda: addManySong()
)

delete_song_menu = Menu(menubar)
menubar.add_cascade(
    label="Suppression",
    menu=delete_song_menu
)
delete_song_menu.add_command(
    label="Supprimer cette musique de la liste",
    command=lambda: deleteSong()
)
delete_song_menu.add_command(
    label="Supprimer la liste",
    command=lambda: deleteAllSong()
)

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(
    label="About",
    command=lambda: about()
)

# -----------------------------
# Init Status bar
# -----------------------------

status_bar = Label(
    main, text="",
    bd=1, relief=GROOVE,
    anchor=E
)
status_bar.pack(
    fill=X, side=BOTTOM,
    ipadx=2
)

# -----------------------------
# Init playlist box
# -----------------------------

playlist_box = Listbox(
    main,
    height=8, width=80,
    bg="black", fg="green",
    selectbackground="green",
    selectforeground="black",
    font=("popins", 14),
).pack(padx=15, pady=20)

# --------------------
# Init Entry Text Song
# --------------------

text_box = Text(
    main,
    height=8, width=80,
).pack(padx=15, pady=20)

# -----------------------------
# Init player control buttons
# -----------------------------

"""
Create player control frame
"""
control_frame = Frame(main)
control_frame.pack(pady="10", side="bottom")

"""
play button
"""
play = BASE_DIR / 'images/play.png'
play_img = PhotoImage(file=play)
play_button = Button(
    control_frame,
    bg="white",
    height=60,
    width=70,
    image=play_img,
    justify="center",
    command=lambda: playSong()
)
play_button.grid(row=0, column=0, padx=10)

"""
previous button
"""
prev = BASE_DIR / 'images/prev.png'
prev_img = PhotoImage(file=prev)
prev_button = Button(
    control_frame,
    bg="white",
    height=60,
    width=70,
    image=prev_img,
    justify="center",
    command=lambda: prevSong()
)
prev_button.grid(row=0, column=1, padx=10)

"""
pause song button
"""
pause = BASE_DIR / 'images/pause.png'
pause_img = PhotoImage(file=pause)
pause_button = Button(
    control_frame,
    bg="white",
    height=60,
    width=70,
    image=pause_img,
    justify="center",
    command=lambda: pauseSong(paused)
)
pause_button.grid(row=0, column=2, padx=10)

"""
next button
"""
next = BASE_DIR / 'images/next.png'
next_img = PhotoImage(file=next)
next_button = Button(
    control_frame,
    bg="white",
    height=60,
    width=70,
    image=next_img,
    justify="center",
    command=lambda: nextSong()
)
next_button.grid(row=0, column=3, padx=10)

"""
stop button
"""
stop = BASE_DIR / 'images/stop.png'
stop_img = PhotoImage(file=stop)
stop_button = Button(
    control_frame,
    bg="white",
    height=60,
    width=70,
    image=stop_img,
    justify="center",
    command=lambda: stopSong()
)
stop_button.grid(row=0, column=4, padx=10)

"""
quit button
"""
exit = BASE_DIR / 'images/quit.png'
exit_img = PhotoImage(file=exit)
exit_button = Button(
    control_frame,
    height=60,
    width=70,
    borderwidth=0,
    image=exit_img,
    justify="center",
    command=lambda: main.destroy()
)
exit_button.grid(row=0, column=6, padx=10)

# ---------------------------------
# Init Command
# ---------------------------------

def addSong():
    """
    add song command
    """
    song = filedialog.askopenfilename(
        initialdir=path_song,
        title="Choisir une chanson",
        filetypes=(("mp3 Files", "*.mp3"),)
    )
    song = os.path.split(song)
    getsong = song[1]

    # add song to listbox
    if getsong.endswith(".mp3"):
        getsong = getsong.replace(".mp3", "")
        playlist_box.insert(END, getsong)

def addManySong():
    """
    add many song command
    """
    songs = filedialog.askopenfilenames(
        initialdir=path_song,
        title="Choisir une chanson",
        filetypes=(("mp3 Files", "*.mp3"),)
    )
    for song in songs:
        song = os.path.split(song)
        getsong = song[1]
        # add song to listbox
        if getsong.endswith(".mp3"):
            getsong = getsong.replace(".mp3", "")
            playlist_box.insert(END, getsong)

def playSong():
    """
    play song command
    """
    song = playlist_box.get(ACTIVE)
    song = f'{path_song}/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # call song time
    songTimeInfo()

def stopSong():
    """
    stop song command
    """
    pygame.mixer.music.stop()
    playlist_box.selection_clear(ACTIVE)

    # clear statusbar
    status_bar.config(text='')

def nextSong():
    """
    next song command
    """
    nextsong = playlist_box.curselection()
    nextsong = nextsong[0]+1

    song = playlist_box.get(nextsong)
    song = f'{path_song}/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    playlist_box.selection_clear(0, END)
    playlist_box.activate(nextsong)
    playlist_box.selection_set(nextsong, last=None)

def prevSong():
    """
    prev song command
    """
    nextsong = playlist_box.curselection()
    nextsong = nextsong[0]-1

    song = playlist_box.get(nextsong)
    song = f'{path_song}/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    playlist_box.selection_clear(0, END)
    playlist_box.activate(nextsong)
    playlist_box.selection_set(nextsong, last=None)

def deleteSong():
    playlist_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def deleteAllSong():
    playlist_box.delete(0, END)
    pygame.mixer.music.stop()

# Init control variable paused song
global paused
paused = False

def pauseSong(is_paused):
    """
    pause song command
    """
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def songTimeInfo():
    """
    Grab song lenght time info
    """
    current_time = pygame.mixer.music.get_pos()
    current_time = current_time / 1000

    converted_current_time = time.strftime(
        '%M:%S',
        time.gmtime(current_time)
    )

    song = playlist_box.get(ACTIVE)
    song = f'{path_song}/{song}.mp3'

    song_mut = MP3(song)
    song_length = song_mut.info.length

    converted_song_length = time.strftime(
        '%M:%S',
        time.gmtime(song_length)
    )

    song_timestamp = f"""
        {converted_current_time} of {converted_song_length}
    """
    status_bar.config(text=song_timestamp)
    status_bar.after(1000, songTimeInfo)
