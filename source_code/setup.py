import sys

from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["autoMeditationsWallpaper"], "excludes": ["asyncio", "email", "html", "http",
                                                                            "lib2to3", "multiprocessing", "pydoc_data",
                                                                            "test", "tkinter", "unittest", "xmlrpc"]}

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "program",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]stoic_wallpaper_generator.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     "icon.ico",  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    ("StartupShortcut",  # Shortcut
     "StartupFolder",  # Directory_
     "program",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]stoic_wallpaper_generator.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     "logo.ico",  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),
]
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable("stoic_wallpaper_generator.py", icon="logo.ico", shortcutName='stoic_wallpaper_generator',
                          shortcutDir='DesktopFolder', base=base)]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}

setup(
    name="stoic_wallpaper_generator",
    version="1.0",
    description='Generates and sets wallpaper with excerpts from Marcus Aurelius "meditations"',
    author='Mir Hannes Wartel',
    executables=executables,
    options={"build_exe": build_exe_options, "bdist_msi": bdist_msi_options
             },
)
