import PyQt5
from sampel import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
import sys
from operator import add, sub, mul, truediv
x = None
y = None
point = False

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
ui.label.setText('0')


def clear() -> None:
    ui.label.setText('0')


def add_digit(bnt_text: str) -> None:
    if ui.label.text() == '0':
        ui.label.setText(bnt_text)
    else:
        ui.label.setText(ui.label.text() + bnt_text)


def add_point():
    if not point:
        ui.label.setText(ui.label.text() + '.')


def equels():
    expression = ui.label.text()
    try:
        if '+' in expression:
            x, y = expression.split('+')
            A = str(add(float(x), float(y)))
            ui.label.setText(str(A))
        elif '-' in expression:
            x, y = expression.split('-')
            A = str(sub(float(x), float(y)))
            ui.label.setText(str(A))
        elif '*' in expression:
            x, y = expression.split('*')
            A = str(mul(float(x), float(y)))
            ui.label.setText(str(A))
        elif '/' in expression:
            x, y = expression.split('/')
            A = str(truediv(float(x), float(y)))
            ui.label.setText(str(A))
    except ValueError:
        ui.label.setText('Error')
    except ZeroDivisionError:
        ui.label.setText('Error')


ui.number_10.clicked.connect(lambda: add_digit('0'))
ui.number_1.clicked.connect(lambda: add_digit('1'))
ui.number_2.clicked.connect(lambda: add_digit('2'))
ui.number_3.clicked.connect(lambda: add_digit('3'))
ui.number_4.clicked.connect(lambda: add_digit('4'))
ui.number_5.clicked.connect(lambda: add_digit('5'))
ui.number_6.clicked.connect(lambda: add_digit('6'))
ui.number_7.clicked.connect(lambda: add_digit('7'))
ui.number_8.clicked.connect(lambda: add_digit('8'))
ui.number_9.clicked.connect(lambda: add_digit('9'))
ui.pushButton_2.clicked.connect(lambda: add_digit('+'))
ui.pushButton_3.clicked.connect(lambda: add_digit('-'))
ui.pushButton_4.clicked.connect(lambda: add_digit('*'))
ui.pushButton_5.clicked.connect(lambda: add_digit('/'))
ui.pushButton.clicked.connect(equels)
ui.pushButton_6.clicked.connect(add_point)
ui.pushButton_7.clicked.connect(clear)

sys.exit(app.exec_())
