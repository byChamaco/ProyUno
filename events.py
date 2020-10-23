import var,sys,clients

class Eventos():

    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print('Error: %s ' % str(error))

    def validarDNI(self):
        try:
            dni = var.ui.editDni.text()
            if clients.Clients.validarDNI(dni):
                var.ui.lblValido.setStyleSheet('QLabel {color: green;}')
                var.ui.lblValido.setText('V')
                var.ui.editDni.setText(dni.upper())
            else:
                var.ui.lblValido.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValido.setText('X')
                var.ui.editDni.setText(dni.upper())
        except Exception as error:
            print('Error: %s ' % str(error))