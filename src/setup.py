import sys
from cx_Freeze import *

setup(
    name = 'game',
	version = '3.1',
	description = 'Best car dodge topdown view game ever!',
    executables=[Executable('game.py', base = 'Win32GUI')]
)