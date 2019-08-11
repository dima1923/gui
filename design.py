from PyQt5 import QtWidgets,QtGui,QtCore, QtSql
import user

class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900,900)
        self.main_win = QtWidgets.QWidget()
        self.admin = QtWidgets.QWidget()
        self.view = QtWidgets.QWidget()
        self.add = QtWidgets.QWidget()
        self.initUI_1()
        self.initUI_2()
        self.initUI_3()
        self.initUI_4()
        self.stack = QtWidgets.QStackedLayout(self)
        self.stack.addWidget(self.main_win)
        self.stack.addWidget(self.admin)
        self.stack.addWidget(self.view)
        self.stack.addWidget(self.add)
        self.button.clicked.connect(self.open_admin)
        self.pushButton.clicked.connect(self.open_add)
        self.pushButton_2.clicked.connect(self.open_view)
        self.pushButton_3.clicked.connect(self.add_row)
        self.stack.setCurrentIndex(0)


    def initUI_1(self):
        self.main_win.resize(824, 534)
        #self.stack = QtWidgets.QStackedLayout(self)
        self.label1=QtWidgets.QLabel("Login",self.main_win)
        self.login = QtWidgets.QLineEdit(self.main_win)
        self.login.setGeometry(QtCore.QRect(300, 140, 331, 71))
        self.login.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("([A-Za-z0-9]+)@([A-Za-z]+).([A-Za-z]{2})")))
        self.label1.setGeometry(QtCore.QRect(250,145,60,20))
        self.label2=QtWidgets.QLabel("Password",self.main_win)
        self.label2.setGeometry(QtCore.QRect(230,245,60,20))
        self.password = QtWidgets.QLineEdit(self.main_win)
        self.password.setGeometry(QtCore.QRect(300, 240, 331, 71))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9]+")))
        self.button = QtWidgets.QPushButton(self.main_win)
        self.button.setGeometry((QtCore.QRect(300,340,331,71)))
        self.button.setText("OK")


    def initUI_2(self):
        self.admin.resize(824,534)
        self.pushButton = QtWidgets.QPushButton(self.admin)
        self.pushButton.setGeometry(QtCore.QRect(170, 90, 271, 71))
        self.pushButton.setText("Add row")
        self.pushButton_2 = QtWidgets.QPushButton(self.admin)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 190, 271, 71))
        self.pushButton_2.setText("View table")

    def initUI_3(self):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("/home/dmitry/Desktop/my")
        con.open()
        view = QtWidgets.QTableView(self.view)
        model = QtSql.QSqlTableModel(self.view, db=con)
        model.setTable("BitcoinJPY")
        model.select()
        view.setModel(model)
        view.setGeometry(0, 0, 900, 900)
        view.show()
        con.close()

    def initUI_4(self):
        self.add.resize(824,534)
        self.labelTS=QtWidgets.QLabel("Timestamp",self.add)
        self.labelTS.setGeometry(QtCore.QRect(0,0,100,40))
        self.timestamp = QtWidgets.QLineEdit(self.add)
        self.timestamp.setValidator(QtGui.QIntValidator())
        self.timestamp.setGeometry(QtCore.QRect(100,0,200,40))
        self.labelO=QtWidgets.QLabel("Open",self.add)
        self.labelO.setGeometry(QtCore.QRect(0,45,100,40))
        self.oopen=QtWidgets.QLineEdit(self.add)
        self.oopen.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+.[0-9]+')))
        self.oopen.setGeometry(QtCore.QRect(100, 45, 200, 40))
        self.labelH=QtWidgets.QLabel("High",self.add)
        self.labelH.setGeometry(QtCore.QRect(0, 90, 100, 40))
        self.high=QtWidgets.QLineEdit(self.add)
        self.high.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+.[0-9]+')))
        self.high.setGeometry(QtCore.QRect(100, 90, 200, 40))
        self.labelL = QtWidgets.QLabel("Low", self.add)
        self.labelL.setGeometry(QtCore.QRect(0, 135, 100, 40))
        self.low = QtWidgets.QLineEdit(self.add)
        self.low.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+.[0-9]+')))
        self.low.setGeometry(QtCore.QRect(100, 135, 200, 40))
        self.labelC = QtWidgets.QLabel("Close", self.add)
        self.labelC.setGeometry(QtCore.QRect(0, 180, 100, 40))
        self.Close = QtWidgets.QLineEdit(self.add)
        self.Close.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+.[0-9]+')))
        self.Close.setGeometry(QtCore.QRect(100, 180, 200, 40))
        self.labelVBTC = QtWidgets.QLabel("VolumeBTC", self.add)
        self.labelVBTC.setGeometry(QtCore.QRect(0, 225, 100, 40))
        self.VBTC = QtWidgets.QLineEdit(self.add)
        self.VBTC.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+.[0-9]+')))
        self.VBTC.setGeometry(QtCore.QRect(100, 225, 200, 40))
        self.labelVC = QtWidgets.QLabel("VolumeCurrency", self.add)
        self.labelVC.setGeometry(QtCore.QRect(0, 270, 100, 40))
        self.VC = QtWidgets.QLineEdit(self.add)
        self.VC.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+.[0-9]+')))
        self.VC.setGeometry(QtCore.QRect(100, 270, 200, 40))
        self.labelWP = QtWidgets.QLabel("Weighted Price", self.add)
        self.labelWP.setGeometry(QtCore.QRect(0, 315, 100, 40))
        self.WP = QtWidgets.QLineEdit(self.add)
        self.WP.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+.[0-9]+')))
        self.WP.setGeometry(QtCore.QRect(100, 315, 200, 40))
        self.pushButton_3=QtWidgets.QPushButton(self.add)
        self.pushButton_3.setText('OK')
        self.pushButton_3.setGeometry(QtCore.QRect(40,350,30,30))

    def open_admin(self):
        po = user.user(str(self.login.text()), str(self.password.text())).admin_or_user()
        if(po=="USER"):
            self.stack.setCurrentIndex(2)
        elif(po=="ADMIN"):
            self.stack.setCurrentIndex(1)
        else:
            self.close()

    def open_view(self):
        self.stack.setCurrentIndex(2)

    def open_add(self):
        self.stack.setCurrentIndex(3)

    def add_row(self):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("/home/dmitry/Desktop/my")
        con.open()
        query = "INSERT INTO BitcoinJPY (Timestamp,Open, High, Low, Close, 'Volume(BTC)', 'Volume(Currency)', Weighted_Price) VALUES ("+self.timestamp.text()+\
                ","+self.oopen.text()+","+self.high.text()+","+self.low.text()+","+self.Close.text()+","+self.VBTC.text()+","+self.VC.text()+","+self.WP.text()+")"

        con.exec(query)
        con.close()
        self.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec_())