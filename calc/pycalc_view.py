from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class CalcWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set initial window size and title
        self.setFixedSize(280, 300)
        self.setWindowTitle("PyCalc")
        # Skeleton
        # Simple vertical box layout
        # Set the central widget and the general layout
        self._central_widget = QWidget(self)
        self.vbox_lyt = QVBoxLayout(self._central_widget)
        self.setCentralWidget(self._central_widget)

        self.statusBar().showMessage("Author : CodeJack")

        # Create GUI
        self._create_gui()

    def _create_gui(self):
        # Create the display area
        self._create_display()

        # Create a grid for buttons
        self._create_btn_grid()

        pass

    def _create_display(self):
        # Add a read-only QLineEdit for display
        self.display = QLineEdit(self._central_widget)
        self.display.setFixedHeight(50)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.vbox_lyt.addWidget(self.display)

    def _create_btn_grid(self):
        # Declare the layout
        btn_lyt = QGridLayout()

        # Declare the dictionary of buttons
        self.buttons = {}
        btn_pos = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }

        for btn_txt, pos in btn_pos.items():
            self.buttons[btn_txt] = QPushButton(btn_txt)
            self.buttons[btn_txt].setFixedSize(50, 50)
            btn_lyt.addWidget(self.buttons[btn_txt], pos[0], pos[1])

        # Add this grid to layout
        self.vbox_lyt.addLayout(btn_lyt)

    def set_display_txt(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def clear_display(self):
        self.display.clear()
        self.display.setFocus()

    def get_display_txt(self):
        return self.display.text()
