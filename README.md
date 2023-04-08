# heart-disease-prediction
Heart Disease Prediction is providing a machine learning solution for predicting heart disease in patients. It includes a script that preprocesses patient data, trains various machine learning models, and selects the best performing model for predicting the likelihood of heart disease in new patients.


![image](https://user-images.githubusercontent.com/114264135/230742520-cdc34605-e338-4650-91d9-dda3a52a8c4c.png)

Team Name: Vector AI
Team members: -
1- احمد عماد عبدالفتاح رمضان
2- احمد طارق محمد على زاهر
3- احمد عبدالحميد احمد عبدالمقصود
Project title: heart disease prediction using machine learning.


The PEAS components for the project:
Performance measure:
Accuracy in predicting heart disease cases using the built model.
Overall classification error rate (False Positive Rate and False Negative Rate).

Environment:
Data of individuals suspected of having heart disease.
Medical data variables collected during the medical examination such as age, gender, blood pressure, etc.

Actuators:
The computer screen is the actuator.
The expected output on screen from the system is a prediction of the presence or absence of heart disease.
The output can be a value between true and false or 0% to 100% representing the probability of the presence of heart disease or a decision value (true or false) representing the presence or absence of heart disease.

Sensors:
The sensors are the keyboard and mouse, which are used to input data from individuals suspected of having heart disease.
The input data includes medical examination data such as age, gender, blood pressure, and other relevant information needed for the machine learning model to predict the likelihood of heart disease.

The ODESA components for the project:
Observability:
 The system is fully observable as it has access to all the relevant information of the individuals such as medical examination data like age, gender, blood pressure, etc.

Determinism:
The system is deterministic since it follows a fixed set of algorithms to predict the likelihood of heart disease in individuals based on their medical examination data.

Episode: 
The system is episode as it is trained and tested on a fixed dataset, and each prediction of the likelihood of heart disease is considered as a single episode.
Static:
The system is static as the dataset used to build and test the model does not change over time.
Agent: 
The system is a single-agent system as it involves only one agent, i.e., the machine learning model, that predicts the likelihood of heart disease in individuals based on their medical examination data.


