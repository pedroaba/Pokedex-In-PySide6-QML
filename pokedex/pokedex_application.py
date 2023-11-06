import ctypes

from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication, QIcon

from pokedex.settings import SCREEN_QML_FOLDER, ASSETS_FOLDER
from pokedex.bridge import SearchPokemonBridge


app_id = "pedroaba.pokedex"  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

app = QGuiApplication()

app.setWindowIcon(
  QIcon(
    str(ASSETS_FOLDER / "icon.png")
  )
)

search_bridge = SearchPokemonBridge()

engine = QQmlApplicationEngine()
engine.load(
  SCREEN_QML_FOLDER / "pokedex.qml"
)

engineContext = engine.rootContext()
engineContext.setContextProperty("searchBridge", search_bridge)

app.exec()
