####part 1 import file
import numpy as np

import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from  tensorflow import keras
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import recall_score, f1_score, accuracy_score
from prettytable import PrettyTable
from tensorflow import keras
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def dn(result , frame ,tb,data ):
        RANDOM_STATE_SEED = 12

        # Load the data
        line_number =93
        df = pd.read_csv(data )
       

        # Replace every value in columns to NaN
        df.replace([np.inf, -np.inf], np.nan, inplace=True)

        # Remove every row that has NaN value
        df.dropna(inplace=True)

        if 'Timestamp' in df.columns:
            df.drop(['Timestamp'], axis=1, inplace=True)

        # Split data into features and labels
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_STATE_SEED)

        # Preprocessing: Scale data to [0, 1]
        scaler = MinMaxScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Encode labels
        le = LabelEncoder()
        le.fit(y_train)
        y_train = le.transform(y_train)
        y_test = le.transform(y_test)
        num_classes = len(le.classes_)
        y_train =  keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)

        # Ensure that train and test datasets have the same number of columns
        X_train = pd.DataFrame(X_train)
        X_test = pd.DataFrame(X_test)
        X_train, X_test = X_train.align(X_test, axis=1, fill_value=0)

        # Define the model architecture
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(num_classes, activation='softmax')
        ])
        # Compile the model
        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])


        ####part 3 testing


        # Load the model
        model = keras.models.load_model("C:/Users/najme/PycharmProjects/pythonProject1/my_model")

        # Define the attack type names based on their frequency in the dataset
        label_counts = df['Label'].value_counts()
        attack_type_names = list(label_counts.index)
        attack_type_dict = {i: attack_type_names[i] for i in range(len(attack_type_names))}

        y_pred = model.predict(X_test)
        if y_pred.shape[-1] == 1:
            # Convert predicted probabilities to binary labels
            y_pred_classes = (y_pred > 0.5).astype(int)
        else:
            # Convert predicted probabilities to one-hot encoded labels
            y_pred_classes = np.argmax(y_pred, axis=1).reshape(-1, 1)

        # Convert true labels to their corresponding attack type names for the test set
        y_true_classes_names = np.vectorize(attack_type_dict.get)(np.argmax(y_test, axis=1).reshape(-1, 1).ravel(), 'Unknown')

        # Convert predicted class labels to attack type names
        y_pred_classes_names = np.vectorize(attack_type_dict.get)(y_pred_classes.ravel())

        # Update the labels list to include known attack types and any new attack types
        labels = list(attack_type_dict.values())

        # Calculate the accuracy for the test set and print it as a percentage
        accuracy = accuracy_score(np.argmax(y_test, axis=1), y_pred_classes)
        accuracy_pct = accuracy * 100
        print("The attack detection system has an accuracy of {:.2f}% on the test set.".format(accuracy_pct))

        # Calculate recall and F1 scores for each class
        recalls = recall_score(y_true_classes_names, y_pred_classes_names, average=None)
        f1_scores = f1_score(y_true_classes_names, y_pred_classes_names, average=None)

        # Create a table
        table = PrettyTable()
        table.field_names = ["Attack Type", "Recall", "F1 Score"]

        # Add rows to the table
        for i, label in enumerate(labels):
            table.add_row([label, f"{recalls[i]:.4f}", f"{f1_scores[i]:.4f}"])
        # Print the table
        print(table)

        tb.setHorizontalHeaderLabels(table.field_names)

        # Add the rows to the Qt table
        for row_idx, row in enumerate(table._rows):
            for col_idx, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                tb.setItem(col_idx, row_idx, item)

        # Check for new attacks with recall and F1 score of 0.00
        new_attacks_detected = False
        for i in range(len(recalls)):
            if recalls[i] == 0.0 and f1_scores[i] == 0.0:
                label = labels[i]
                new_attack_type_name = f"{label} (new)"
                attack_type_dict[len(attack_type_dict)] = new_attack_type_name
                attack_type_names.append(new_attack_type_name)
                y_true_classes_names[y_true_classes_names == label] = new_attack_type_name
                y_pred_classes_names[y_pred_classes_names == label] = new_attack_type_name
                result.setText(f"New attack type detected: {new_attack_type_name}")
                new_attacks_detected = True

        if not new_attacks_detected:

            result.setText("All attacks have been detected." + "There are no new attacks.")


        # Create a bar chart of recall scores for each attack type

        # Create a Matplotlib figure and add a plot
        figure = Figure(figsize=(12, 6))
        canvas = FigureCanvas(figure)
        axes = figure.add_subplot(111)
        axes.bar(labels, recalls)
        axes.set_title("Recall Scores by Attack Type")
        axes.set_xlabel("Attack Type")
        axes.set_ylabel("Recall Score")
        plt.xticks(rotation=90)

        # Add the plot canvas to the Qt frame
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        frame.setLayout(layout)
