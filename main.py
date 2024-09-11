"""
   ___             _         __     ___            __
  / _ \_______    (_)__ ____/ /_   / _ \___ ____  / /____  ____
 / ___/ __/ _ \  / / -_) __/ __/  / , _/ _ `/ _ \/ __/ _ \/ __/
/_/  /_/  \___/_/ /\__/\__/\__/  /_/|_|\_,_/ .__/\__/\___/_/
             |___/                        /_/
First created: 9/6/24
"""

## Imports
import sys
import os
import platform
import hashlib
# CRYPTOGRAPHY NEEDED
from getpass import getpass

# work on importing base16 color schemes

OS = os.name
Platform = sys.platform
PlatformRelease = platform.release
print(OS, Platform, PlatformRelease)
# - Login screen -
print(" _      __    __                     __     ")
print("| | /| / /__ / /______  __ _  ___   / /____ ")
print("| |/ |/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \ ")
print("|__/|__/\__/_/\__/\___/_/_/_/\__/  \__/\___/")
print("__________                __")
print("\______   \_____  _______/  |_  ___________")
print(" |       _/\__  \ \____ \   __\/  _ \_  __ \ ")
print(" |    |   \ / __ \|  |_> >  | (  <_> )  | \/")
print(" |____|_  /(____  /   __/|__|  \____/|__|")
print("        \/      \/|__|")

""" 
 - Goals -
 1. Alternative for Youtube, Facebook, Twitter, Reddit, snapchat, etc
 2. Zones for everyone, I.e. drawing/art zone, code zone, Linux zone, etc
 3. Safe platform for all ages (Except kids under 13, they don't need
 to be on social media.)
 4. 90% OR more in Python (Not counting databases and the front-end)
 5. Respect user privacy
 6. Be under the GPL 3.0 license or MIT.
 7. No AI in creative works zones.
"""

## - USERNAME -
UserName = input("Username: ")
# Username is stored with the hashed password in a (USERNAMEhere).txt file,
# then encrypted with AES-256

## - PASSWORD -
Password = getpass("Password: ")

# Password hashing
def hash_password(password):
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()


hashed_password = hash_password(Password)
print("Hashed password:", hashed_password)
# Password gets hashed locally, then sent to a database

# WIP encryption
# EncryptionKey = Fernet.generate_key()
# cipher_suite = Fernet(EncryptionKey)
# encoded_text = cipher_suite.encrypt(p[password])

## Databse hookups and send-outs
# set up database (Maria, Mongo, Redis, Access, etc)

## - FYP -


## Search bar & searching stuff

## - Settings -

# Content filtering options
# 1. Coding include/exclude
# 2. Age based content
# 3. Specific topic include/exclude
# 4. Curse word blurring/muting

#  - Theming -
# Base16 themes
# Light and dark mode

# - advertising settings -
# 1. Ad include/exclude
# 2. Ad time limit
# 3. Ad topic filtering
