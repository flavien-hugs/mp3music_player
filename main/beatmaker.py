# beatmaker button

import os
from pathlib import Path

import pygame
from tkinter import *

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize pygame mixer
pygame.mixer.init()
path_song_beat = BASE_DIR / "songs/beats/"

# --------------------
# Define button list
# --------------------

def fisrtSong():
    song = f'{path_song_beat}/beat.1.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def firstSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='blue2',
        width=20,
        command=lambda: fisrtSong()
    ).grid(row=1, column=1)

# --------------------------------------

def secondSong():
    song = f'{path_song_beat}/beat.2.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def secondSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='green2',
        width=20,
        command=lambda: secondSong()
    ).grid(row=1, column=2)

# --------------------------------------

def threeSong():
    song = f'{path_song_beat}/beat.3.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def threeSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='red2',
        width=20,
        command=lambda: threeSong()
    ).grid(row=1, column=3)

# --------------------------------------

def fourSong():
    song = f'{path_song_beat}/beat.4.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def fourSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='yellow2',
        width=20,
        command=lambda: fourSong()
    ).grid(row=2, column=1)

# --------------------------------------

def fiveSong():
    song = f'{path_song_beat}/beat.5.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def fiveSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='gray2',
        width=20,
        command=lambda: fiveSong()
    ).grid(row=2, column=2)

# --------------------------------------

def sixSong():
    song = f'{path_song_beat}/beat.6.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def sixSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='purple2',
        width=20,
        command=lambda: sixSong()
    ).grid(row=2, column=3)

# --------------------------------------

def sevenSong():
    song = f'{path_song_beat}/beat.1.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def sevenSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='blue2',
        width=20,
        command=lambda: sevenSong()
    ).grid(row=3, column=1)

# --------------------------------------

def eightSong():
    song = f'{path_song_beat}/beat.3.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def eightSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='green2',
        width=20,
        command=lambda: eightSong()
    ).grid(row=3, column=2)

# --------------------------------------

def nineSong():
    song = f'{path_song_beat}/beat.2.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def nineSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='red2',
        width=20,
        command=lambda: nineSong()
    ).grid(row=3, column=3)

# --------------------------------------

def tenSong():
    song = f'{path_song_beat}/beat.4.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def tenSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='yellow2',
        width=20,
        command=lambda: tenSong()
    ).grid(row=4, column=1)

# --------------------------------------

def elevenSong():
    song = f'{path_song_beat}/beat.4.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def elevenSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='gray2',
        width=20,
        command=lambda: elevenSong()
    ).grid(row=4, column=2)

# --------------------------------------

def twelveSong():
    song = f'{path_song_beat}/beat.4.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def twelveSongButton(control_frame):
    btn = Button(
        control_frame,
        bg='purple2',
        width=20,
        command=lambda: twelveSong()
    ).grid(row=4, column=3)

# --------------------------------------

def openBeatMaker(main):
    win = Toplevel(main)
    win.title("BeatMaker")
    win.geometry("650x150")
    win.resizable(False, False)

    control_frame = Frame(win)
    control_frame.pack(pady=10, padx=10)

    firstSongButton(control_frame)
    secondSongButton(control_frame)
    threeSongButton(control_frame)
    fourSongButton(control_frame)
    fiveSongButton(control_frame)
    sixSongButton(control_frame)
    sevenSongButton(control_frame)
    eightSongButton(control_frame)
    nineSongButton(control_frame)
    tenSongButton(control_frame)
    elevenSongButton(control_frame)
    twelveSongButton(control_frame)
