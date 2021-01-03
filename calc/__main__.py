__version__ = '0.1'
__author__ = 'CodeJack'

import sys
from calc.pycalc_view import CalcWindow
from calc.pycalc_contrllr import CalcCtrl
from calc.pycalc_model import evaluate
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    gui = CalcWindow()
    _evaluate = evaluate
    CalcCtrl(evaluate=_evaluate, view=gui)

    gui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
