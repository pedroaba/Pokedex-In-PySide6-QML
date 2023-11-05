import QtQuick
import QtQuick.Controls

ApplicationWindow  {
    visible: true
    width: 500
    height: 400
    font.pixelSize: 40
    title: "Pokedex"

    Button {
        text: 'Botão !'
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        width: 300
        height: 40
    }
}
