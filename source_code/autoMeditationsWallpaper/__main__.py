import ctypes
from pathlib import Path
from autoMeditationsWallpaper.textSlicer import find_lines

txt = ".\\meditations\\55317.txt"
def main():

    find_lines(txt)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(Path("sample-out.png").resolve()), 0)


if __name__ == '__main__':
    main()
