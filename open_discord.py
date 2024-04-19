#!/usr/bin/env python3

import os

def open_flatpak_app(app_id):
    """Opens a Flatpak app using the flatpak command."""
    os.system(f"flatpak run {app_id}")

def open_discord():
    """Opens Discord specifically."""
    open_flatpak_app("com.discordapp.Discord")

if __name__ == "__main__":
    open_discord()
