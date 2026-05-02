from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(lambda: self.submit())

    def submit(self):
        import csv

        full_name = self.fullname_lineedit.text().strip()
        email = self.email_lineedit.text().strip()
        number = self.number_lineedit.text().strip()
        issue = self.textEdit.toPlainText().strip()

        if full_name == "":
            self.validation_label.setText("Enter your name")
            return
        if email == "":
            self.validation_label.setText("Enter your email")
            return
        if number == "":
            self.validation_label.setText("Enter your number")
            return
        if issue == "":
            self.validation_label.setText("Enter your issue")
            return

        with open("tickets.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([full_name, email, number, issue])

        self.validation_label.setText("Ticket has been submitted")

        self.fullname_lineedit.clear()
        self.email_lineedit.clear()
        self.number_lineedit.clear()
        self.textEdit.clear()

        self.fullname_lineedit.setFocus()