from json import dumps
from os import listdir, getcwd
from os.path import exists, isfile
from pathlib import Path
from re import sub

import bcolors

backup_output_file = getcwd() + "\\OsuBackup.json"

osu_path = str(Path.home()) + "\\AppData\\Local\\osu!\\"
osu_songs_path = osu_path + "Songs\\"

osu_songs = None

backup_output = {}
backup_output_ids = []


def check_custom_output_file():
    global backup_output_file

    while isfile(backup_output_file):
        backup_output_file = input(
            bcolors.FAIL + "File already exists! Enter different output file (default OsuBackup.json):\n")
        while not sub(r'\W+', '', backup_output_file).strip():
            backup_output_file = input(
                bcolors.FAIL + "File name invalid! Enter different output file (default OsuBackup.json):\n")


def check_custom_osu_directory():
    global osu_path
    global osu_songs_path
    while not exists(osu_path):
        osu_path = input(bcolors.FAIL + "Invalid directory! Enter different/custom directory here:\n")
        osu_songs_path = osu_path + "Songs\\"


def reset():
    print('\033[0m')


def check_osu_directory():
    global osu_path
    global osu_songs_path
    global osu_songs
    while not isfile(osu_path + "osu!.exe"):
        osu_path = input(bcolors.FAIL + "Invalid directory (osu.exe not found)! Enter different/custom osu here:\n")
        osu_songs_path = osu_path + "Songs\\"
        reset()

    while not exists(osu_songs_path):
        osu_path = input(
            bcolors.FAIL + "Invalid directory (Songs directory not found)! Enter different/custom osu here:\n")
        osu_songs_path = osu_path + "Songs\\"
        reset()

    # Prevent from needing to check again if songs directory is valid
    osu_songs = listdir(osu_songs_path)
    while len(osu_songs) == 0:
        osu_path = input(bcolors.FAIL + "Invalid directory (Songs directory empty)! Enter different/custom osu "
                                        "directory here:\n")
        osu_songs_path = osu_path + "Songs\\"
        reset()


if __name__ == '__main__':
    mode = None

    while not (mode == "0" or mode == "1"):
        mode = input(
            "Would you like to backup your osu beatmaps or "
            "restore them from a previous backup? (0:backup | 1:restore): \n")

    cont = ""

    while not (cont.lower() == "y" or cont.lower() == "n"):
        if mode == "0":
            cont = input(
                bcolors.WARN + "You will be " + bcolors.BOLD + "backing up " + bcolors.WARN + "your osu beatmaps. "
                                                                                              "Continue (y/n)?\n")
        else:
            cont = input(
                bcolors.WARN + "You will be " + bcolors.BOLD + "restoring " + bcolors.WARN + "your osu beatmaps. "
                                                                                             "Continue (y/n)?\n")
    if cont.lower() == "y":
        if mode == "0":
            if isfile(backup_output_file):
                check_custom_output_file()

            print(bcolors.OK + "Output file set to: " + backup_output_file)
            reset()

            # If the default osu directory does not exist
            if not exists(osu_path):
                check_custom_osu_directory()

            print(bcolors.OK + "osu! directory: " + osu_path)
            reset()

            # If the osu directory does not contain osu!.exe or if the songs directory does not exist or is empty.
            if not isfile(osu_path + "osu!.exe") or not exists(osu_songs_path) or len(listdir(osu_songs_path)) == 0:
                check_osu_directory()

            print(bcolors.OK + "osu! directory is valid")
            reset()

            # Directory was correct from start
            if osu_songs is None:
                osu_songs = listdir(osu_songs_path)

            for song_directory_name in osu_songs:
                beatmap_set_id = song_directory_name.split(' ')[0]

                print(bcolors.ITALIC + "Found: " + song_directory_name)
                backup_output_ids.append(beatmap_set_id)

            reset()
            backup_output.update({"beatmapsets": backup_output_ids})
            print(backup_output)
            f = open(backup_output_file, "w")
            f.write(dumps(backup_output))
            f.close()

            print(bcolors.OK + "Successfully backed up osu songs to " + backup_output_file)
            input(bcolors.WARN + "Press enter to close.")
        else:
            print("Restoring in progress")
            print(bcolors.OK + "Restoring not implemented yet.")
            input(bcolors.WARN + "Press enter to close.")
            # Restore
            # TODO:
            #   - Get each beatmap user already has
            #   - If any IDS are in the backup, remove them from download queue
            #   - Let user define delay (min x seconds)
            #   - Give estimate on time based on download speed & amount of maps & delay
            #   - Loop over all IDS in the backups 'beatmapsets' array
            #   - Download .osz from = 'https://osu.ppy.sh/beatmapsets/ID/download'
            #   - Unzip the .osz file and move into songs folder
            #   - Delete .osz file
            #   - Wait however many seconds so as to not get rate limited
            # ----- I emailed osu support to see what delay if any I should set, and whether I could continue
            #       this project or not at all and I am waiting for a response ---
            
    else:
        quit()
