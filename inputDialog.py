import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QInputDialog, QLabel
)
from PyQt5.QtCore import Qt

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.resize(500, 200)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        button_width = 150  # Lebar tetap tombol

        # Row 1
        row1 = QHBoxLayout()
        self.btn_item = QPushButton("Choose from list")
        self.btn_item.setFixedWidth(button_width)
        self.le = QLineEdit()
        self.le.setMinimumWidth(250)
        row1.addWidget(self.btn_item)
        row1.addWidget(self.le)
        self.btn_item.clicked.connect(self.getItem)

        # Row 2
        row2 = QHBoxLayout()
        self.btn_text = QPushButton("get name")
        self.btn_text.setFixedWidth(button_width)
        self.le1 = QLineEdit()
        self.le1.setMinimumWidth(250)
        row2.addWidget(self.btn_text)
        row2.addWidget(self.le1)
        self.btn_text.clicked.connect(self.getText)

        # Row 3
        row3 = QHBoxLayout()
        self.btn_int = QPushButton("Enter an integer")
        self.btn_int.setFixedWidth(button_width)
        self.le2 = QLineEdit()
        self.le2.setMinimumWidth(250)
        row3.addWidget(self.btn_int)
        row3.addWidget(self.le2)
        self.btn_int.clicked.connect(self.getInt)

        # Label nama di bawah tengah
        self.name_label = QLabel("L. M. Noval A. - F1D022056")
        self.name_label.setAlignment(Qt.AlignCenter)

        # Gabungkan semuanya ke layout utama
        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)
        main_layout.addStretch()  # Memberi ruang sebelum label bawah
        main_layout.addWidget(self.name_label)

        self.setLayout(main_layout)

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(
            self, "select input dialog", "list of languages", items, 0, False
        )
        if ok and item:
            self.le.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(
            self, 'Text Input Dialog', 'Enter your name:'
        )
        if ok:
            self.le1.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(
            self, "integer input dialog", "enter a number"
        )
        if ok:
            self.le2.setText(str(num))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
