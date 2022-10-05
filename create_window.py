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
    QLabel,
    QComboBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_window()

    def set_window(self):

        self.setWindowTitle("BARCODE CREATOR")
        self.setGeometry(100, 100, 200, 100)
        self.setFixedSize(300, 200)

        self.label_code = QLabel()
        self.label_code.setText('Barcode type')

        self.label_width = QLabel()
        self.label_width.setText('Label width')

        self.label_high = QLabel()
        self.label_high.setText('Label hight')

        self.combobox_code = QComboBox()
        self.combobox_code.addItems(["ean13",
                                    "ean13-guard",
                                    "ean",
                                    "ean8",
                                    "ean8-guard",
                                    "gtin",
                                    "ean14",
                                    "jan",
                                    "upc",
                                    "upca",
                                    "isbn",
                                    "isbn13",
                                    "gs1",
                                    "isbn10",
                                    "issn",
                                    "code39",
                                    "pzn",
                                    "code128",
                                    "itf",
                                    "gs1_128",
                                    "codabar",
                                    "nw-7"
                                    ])

        self.spinbox_width = QSpinBox()
        self.spinbox_width.setValue(80)

        self.spinbox_high = QSpinBox()
        self.spinbox_high.setValue(20)

        self.button_file = QPushButton('Choose CSV file')
        self.button_file.clicked.connect(lambda: self.open_dialog())

        self.button_folder = QPushButton('Where to save')
        self.button_folder.clicked.connect(lambda: self.open_folder_dialog())

        self.label_filename = QLineEdit('ean13_1.csv')
        self.label_foldername = QLineEdit()

        self.button_create = QPushButton('Create labels')
        self.button_create.clicked.connect(lambda: self.create_labels())

        container = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.label_code, 0, 0)
        layout.addWidget(self.combobox_code, 0, 1)
        layout.addWidget(self.label_width, 1, 0)
        layout.addWidget(self.spinbox_width, 1, 1)
        layout.addWidget(self.label_high, 2, 0)
        layout.addWidget(self.spinbox_high, 2, 1)
        layout.addWidget(self.button_file, 3, 0)
        layout.addWidget(self.label_filename, 3, 1, 1, 1)
        layout.addWidget(self.button_folder, 4, 0)
        layout.addWidget(self.label_foldername, 4, 1, 1, 1)
        layout.addWidget(self.button_create, 5, 0, 1, 2)

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


    def open_folder_dialog(self):
        folder_to_save = QFileDialog.getExistingDirectory(self, 'Choose folder to save images')
        self.label_foldername.setText(folder_to_save)

    def create_labels(self):
        bar_code.print_barcode(
                get_csv.get_csv(self.label_filename.text()),
                self.combobox_code.currentText(),
                self.label_foldername.text()
                )
