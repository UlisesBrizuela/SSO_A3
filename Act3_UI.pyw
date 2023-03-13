from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
import sys


class Ui_MainWindow(object):
    ######################### DESARROLLO DE PLANIFICADORES #######################################################
    def Archivo(self):
        procesos = []
        with open("./procesos.txt", 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                proceso, ciclos, prioridad = linea.strip().split(',')
                procesos.append((proceso, int(ciclos), int(prioridad)))
        return procesos

    def RoundRobin(self):
        self.label.setText("")
        Q = 3
        cola = deque(self.Archivo())
        while cola:
            proceso_actual = cola.popleft()
            nombre, quantum, p = proceso_actual
            self.label.append(f"Ejecuntando: {nombre}, con {quantum} quantum.")
            quantum -= Q
            if quantum > 0:
                cola.append((nombre, quantum, p))
                self.label.append(f"El proceso: {nombre} volvio a la cola con {quantum} quantum restantes.\n")
            else:
                self.label.append(f"Proceso {nombre} terminado.\n")
    
    def SFJ(self):
        self.label.setText("")
        cola = deque(sorted(self.Archivo(), key = lambda x: x[1]))
        while cola:
            proceso_actual = cola.popleft()
            nombre, tamaño, p = proceso_actual
            self.label.append(f"Proceso ejecutado: {nombre} con {tamaño} ciclos.\n")

    def FIFO(self):
        self.label.setText("")
        cola = deque(self.Archivo())
        while cola:
            proceso_actual = cola.popleft()
            nombre, q, p = proceso_actual
            self.label.append(f"Proceso ejecutado: {nombre}.\n")

    def Prioridades(self):
        self.label.setText("")
        cola = deque(sorted(self.Archivo(), key = lambda x: x[2]))
        while cola:
            proceso_actual = cola.popleft()
            nombre, q, prioridad = proceso_actual
            self.label.append(f"Proceso Ejecutado: {nombre}, con prioridad {prioridad}.\n")

############################ DEFINICIONES DE GUI ###################################################################
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1280, 720)
        MainWindow.setWindowTitle("ALGORITMOS DE PLANIFICACION")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1040, 10, 231, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("SELECCIONA UNA OPCION")

        self.RoundRobin_B = QtWidgets.QRadioButton(self.groupBox)
        self.RoundRobin_B.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.RoundRobin_B.setText("ROUND ROBIN")

        self.SJF_B = QtWidgets.QRadioButton(self.groupBox)
        self.SJF_B.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.SJF_B.setText("SJF")

        self.Fifo_B = QtWidgets.QRadioButton(self.groupBox)
        self.Fifo_B.setGeometry(QtCore.QRect(20, 60, 95, 20))
        self.Fifo_B.setText("FIFO")

        self.Prio_B = QtWidgets.QRadioButton(self.groupBox)
        self.Prio_B.setGeometry(QtCore.QRect(20, 80, 150, 20))
        self.Prio_B.setText("PRIORIDADES")


        self.scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll.setGeometry(QtCore.QRect(0, 0, 1031, 721))   
        self.scroll.setWidgetResizable(True)
        
        self.scrollCont = QtWidgets.QWidget()
        self.scrollCont.setGeometry(QtCore.QRect(0, 0, 1031, 721))


        self.label = QtWidgets.QTextBrowser(self.scrollCont)
        self.label.setGeometry(QtCore.QRect(0, 0, 1031, 721))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setText("SELECCIONE UNA OPCION Y PRESIONE EL BOTON PROCESAR")
        self.label.setFont(font)
        self.scroll.setWidget(self.scrollCont)

        self.proces_B = QtWidgets.QPushButton(self.centralwidget)
        self.proces_B.setGeometry(QtCore.QRect(1040, 140, 93, 28))
        self.proces_B.setText("PROCESAR")


        self.Exit_B = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_B.setGeometry(QtCore.QRect(1140, 140, 93, 28))
        self.Exit_B.setText("SALIR")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

####################### OPERACIONES DE PRESIONAR Y SELECCIONAR ############################################################
        self.proces_B.clicked.connect(self.selecciones)
        self.Exit_B.clicked.connect(self.salida)
    
    def selecciones(self):
        if self.RoundRobin_B.isChecked():
            self.RoundRobin()
        elif self.SJF_B.isChecked():
            self.SFJ()
        elif self.Fifo_B.isChecked():
            self.FIFO()
        elif self.Prio_B.isChecked():
            self.Prioridades()
    def salida():
        sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
