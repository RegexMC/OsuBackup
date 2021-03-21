from json import dumps
from os import getcwd, listdir
from os.path import exists, join
from pathlib import Path
from re import sub


class Colors:
    OK = '\033[92m'
    WARN = '\033[93m'
    ERR = '\033[31m'
    BOLD = '\033[1m'
    FAIL = ERR + BOLD


# Reset color in console. end="" is there so there isnt an extra new line
def reset():
    print('\033[0m', end="")


user_directory = str(Path.home())  # C:/Users/.../
working_directory = getcwd()  # ./

osu_directory = None  # osu! directory | C:/Users/.../AppData/Local/osu!/
osu_songs_directory = None  # osu!/Songs/

ids = []  # List of beatmap IDs
output = {}  # Object to be written to the output file
output_path = "OsuBackup_output.json"  # Output file name

input_obj = {}
input_path = None

if __name__ == '__main__':
    osu_directory = join(user_directory, "AppData/Local/osu!/")

    while not exists(osu_directory):
        osu_directory = input(Colors.FAIL + "Directory not found! Enter custom osu directory here:\n")
    reset()

    osu_songs_directory = join(osu_directory, "Songs")
    while not exists(osu_songs_directory):
        osu_songs_directory = input(Colors.FAIL + "Songs directory not found! Enter custom osu songs directory here:\n")
    reset()

    mode = None
    while mode not in ["0", "1"]:
        mode = input(Colors.WARN + "Would you like to backup your osu beatmaps or restore them from a previous backup?"
                                   "(0:backup | 1:restore):\n")
    reset()

    proceed = None
    while proceed not in ["y", "n", "yes", "no"]:
        if mode:
            proceed = input(Colors.WARN + "You will be backing up your osu beatmaps. Continue (y/n)?\n")
        else:
            proceed = input(Colors.WARN + "You will be restoring your osu beatmaps. Continue (y/n)?\n")
    reset()

    if proceed in ["y", "yes"]:
        # Continue

        if mode:
            # Backup

            while exists(output_path) or not output_path:
                output_path = sub(r'\W+', '', input(
                    Colors.FAIL + "File " + output_path +
                    " already exists! Please enter a different output file:\n")).strip()
            reset()

            ids = []
            # Loop over each folder inside of the osu_songs directory, song_directory_name being each sub folders name
            for beatmap_folder in listdir(osu_songs_directory):
                beatmap_set_id = beatmap_folder.split(' ')[0]
                print(Colors.OK + "Found: " + beatmap_folder)
                ids.append(beatmap_set_id)
            reset()

            output.update({"beatmapsets": ids})
            print(output)

            # Create the output file and write the backup output to it
            f = open(output_path, "w")
            f.write(dumps(output))
            f.close()

            input("Backup Successful. Press enter to exit.")
    else:
        # Restore
        print("Restore")
        # TODO:
        #             #   - Get each beatmap user already has
        #             #   - If any IDS are in the backup, remove them from download queue
        #             #   - Let user define delay (min x seconds)
        #             #   - Give estimate on time based on download speed & amount of maps & delay
        #             #   - Loop over all IDS in the backups 'beatmapsets' array
        #             #   - Download .osz from = 'https://osu.ppy.sh/beatmapsets/ID/download'
        #             #   - Unzip the .osz file and move into songs folder
        #             #   - Delete .osz file
        #             #   - Wait however many seconds so as to not get rate limited
        #             # ----- I emailed osu support to see what delay if any I should set, and whether I could continue
        #             #       this project or not at all and I am waiting for a response ---
        input("Not made yet. Press enter to exit.")
else:
    exit()
