from PyQt5 import QtWidgets
from contenedores import menu_principal

def main():
    app = QtWidgets.QApplication([])
    lanzador = menu_principal.Menu_principal()
    lanzador.show()
    app.exec()

main()