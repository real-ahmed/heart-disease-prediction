from PyQt5.QtWidgets import (
    QApplication, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout, QWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import numpy as np
from model import heart_disease_prediction



class HeartDiseaseForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Heart Disease Prediction")

        # input fields

        self.age_edit = QLineEdit()
        self.sex_combo = QComboBox()
        self.chest_pain_combo = QComboBox()
        self.bp_edit = QLineEdit()
        self.chol_edit = QLineEdit()
        self.sugar_check = QCheckBox()
        self.ecg_check = QCheckBox()
        self.max_hr_edit = QLineEdit()
        self.angina_check = QCheckBox()
        self.st_edit = QLineEdit()
        self.slope_combo = QComboBox()
        self.vessels_combo = QComboBox()
        self.thal_combo = QComboBox()

        # data Validator
        self.age_edit.setValidator(QIntValidator())
        self.bp_edit.setValidator(QIntValidator())
        self.chol_edit.setValidator(QIntValidator())
        self.max_hr_edit.setValidator(QIntValidator())
        self.st_edit.setValidator(QIntValidator())
        self.sex_combo.addItems(["Male", "Female"])
        self.chest_pain_combo.addItems(["0", "1", "2", "3"])
        self.slope_combo.addItems(["Upsloping", "Flat", "Downsloping"])
        self.vessels_combo.addItems(["0", "1", "2", "3"])
        self.thal_combo.addItems(["Normal", "Fixed Defect", "Reversible Defect"])

        #defined labels
        self.labels = {
            self.age_edit: "Age:",
            self.sex_combo: "Sex:",
            self.chest_pain_combo: "Chest Pain Level:",
            self.bp_edit: "Resting Blood Pressure (mmHg):",
            self.chol_edit: "Cholesterol (mg/dL):",
            self.sugar_check: "Fasting Blood Sugar (>120 mg/dL):",
            self.ecg_check: "Resting ECG Results:",
            self.max_hr_edit: "Maximum Heart Rate:",
            self.angina_check: "Exercise Induced Angina:",
            self.st_edit: "ST Depression Induced by Exercise:",
            self.slope_combo: "Slope of Peak Exercise ST Segment:",
            self.vessels_combo: "Number of Major Vessels Colored by Flourosopy:",
            self.thal_combo: "Thalassemia Type:",
        }

        #create labels layout
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        for widget in self.labels.keys():
            label = QLabel(self.labels[widget])
            label.setStyleSheet("padding: 5px;")
            self.form_layout.addRow(label, widget)



        # Add submit button
        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("padding: 10px; background-color: #4CAF50; color: white; border: none;")
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(submit_button)
        submit_button.clicked.connect(self.on_submit)  # Connect the button's clicked signal to the on_submit function
        # Set form layout
        self.setLayout(self.layout)
        self.result_label = QLabel()
    def on_submit(self):
        if hasattr(self, 'result_label'):
            self.result_label.setParent(None)
            self.result_label.deleteLater()
            data = [int(self.age_edit.text()),
                    1 if self.sex_combo.currentText() == "Male" else 0,
                    int(self.chest_pain_combo.currentText()),
                    int(self.bp_edit.text()),
                    int(self.chol_edit.text()),
                    1 if self.sugar_check.isChecked() else 0,
                    1 if self.ecg_check.isChecked() else 0,
                    int(self.max_hr_edit.text()),
                    1 if self.angina_check.isChecked() else 0,
                    int(self.st_edit.text()),
                    0 if self.slope_combo.currentText() == "Upsloping" else 1 if self.slope_combo.currentText() == "Flat" else 2,
                    int(self.vessels_combo.currentText()),
                    2 if self.thal_combo.currentText() == "Normal" else 6 if self.thal_combo.currentText() == "Fixed Defect" else 7]

            result = heart_disease_prediction(np.array([data]))

            # Create a QLabel widget to display the prediction result
            if result[0] == 1:
                self.result_label = QLabel(f"You have a heart Disease\n"
                                      f"accuracy : {result[1]}%")
            else:
                self.result_label = QLabel(f"you are in perfect health\n"
                                      f"accuracy : {result[1]}%")

            self.result_label.setAlignment(Qt.AlignCenter)
            self.result_label.setStyleSheet("font-size: 20px; ")  # Set font size
            self.form_layout.addRow(self.result_label)





