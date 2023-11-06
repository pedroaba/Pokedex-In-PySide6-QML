from pathlib import Path

ROOT_DIRECTOR = Path(".")
SCREEN_QML_FOLDER = ROOT_DIRECTOR / "screen"
ASSETS_FOLDER = ROOT_DIRECTOR / "assets"
TEMP_FOLDER = ROOT_DIRECTOR / "temp"

if not TEMP_FOLDER.exists():
    TEMP_FOLDER.mkdir(exist_ok=True)
