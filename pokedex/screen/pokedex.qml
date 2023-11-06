import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow  {
    Material.theme: "Dark"

    visible: true

    width: 600
    height: 450

    font.pixelSize: 16

    title: "Pokedex"

    Row {
        id: row
        spacing: 24
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: parent.top
            topMargin: 20
        }

        TextField {
            id: pokemon_search
            placeholderText: "Digite um nome de pokemon ou id..."
            width: 250
            height: 40
        }

        Button {
            id: pokemon_submit
            text: "Search the Pokemon"
            width: 250
            height: 1.3 * pokemon_search.height

            y: -6

            background: Rectangle {
                radius: 4
                border.width: 1
                border.color: "#7c7c7e"
                color: mouse.hovered ? "#7c7c7e" : "#575758"
            }

            HoverHandler {
                id: mouse
                acceptedDevices: PointerDevice.Mouse
                cursorShape: Qt.PointingHandCursor
            }

            onClicked: {
                pokemon_search.text = "Procurando pokemon..."
                image.source = "../assets/loading_without_bg.gif"

                const pokemonResult = searchBridge.fetch_pokemon(pokemon_search.text);

                pokemon_search.text = "";
                pokemon_label.text = "";

                pokemon_label.text = pokemonResult[1];
                image.source = pokemonResult[0];
            }
        }
    }

    Label {
        id: pokemon_label
        text: "Pokemon !"

        anchors {
            horizontalCenter: parent.horizontalCenter
            top: row.top
            topMargin: 60
        }
    }

    Image {
        id: image
        cache: false
        width: 300
        height: 300

        anchors {
            horizontalCenter: parent.horizontalCenter
            top: row.top
            topMargin: 90
        }
    }
}
