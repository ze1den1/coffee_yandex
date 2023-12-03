import sqlite3
import sys

from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from UI.main import Ui_Coffee
from UI.addEditCoffeeForm import Ui_AddForm

con = sqlite3.connect('data/coffee.sqlite')
cur = con.cursor()


class AddEdit(QWidget, Ui_AddForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__i = 0

        self.execute.clicked.connect(self.run)

    def run(self) -> None:
        coffee_id = self.id_edit.text()
        name = self.name_edit.text()
        roasting = self.roasting_edit.text()
        price = self.price.value()
        volume = self.volume.value()
        taste = self.taste.toPlainText()
        coffee_type = int(self.coffee_type.isChecked())

        try:
            cur.execute(f"""SELECT id FROM coffee WHERE id == {coffee_id}""").fetchall()
        except sqlite3.OperationalError:
            print('Введите корректный айди')
            return
        if cur.execute(f"""SELECT id FROM coffee WHERE id == {coffee_id}""").fetchall():
            if name:
                cur.execute(f"""UPDATE coffee SET 'название сорта' = '{name}' WHERE
                            coffee.ID = '{coffee_id}'""")
            if roasting:
                cur.execute(f"""UPDATE coffee SET 'степень обжарки' = '{roasting}' WHERE
                            coffee.ID = '{coffee_id}'""")
            if price > 0:
                cur.execute(f"""UPDATE coffee SET 'цена (руб)' = '{price}' WHERE
                            coffee.ID = '{coffee_id}'""")
            if volume > 0:
                cur.execute(f"""UPDATE coffee SET 'объем упаковки (мл)' = '{volume}' WHERE
                            coffee.ID = '{coffee_id}'""")
            if taste:
                cur.execute(f"""UPDATE coffee SET 'описание вкуса' = '{taste}' WHERE
                            coffee.ID = '{coffee_id}'""")
            cur.execute(f"""UPDATE coffee SET 'молотый/в зернах' = '{coffee_type}' WHERE
                        coffee.ID = '{coffee_id}'""")
        else:
            cur.execute(f"""INSERT INTO coffee ('название сорта', 'степень обжарки', 'молотый/в зернах',
                        'описание вкуса', 'цена (руб)', 'объем упаковки (мл)') VALUES ('{name}', '{roasting}',
                                                                                '{coffee_type}', '{taste}',
                                                                                '{price}', '{volume}')""")
        self.__i += 1

        con.commit()
        self.check.setText(str(self.__i))
        self.id_edit.clear()
        self.name_edit.clear()
        self.roasting_edit.clear()
        self.price.setValue(0)
        self.volume.setValue(0)
        self.taste.setText('')


class Coffee(QMainWindow, Ui_Coffee):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._add_edit = AddEdit()

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data/coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        db.close()

        self.coffee_view.setModel(model)

        self.add_btn.clicked.connect(self.add_edit_show)
        self._add_edit.check.textChanged.connect(self.update_table)

    def update_table(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data/coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        db.close()
        self.coffee_view.setModel(model)

    def add_edit_show(self) -> None:
        self._add_edit.show()


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    sys._excepthook = sys.excepthook
    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    w = Coffee()
    w.show()
    sys.exit(app.exec())
