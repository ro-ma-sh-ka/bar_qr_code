import bar_code
import get_csv
from pathlib import Path
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QSpinBox,
    QGridLayout,
    QWidget,
    QFileDialog,
    QLineEdit,
    QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_window()

    def set_window(self):

        self.setWindowTitle("BARCODE CREATOR")
        self.setGeometry(100, 100, 200, 100)
        self.setMinimumSize(200, 200)

        self.label_code = QLabel()
        self.label_code.setText('Barcode type')

        self.label_width = QLabel()
        self.label_width.setText('Label width')

        self.label_high = QLabel()
        self.label_high.setText('Label hight')

        self.spinbox_code = QSpinBox()
        self.spinbox_code.setValue(80)

        self.spinbox_width = QSpinBox()
        self.spinbox_width.setValue(80)

        self.spinbox_high = QSpinBox()
        self.spinbox_high.setValue(20)

        self.button_file = QPushButton('Choose CSV file')
        self.button_file.clicked.connect(lambda: self.open_dialog())

        self.label_filename = QLineEdit()

        self.button_create = QPushButton('Create labels')
        self.button_create.clicked.connect(lambda: self.create_labels())

        container = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.label_code, 0, 0)
        layout.addWidget(self.spinbox_code, 0, 1)
        layout.addWidget(self.label_width, 1, 0)
        layout.addWidget(self.spinbox_width, 1, 1)
        layout.addWidget(self.label_high, 2, 0)
        layout.addWidget(self.spinbox_high, 2, 1)
        layout.addWidget(self.button_file, 3, 0)
        layout.addWidget(self.label_filename, 3, 1, 1, 1)
        layout.addWidget(self.button_create, 4, 0, 1, 2)

        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_dialog(self):
        home_dir = str(Path.home())
        filename = QFileDialog.getOpenFileName(
            self,
            "Open File",
            home_dir,
            "CSV files (*.csv);; All Files (*)",
        )
        self.label_filename.setText(str(filename[0]))

    def create_labels(self):
        bar_code.print_barcode(get_csv.get_csv(self.label_filename.text()))
