# This Streamlit app allows users to select a dataset andexplore how different parameters influence the performance of a K-Nearest Neighbors (KNN) machine learning model.

# Step 0: Import libraries used to build the app, handle data, build the KNN model, and visualize and evaluate its performance.
import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt



# Step 1: Initial app setup
# Add page configuration, title, and description.
st.set_page_config(page_title = "KNN Machine Learning Explorer", page_icon = "🎯")
st.title("K-Nearest Neighbors Machine Learning Explorer 🎯")
st.markdown("Welcome to the K-Nearest Neighbors (KNN) Machine Learning Explorer! This app allows you to explore how different parameters influence the performance of a K-Nearest Neighbors (KNN) machine learning model. Use the sidebar to choose a dataset and get started!")

# Set up sidebar for dataset selection and parameter tuning
st.sidebar.header("Select Dataset & Parameters")
data_options = st.sidebar.selectbox( # Dropdown allows users to select a built-in dataset to explore or upload their own dataset in CSV format.
    "Choose a Dataset", 
    ("Breast Cancer", "Wines", "Upload a CSV file"))

# Build tabs to organize the major sections of the app.
tab1, tab2, tab3 = st.tabs(["Overview 💬", "Data Visualization 📊", "Model Evaluation 🔍"])



# Step 2: Build tab 1
# Tab 1 provides an overview of KNN and defines key parameters.
with tab1:
    st.header("Introduction to K-Nearest Neigbors (KNN)")
    st.markdown("Click each button to learn more about KNN")
    if st.button("What is KNN?"):  # Buttons allow users to move through background information at their own pace.
        st.markdown("KNN is a simple model that can be used for classification tasks where outcomes are categorical. KNN relies on the idea that similar data points in the feature space tend to have similar outcomes.")
    if st.button("How does KNN work?"):
        st.markdown("KNN classifies new data points by calculating the distance between a new data point and all training examples, then identifying the 'k' nearest neighboring data points and assigning the class most common among its neighbors to the new data point.")
    if st.button("Key Parameters of KNN"):
        st.markdown("- **Number of Neighbors (k)**: Determines how many nearby data points are considered in the classification of a new data point. It is important to select a number of neighbors that captures patterns in the data without overfitting or underfitting.")
        st.markdown("- **Weight Function**: Determines how much influence each neighbor has on the classification. 'Uniform' gives equal weight to all neighbors, while 'distance' gives more weight to closer neighbors. This can improve performance by accounting for the relevance of nearby points.")
        st.markdown("- **Distance Metric**: Determines how distance is calculated between data points. Common metrics include 'euclidean', 'manhattan', and 'cosine'. Choosing the right distance metric allows the model to adapt to the shape of the neighborhood and improves model performance.")



# Step 3: Build tab 2
# Tab 2 allows viewers to explore and visualize their chosen dataset and its features.
with tab2:
    st.header("Explore the Data")
    st.markdown("Take a moment to visualize your chosen dataset and its features! This will help you understand the data and how KNN works to classify data points based on feature similarity.")

    # Load a dataset based on the user's input.
    if data_options == "Breast Cancer":
        # Access and load the built-in Breast Cancer dataset from scikit-learn.
        from sklearn.datasets import load_breast_cancer
        cancer = load_breast_cancer()
        df = pd.DataFrame(cancer.data, columns=cancer.feature_names)  # Create a DataFrame, set feature names as column headers.
        df["target"] = cancer.target  # Identify the target variable.
        # Create a button to preview the selected dataset.
        st.subheader("Dataset Preview")
        if st.button("Click here to view"):
            st.dataframe(df.head())
    elif data_options == "Wines":
        # Access and load the built-in Wine dataset from scikit-learn
        from sklearn.datasets import load_wine
        wine = load_wine()
        df = pd.DataFrame(wine.data, columns=wine.feature_names) # Create a DataFrame, set feature names as column headers
        df["target"] = wine.target  # Identify the target variable.
        # Create a button to preview the selected dataset.
        st.subheader("Dataset Preview")
        if st.button("Click here to view"):
            st.dataframe(df.head())
    else:  # Provide an option for users to upload their own dataset.
        upload = st.sidebar.file_uploader("Note: the last column in the dataset is automatically set as the target variable", type=["csv"])  # Create a CSV uploader in the sidebar and store input as 'upload'.
        if upload is not None:
            df = pd.read_csv(upload)  # Create a DataFrame.
            # Create a button to preview the uploaded dataset.
            st.subheader("Dataset Preview")
            if st.button("Click here to view"):
                st.dataframe(df.head())
        else:  # Guardrail pauses the rest of the app from running if no file is uploaded.
            st.warning("Please upload a CSV file to proceed.")
            st.stop()
    
    

# Step 4: Build a K-Nearest Neighbors (KNN) model using the chosen dataset.
    # Create a list of features and designate the last column as the target variable.
    features = df.columns.tolist()
    target = df.columns[-1]

    # Create 'X' and 'y' for model training.
    X = df.drop(columns=[target])  # Contains all features except the target variable.
    y = df[target]  # Contains only the target variable.

    # Splilt the dataset for training and testing.
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,  # 80% of data is used to fit the model, 20% of data is used to evaluate the model.
                                                        random_state=42)  # Ensures reproducibility of results.

    # Scale the features for better performance.
    # Scaling standardizes features for KNN, ensuring that all contribute equally to distance calculations.
    scaler = StandardScaler() 
    
    # Fit the scaler on the training data, and transform training and test data.
    # Scale after splitting to prevent data leakage and ensure the model is evaluated on unseen data.
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Set up interactive parameters for KNN in the sidebar
    st.sidebar.subheader("Select Parameters")
    k = st.sidebar.slider("Number of Neighbors (k)", 1, 25, 5)  # Slider selects k values between 1 and 25, with a default k=5.
    weights = st.sidebar.radio("Weight Function", ("uniform", "distance"))  # Select a weight function: "uniform" or "distance".
    metric = st.sidebar.radio("Distance Metric", ("euclidean", "manhattan", "cosine"))  # Select a distance metric: "euclidean", "manhattan", or "cosine".

    # Train the KNN model using selected parameters.
    knn = KNeighborsClassifier(n_neighbors=k, weights=weights, metric=metric)  # Uses selected parameters.
    knn.fit(X_train, y_train)  # Fits KNN model to the training data.
    y_pred = knn.predict(X_test) # Predicts labels for the test dataset.



# Step 5: Build tab 2 (continued).
# This interactive visualization allows users to select features for the x and y axes and observe patterns in the data. Though users cannot visualize every feature at once, this feature allows them to understand how feature similarity relates to class similarity.
    st.subheader("Feature Visualization")
    st.markdown("Select features to visualize how data points cluster based on feature similarity and class labels.")
    features = X.columns.tolist()  # Creates a list of features (excluding the target variable) for users to select.
    
    x_axis = st.selectbox("X-axis feature", features, index=0)  # Create dropdowns to select x- and y-axis features.
    y_axis = st.selectbox("Y-axis feature", features, index=1)
    
    # If there are at least two features to plot, create a scatter plot using selected features, with points colored by class label.
    if len(features) >= 2:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=df, x=x_axis, y=y_axis, hue=target, palette="muted", ax=ax)
        plt.title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig)
    else:  # Guardrail if the dataset does not have enough features to visualize.
        st.warning("This dataset requires at least two features for visualization.") 



# Step 6: Build tab 3
# Allow viewers to evaluate the performance of the KNN model with different performance metrics.
with tab3:
    st.header("Evaluate the KNN Model")
    st.markdown(f"KNN performance with the **{data_options}** dataset using **k={k}**, a **{weights}** weight function, and the **{metric}** distance metric.")  # Displays the selected parameters.
    st.subheader("Performance Metrics")
    
    # Create a dropdown that allows users to choose an evaluation metric.
    eval_metric = st.selectbox(
        "Select an evaluation metric to display",
        ("Accuracy", "Confusion Matrix", "Classification Report"))
    
    # Calculate and display the selected metric.
    # Calculate accuracy by comparing true 'y_test' labels to predicted 'y_pred' labels.
    if eval_metric == "Accuracy":
        # Define accuracy
        st.subheader("Accuracy Score")
        st.markdown("Accuracy is the proportion of correct predictions out of all predictions made. It is a popular evaluation metric when classes are balanced and the costs of false positives and false negatives are similar. A greater accuracy score indicates better model performance.")
        accuracy = accuracy_score(y_test, y_pred) # Calulates accuracy score.
        st.write(f"**Current Model Accuracy = {accuracy:.2f}**")
        # Create a plot showing accuracy vs. number of neighbors (k) to help users visualize how k influences model performance within the chosen dataset.
        k_values = range(1, 26, 2)  # Defines range of k values (odd numbers only to avoid ties).
        accuracies = [] 
        for k in k_values:  # Loops through each k, fits KNN model, and calculates accuracy.
            knn_temp = KNeighborsClassifier(n_neighbors=k, weights=weights, metric=metric)
            knn_temp.fit(X_train, y_train)
            y_temp_pred = knn_temp.predict(X_test)
            accuracies.append(accuracy_score(y_test, y_temp_pred))  # Stores accuracy for each k in 'accuracies' list.
        # Display plot.
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(k_values, accuracies, marker="o")
        ax.set_title("Accuracy vs. Number of Neighbors (k)")
        ax.set_xlabel("Number of Neighbors (k)")
        ax.set_ylabel("Accuracy")
        ax.set_xticks(k_values)
        st.pyplot(fig)
    # Create a confusion matrix to show counts of true positives, true negatives, false positives, and false negatives.
    elif eval_metric == "Confusion Matrix":
        st.subheader("Confusion Matrix")
        st.markdown("A confusion matrix shows the counts of true positives, true negatives, false positives, and false negatives. It provides more detailed information about model performance than accuracy alone and is especially useful for understanding different types of error.")
        # st.markdown("**Confusion Matrix**")
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.title("KNN Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        st.pyplot(plt)
        # Key
        confusion_defs = {"Predicted 0": {"Actual 0": "True Negative (TN)", "Actual 1": "False Negative (FN)"},
                          "Predicted 1": {"Actual 0": "False Positive (FP)", "Actual 1": "True Positive (TP)"}}
        df_defs = pd.DataFrame(confusion_defs)
        st.write("**Confusion Matrix Key**")
        st.table(df_defs)

    # Generate a classification report to display precision, recall, f1-score, and support for each class and for overall model performance.
    elif eval_metric == "Classification Report":
        st.subheader("Classification Report")
        st.markdown("A classification report calculates precision, recall, f1-score, and support for each class and for as overall model performance. It helps evaluate how well the model performs across different classes and can reveal consistencies or discrepancies.")
        st.markdown("**Classification Report**")
        cr = classification_report(y_test, y_pred)
        st.code(cr, language=None) # Displays classification report as plain text within a code block.
        # Key
        st.write("**Classification Report Key**")
        st.write("- **Precision**: The proportion of true positives out of all predicted positives. It measures the accuracy of positive predictions.")
        st.write("- **Recall**: The proportion of true positives out of all actual positives. It measures the model's ability to identify positive cases.")
        st.write("- **F1-Score**: The harmonic mean of precision and recall, which balances both metrics.")
        st.write("- **Support**: The number of actual occurrences of each class in the test set.")