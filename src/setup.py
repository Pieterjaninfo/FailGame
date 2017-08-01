import sys
from cx_Freeze import setup, Executable

target = Executable(
	script = 'game.py', 
	base = 'Win32GUI',
	icon = 'resources/bin.ico'
)

setup(
    name = 'RaceGame',
	version = '1.0',
	description = 'Best car dodge topdown view game ever!',
	author = 'Luke Dudeson',
    executables=[target]
)