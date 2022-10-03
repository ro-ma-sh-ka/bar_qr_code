from create_window import MainWindow
from PyQt6.QtWidgets import QApplication


app = QApplication([])
window = MainWindow()
window.show()
exit(app.exec())
