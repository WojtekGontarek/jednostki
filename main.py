import sys

from PyQt6.QtGui import qPremultiply
from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.convertButton.clicked.connect(self.convert)
        self.ui.kmmile_km.textChanged.connect(self.convert_km)
        self.ui.kmmile_mile.textChanged.connect(self.convert_mile)

        self.ui.inchcm_cm.textChanged.connect(self.convert_cm)
        self.ui.inchcm_inch.textChanged.connect(self.convert_inch)

        self.ui.fc_c.textChanged.connect(self.convert_c)
        self.ui.fc_f.textChanged.connect(self.convert_f)

        self.show()

    def convert_km(self):
        self.ui.kmmile_mile.setValue(self.ui.kmmile_km*0.621371)
    def convert_mile(self):
        self.ui.kmmile_km.setValue(self.ui.kmmile_mile/0.621371)

    def convert_cm(self):
        self.ui.inchcm_inch.setValue(self.ui.inchcm_cm*0.3937)
    def convert_inch(self):
        self.ui.inchcm_cm.setValue(self.ui.inchcm_inch/0.3937)

    def convert_f(self):
        self.ui.fc_c.setValue(self.ui.inchcm_inch/0.3937)
