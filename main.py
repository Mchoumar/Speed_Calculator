from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QPushButton, QGridLayout, \
    QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the grid layout
        grid = QGridLayout()

        # Label and input for the distance
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        # Label and input for the time
        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()

        # Expandable that allows you to switch between metric and imperial sign
        self.expandable = QComboBox()
        self.expandable.addItems(["metric (km)", "imperial (mile)"])

        # Calculate button
        self.button = QPushButton("Calculate")
        self.button.clicked.connect(self.calculate())

        # Output for the result
        self.output_label = QLabel("")

        # Out put the user interface
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(self.expandable, 0, 2)
        grid.addWidget(self.button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    # Changes between the selection options
    def calculate(self):
        # Gets the current
        check = self.expandable.currentText()

        # Checks if the selection is in km or mile and makes the calculation
        if "km" in check:
            print(check)
        elif "mile" in check:
            print(check)


# Constructs the application and displays it
app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
