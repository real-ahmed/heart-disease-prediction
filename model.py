import pandas as pd
import numpy as np

def heart_disease_prediction(data):
    # Load dataset
    df = pd.read_csv("dataset.csv")

    # Drop any rows with missing values
    df.dropna(inplace=True)

    # Split the dataset into features (X) and target (y)
    X = df.drop('target', axis=1)
    y = df['target']

    # Convert data input to numpy array
    data = np.array(data)

    # Calculate prior probabilities
    target_counts = y.value_counts()
    p_heart_disease = target_counts[1] / len(y)
    p_no_heart_disease = target_counts[0] / len(y)

    # Calculate likelihood probabilities
    likelihood_heart_disease = []
    likelihood_no_heart_disease = []
    for i in range(X.shape[1]):
        feature_values = X.iloc[:, i].unique()
        likelihood_heart_disease.append(
            [sum((X.iloc[:, i] == value) & (y == 1)) / target_counts[1] for value in feature_values])
        likelihood_no_heart_disease.append(
            [sum((X.iloc[:, i] == value) & (y == 0)) / target_counts[0] for value in feature_values])

    # Make predictions on input data
    predictions = []
    probabilities = []
    for i in range(data.shape[0]):
        p_heart_disease_given_data = p_heart_disease
        p_no_heart_disease_given_data = p_no_heart_disease
        for j in range(data.shape[1]):
            # Check if the unique value in input data is present in the training data
            if data[i, j] in X.iloc[:, j].unique():
                # Find the index of the unique value in the training data
                index = np.where(X.iloc[:, j].unique() == data[i, j])[0][0]
                # Calculate likelihood probabilities only if the unique value is present in the training data
                p_heart_disease_given_data *= likelihood_heart_disease[j][index]
                p_no_heart_disease_given_data *= likelihood_no_heart_disease[j][index]

        if p_heart_disease_given_data > p_no_heart_disease_given_data:
            predictions.append(1)
            probabilities.append(p_heart_disease_given_data / (p_heart_disease_given_data + p_no_heart_disease_given_data) * 100)
        else:
            predictions.append(0)
            probabilities.append(p_no_heart_disease_given_data / (p_heart_disease_given_data + p_no_heart_disease_given_data) * 100)

    # Return predictions and probabilities
    return [predictions[0], int(probabilities[0])]




