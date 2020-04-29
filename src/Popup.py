
from PySide2.QtWidgets import QMessageBox, QApplication




class Popup(QMessageBox):
    def __init__(self,title = "", main_text = ""):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(main_text)

        self.setIcon(QMessageBox.Warning)
		# self.setStandardButtons(QMessageBox.Ok|QMessageBox.Retry|QMessageBox.Ignore|)
		# self.setDefaultButton(QMessageBox.Retry)
		# self.setInformativeText("informative text, ya!")

		# self.setDetailedText("details")


class PopupError(Popup):

    def __init__(self,title = "", main_text = ""):
        super().__init__()
        self.self.setStandardButtons(QMessageBox.Ok)
        self.setDefaultButton(QMessageBox.Retry)





if __name__ == "__main__":
    qt_app = QApplication()
    p = Popup('title', 'test test')
    p.show()
    qt_app.exec_()
