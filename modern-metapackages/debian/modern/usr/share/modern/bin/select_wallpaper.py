#!/usr/bin/python3

# Select a wallpaper based on the machine's hostname

from pathlib import Path
import random
import socket

random.seed(socket.getfqdn())
wallpapers = Path("/usr/share/modern/wallpaper")
print(random.choice([x for x in wallpapers.iterdir() if x.is_file()]))
