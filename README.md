# OsuBackup
### Currently, this project only supports saving all beatmap IDs, and not restoring them automatically.

---

Got a response from osu support and unfortunately this app will **not** be able to restore beatmaps automatically, and will not be implemented. If you have any ideas on how to potentially remedy this I'm open for suggestions. Currently in mind I have something that simply watches a folder for .osz files and then extracts them to the osu folder, accompanied by a tool that reads a backup file and opens a tab for each ID every 5-10s (so that it is technically not mass downloading in the same sense? idk).

---

**OsuBackup is a project developed by [@RegexMC](https://twitter.com/regexmc) to backup and restore your osu beatmaps.**

It is intended to be used when resetting your device or when switching devices _permanently_. It is not intended to maintain beatmaps between devices and be used frequently.

## Usage
Download the latest release from the [releases page](https://github.com/RegexMC/OsuBackup/releases)

Ensure [Python](https://www.python.org/downloads/) is installed. However, if using the portable executable you can skip this step.

Open the program _(main.py, main.exe)_.

Follow the steps the program walks you through. The output file name must be valid, and the osu folder must exist and be valid. If you encounter any issues with this please [create an issue](https://github.com/RegexMC/OsuBackup/issues).