from PyQt6.QtWidgets import *
from gui import *
import os
#I got "import os" from Ai. I used it to be able to later in the code be able to add a beginner header into the Excel file so that you can see which collum was the name and candidate the chose
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.vote_button.clicked.connect(lambda: self.submit())
        self.exit_button.clicked.connect(lambda: self.close())

    def submit(self):
        import csv

        name = self.name_field.text().strip()

        if name == "":
            self.label_validation.setText("Enter Your Name")
            return
        if self.bob_button.isChecked():
            candidate = "Bob"
        elif self.corey_button.isChecked():
            candidate = "Corey"
        elif self.jerald_button.isChecked():
            candidate = "Jerald"
        else:
            self.label_validation.setText("Please select a candidate.")
            return

        file_exists = os.path.isfile("data.csv")
#This above line I used a Ai on in conjuction to the beggining needing to import operating system tools to be able to look into the "data.csv" file to be able to check it
        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Candidate"])
            writer.writerow([name, candidate])
#In conjuction with line 32 this looks for "Name, Candidate" so that it only writes it once in the file and having it be at the top and never doing it again so that it is not repeatedly writing that after every submission
        self.label_validation.setText("Vote Submitted.")
        self.name_field.clear()

        if self.voteGroup.checkedButton() is not None:
            self.voteGroup.setExclusive(False)
            self.voteGroup.checkedButton().setChecked(False)
            self.voteGroup.setExclusive(True)

        self.name_field.setFocus()