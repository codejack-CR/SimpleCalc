from functools import partial

from calc.pycalc_model import ERROR_MSGS


class CalcCtrl:
    def __init__(self, evaluate, view):
        # Connect controller to model and view
        self._evaluate = evaluate
        self._view = view
        # Create triggers for events
        self._connect_signals()

    def _calculate_res(self):
        result = self._evaluate(expr=self._view.get_display_txt())
        self._view.set_display_txt(result)

    def _build_expression(self, sub_exp):
        if self._view.get_display_txt() in ERROR_MSGS:
            self._view.clear_display()

        expression = self._view.get_display_txt() + sub_exp
        self._view.set_display_txt(expression)

    def _connect_signals(self):
        for btn_txt, btn in self._view.buttons.items():
            if btn_txt not in ['=', 'C']:
                btn.clicked.connect(partial(self._build_expression, btn_txt))

        # Connect clear key
        self._view.buttons['C'].clicked.connect(self._view.clear_display)

        # Connect Equal key or Enter press
        self._view.buttons['='].clicked.connect(self._calculate_res)
        self._view.display.returnPressed.connect(self._calculate_res)
