from PyQt6.QtWidgets import QLineEdit, QApplication
from PyQt6 import QtWidgets, uic
from random import randint
import clipboard

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file.ui', self)
        self.button.clicked.connect(self.func1)     # Generate password
        self.button_2.clicked.connect(self.func2)  # Copy password
        self.setWindowTitle("PassGen app")
        self.generated_password = ""               # Store the last password
        
    def func(self):
        try:
            pw_length = int(self.textEdit.toPlainText())
        except ValueError:
            self.result.setText("Enter a number")
            return None

        if pw_length <= 0:
            self.result.setText("Length must be > 0")
            return None

        my_password = ''.join(chr(randint(33, 126)) for _ in range(pw_length))
        return my_password
    
    def func1(self):
        password = self.func()
        if password:
            self.generated_password = password      # Save it
            self.result.setText(password)
        
    def func2(self):
        if self.generated_password:
            clipboard.copy(self.generated_password)
        else:
            self.result.setText("Generate password first!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
