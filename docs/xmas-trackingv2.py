import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

class DataFrameQueryApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('DataFrame Query App')

        self.name_label = QLabel('Select Name:')
        self.name_combobox = QComboBox(self)
        self.name_combobox.addItems(df['Name'].unique())

        self.query_button = QPushButton('Query', self)
        self.query_button.clicked.connect(self.query_dataframe)

        self.result_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_combobox)
        layout.addWidget(self.query_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def query_dataframe(self):
        selected_name = self.name_combobox.currentText()
        self.result_label.clear()  # Clear previous result

        # Query the DataFrame
        result = df[df['Name'] == selected_name]

        # Display the result
        if not result.empty:
            self.result_label.setText(f"Result: {result.to_string(index=False)}")
        else:
            self.result_label.setText("No matching records")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataFrameQueryApp()
    window.show()
    sys.exit(app.exec_())











