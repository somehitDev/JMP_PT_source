# -*- coding: utf-8 -*-
import sys, jmp
from PySide6.QtWidgets import QApplication
from simple_replace_ui import QMainWindow, Ui_SimpleReplace


class SimpleReplaceWindow(QMainWindow, Ui_SimpleReplace):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    
    def on_item_changed(self, item:str):
        print("[python] item: ", item)

    def on_value_changed(self, value:str):
        print("[python] value: ", value)

    def fn_apply(self):
        jmp.run_jsl(f'setItem("{self.cb_item.currentText()}");')
        jmp.run_jsl(f'value = "{self.le_value.text()}";')
        jmp.run_jsl("Show(item);Show(value);")


if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    win = SimpleReplaceWindow()
    win.showNormal()

    sys.exit(app.exec())
