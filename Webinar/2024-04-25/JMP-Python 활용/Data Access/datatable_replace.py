# -*- coding: utf-8 -*-
import sys, jmp
from PySide6.QtWidgets import QApplication, QTableWidgetItem
from PySide6.QtCore import Qt
from datatable_replace_ui import QMainWindow, Ui_DatatableReplace


class DatatableReplace(QMainWindow, Ui_DatatableReplace):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def showEvent(self, ev):
        self.tw_data.setColumnCount(dt.ncols)
        self.tw_data.setRowCount(dt.nrows)

        self.tw_data.setHorizontalHeaderLabels([
            dt[cidx].name
            for cidx in range(dt.ncols)
        ])

        for cidx in range(dt.ncols):
            for ridx in range(dt.nrows):
                self.tw_data.setItem(ridx, cidx, QTableWidgetItem(str(dt[cidx][ridx])))


        self.tw_data.itemChanged.connect(self.on_tw_data_item_changed)

        super().showEvent(ev)


    def on_tw_data_item_changed(self, item:QTableWidgetItem):
        print(f"[python] item changed / row: {item.row()} / column: {item.column()} / value: {item.text()}")

    def fn_apply(self):
        for cidx in range(dt.ncols):
            for ridx in range(dt.nrows):
                item = self.tw_data.item(ridx, cidx)
                dt[cidx][ridx] = float(item.text())


if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    win = DatatableReplace()
    win.showNormal()

    sys.exit(app.exec())
