from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

def seleciona_mensagem(tipo, nome, num_ip):
    if tipo == "Vítima":
        return f"""Olá, Sr(a) {nome}! 
Comunica-se, para fins de cumprimento do art. 28, § 1º, do Código de Processo Penal, que o inquérito policial nº {num_ip}, em que V. Sa. figurou como VÍTIMA (ou representante da vítima), foi arquivado. 
Cópia da referida decisão poderá ser solicitada pelo e-mail aldemirsilva@mpsp.mp.br,com comprovação de identidade, ou pessoalmente, na sede da Promotoria de Justiça, *rua Almirante Barroso nº 491, Piracicaba/SP*, na 2a., 4a. ou 5a. feiras, das 13h às 17h. 
No prazo de *30 dias*, V. Sa. poderá solicitar a revisão do arquivamento, por pedido escrito, pelo e-mail já informado ou pessoalmente.
Informa-se, por fim, que não respondemos mensagens por este canal de comunicação. 
Atenciosamente, 
11a. Promotoria de Justiça de Piracicaba"""
    else:
        return f"""Olá, Sr(a) {nome}!
Comunica-se, para fins de cumprimento do art. 28 do Código de Processo Penal, que o inquérito policial nº {num_ip}, em que V. Sa. figurou como INDICIADO(A) foi arquivado.
Cópia da referida decisão poderá ser solicitada pelo e-mail aldemirsilva@mpsp.mp.br, com comprovação de identidade, ou pessoalmente, na sede da Promotoria de Justiça, *rua Almirante Barroso nº 491, Piracicaba/SP*, na 2a., 4a. ou 5a. feiras, das 13h às 17h.
Informa-se, por fim, que não respondemos mensagens por este canal de comunicação.
Atenciosamente,
11a. Promotoria de Justiça de Piracicaba"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 90, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 130, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 170, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 221, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 130, 31, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 60, 251, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.pushButton)

        # Definir o foco inicial no lineEdit_3
        self.lineEdit_3.setFocus()

        # Conectar botão ao método capturar_valores
        self.pushButton.clicked.connect(self.capturar_valores)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PJ Piracicaba"))
        self.label.setText(_translate("MainWindow", "Nome"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Vítima"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Indiciado(a)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Vítima"))
        self.label_2.setText(_translate("MainWindow", "Celular"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
        self.label_3.setText(_translate("MainWindow", "Zap Notificator"))
        self.label_4.setText(_translate("MainWindow", "+55"))
        self.label_5.setText(_translate("MainWindow", "IP nº"))

    def capturar_valores(self):
        nome = self.lineEdit.text()
        ip = self.lineEdit_3.text()
        celular = self.lineEdit_2.text()
        tipo = self.comboBox.currentText()
        texto = seleciona_mensagem(tipo, nome, ip)

        url = f"https://api.whatsapp.com/send?phone=55{celular}&text={texto}"
        webbrowser.open(url)
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())