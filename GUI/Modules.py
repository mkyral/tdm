from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QMessageBox

from GUI import DictComboBox, GroupBoxV, VLayout


class ModuleDialog(QDialog):
    sendCommand = pyqtSignal(str, str)

    def __init__(self, device, *args, **kwargs):
        super(ModuleDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Module [{}]".format(device.name))
        self.setMinimumWidth(300)
        self.device = device

        btns = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Close)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        gbxModules = GroupBoxV("Select Module")
        self.gb = DictComboBox(self.device.modules)
        self.gb.setCurrentText(self.device.modules[str(self.device.p['Module'])])
        gbxModules.addWidget(self.gb)

        vl = VLayout()
        vl.addWidgets([gbxModules, btns])
        self.setLayout(vl)

    def accept(self):
        self.sendCommand.emit(self.device.cmnd_topic("module"), self.gb.currentData())
        QMessageBox.information(self, "Module saved", "Device will restart.")
        self.done(QDialog.Accepted)
