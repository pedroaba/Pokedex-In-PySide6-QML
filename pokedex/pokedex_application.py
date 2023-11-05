from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication

from pokedex.settings import SCREEN_QML_FOLDER

app = QGuiApplication()

engine = QQmlApplicationEngine()
engine.load(
  SCREEN_QML_FOLDER / "pokedex.qml"
)

app.exec()
