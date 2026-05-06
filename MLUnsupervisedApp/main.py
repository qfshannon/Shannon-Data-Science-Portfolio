# This Streamlit app allows users to select a dataset and explore how different parameters influence the performance of a K-means clustering machine learning model.

# Step 0: Import libraries used to build the app, handle data, build the KNN model, and visualize and evaluate its performance
import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# Step 1: Initial app setup
# Add page configuration, title, description, sidebar, and tabs
st.set_page_config(page_title = "K-Means Clustering ML Explorer", page_icon = "🌐")
st.title("K-Means Clustering Machine Learning Explorer 🌐")
st.markdown("Welcome to the K-Means Clustering Machine Learning Explorer! This app allows you to explore how different parameters influence the performance of a K-Means Clustering machine learning model. Use the sidebar to choose a dataset and get started!")

st.sidebar.header("Select a Dataset")
# Dropdown allows users to select a built-in dataset to explore or upload their own dataset in CSV format
data_options = st.sidebar.selectbox("Choose a Dataset",
                                    ("Iris", "Penguins", "Heart Disease", "Upload a CSV file"))

tab1, tab2, tab3 = st.tabs(["Model Overview 🔎", "Data Visualization 💡", "Model Evaluation ⚖️"])


# Step 2: Build tab 1
# Tab 1 provides an overview of K-Means Clustering and defines key parameters
with tab1:
    # Define K-Means Clustering and its purpose as an unsupervised machine learning model
    st.subheader("What is K-Means Clustering?")
    st.markdown("K-Means Clustering is a simple machine learning model that used for **unsupervised learning** tasks where the goal is to **identify structure**, **group observations**, or **uncover hidden patterns** in unlabeled data.")
    st.markdown("K-Means Clustering is based on the idea that similar data points in the feature space share similar characteristics.")
    
    # Define key parameters of K-Means Clustering and state how they influence the model's performance
    st.subheader("Key Parameters of K-Means Clustering")
    
    # Implement a select box that allow users to learn about one parameter at a time
    # These parameters were thoughtfully selected as interactive app features because they address primary aspects of cluster selection
    # Understanding how each parameter affects the model will help inform users' decisions and equip them to optimize K-Means Clustering model performance
    parameter = st.selectbox("Select a parameter from the dropdown to learn how it influences the K-Means Clustering model.", ("n_clusters", "init", "n_init", "max_iter", "algorithm"))
    if parameter == "n_clusters":
        st.markdown("**Number of clusters (k)** sets *k* initial centroids, which designates the number of points in the feature space that serve as initial guesses or cluster centers.")
        st.markdown("Choosing the right *k* is pivotal for model performance and can be guided by techniques such as the elbow method or silhouette score.")
    elif parameter == "init":
        st.markdown("**Initialization** determines the method by which initial cluster centroids are chosen. The initialization method can significantly impact the convergence speed and final clustering result.")
        st.markdown("**k-means++**: selects initial cluster centroids using sampling based on an empirical probability distribution of the points’ contribution to the overall inertia. This technique makes several trials at each sampling step and chooses the best centroid among them.")
        st.markdown("**random**: chooses n_clusters observations (rows) at random from data for the initial centroids.")
    elif parameter == "n_init":
        st.markdown("**Number of initializations** sets the number of times the k-means algorithm will be run with different centroid seeds. The final results will be the best output from these runs.")
    elif parameter == "max_iter":
        st.markdown("**Maximum iterations** sets the maximum number of iterations of the k-means algorithm for a single run. This parameter helps control the computational demand and prevents infinite loops.")
    elif parameter == "algorithm":
        st.markdown("**Algorithm** specifies the algorithm to use when computing the k-means clustering. The choice of algorithm can affect the speed and quality of the clustering results.")
        st.markdown("**lloyd**: uses the standard k-means algorithm, which iteratively assigns data points to the nearest cluster centroid and then updates the centroids based on the mean of the assigned points.")
        st.markdown("**elkan**: uses the Elkan variant of k-means, which can be faster on certain datasets by using triangle inequality to reduce the number of distance calculations.")

    # Define performance metrics used to evaluate K-means Clustering models
    st.subheader("Performance Metrics")
    # Create a dictionary to store evaluation metrics and their definitions
    evals = {"Evaluation Metric": ["Silhouette Score", "Elbow Method"],
             "Definition": ["Measures how similar an object is to its own cluster compared to other clusters. It ranges from -1 to 1, where a higher score indicates better-defined clusters.",
                            "A graphical approach to determine the optimal number of clusters by plotting the within-cluster sum of squares (WCSS) against the number of clusters (k)."]
    }
    # Display the dictionary as a dataframe in Streamlit
    df_metrics = pd.DataFrame(evals)
    st.dataframe(df_metrics, hide_index = True)  # Hide the index column for a cleaner display
    

# Step 3: Build tab 2
# Tab 2 allows users to visualize the selected dataset and explore relationships between features
with tab2:
    st.subheader("Data Visualization")
    st.markdown("Visualizing the dataset helps aid understanding of the underlying structure and relationships between features. Use the options below to explore different visualizations.")
    
    # Load and clean each dataset, and identify its target variable and features
    if data_options == "Iris":
        st.subheader("Iris Dataset")
        df = sns.load_dataset("iris")  # Load Iris dataset from seaborn library
        df.dropna(inplace=True)  # Drop rows with missing values to clean data
        st.dataframe(df.head())  # Preview the original dataset
        features = df.columns.tolist()  # Designate the "species" column as the target variable and the rest as features
        target = df.columns[-1]
    
    elif data_options == "Penguins":
        st.subheader("Penguins Dataset")
        df = sns.load_dataset("penguins")  # Load Penguins dataset from seaborn library
        df.dropna(inplace=True)  # Drop rows with missing values to clean data
        st.dataframe(df.head())  # Preview the original dataset
        features = df.columns.tolist()
        target = df.columns[0]  # Designate the "species" column as the target variable and the rest as features
        island_map = {"Torgersen": 0, "Biscoe": 1, "Dream": 2}  # Map island names and sex to numeric values since clustering requires numerical input
        df['island'] = df['island'].map(island_map)
        sex_map = {"Male": 0, "Female": 1}
        df['sex'] = df['sex'].map(sex_map)
    
    elif data_options == "Heart Disease":
        st.subheader("Heart Disease Dataset")
        df = pd.read_csv("data/heart.csv")  # Load Heart Disease dataset from local CSV file
        df["condition"] = df["target"].map({0: "No Disease", 1: "Disease"})
        df.drop(columns = ["target"], inplace = True)
        st.dataframe(df.head())  # Preview the dataset
        # Designate the "condition" column as the target variable and the rest as features
        features = df.columns.tolist()
        target = df.columns[-1]
    
    elif data_options == "Upload a CSV file":
        upload = st.sidebar.file_uploader("",type=["csv"])  # Add dropbox for users to upload their own CSV file
        if upload is not None:
            st.subheader(f"Your '{upload.name}' Dataset")
            df = pd.read_csv(upload)
            st.dataframe(df.head())  # Preview the original dataset
            features = df.columns.tolist()
            target = df.columns[-1]  # Designate the last column as the target variable, assuming it is the label
        else:
            st.subheader("**Upload a CSV file to Visualize Your Own Dataset**")
            st.markdown("The last column will be treated as the target variable for clustering, and the rest will be treated as features. Make sure your dataset is clean and properly formatted for optimal results.")  # Prompt users to ensure their CSV file is properly formatted for the model
            st.warning("Please upload a CSV file to proceed.")
            st.stop()  # Guardrail pauses the rest of the app from running if no file is uploaded


# Step 3.1: Build an interactive visualization that allows users to select features for the x and y axes to observe patterns in the data based on selected features
    # Though users cannot visualize every feature at once, this feature allows them to understand how feature similarity relates to class similarity, which is the basis for K-Means Clustering
    st.subheader("Feature Visualization")
    st.markdown("Plot features to observe how data points cluster based on feature similarity and class labels.")
    
    # Create dropdowns to select x- and y-axis features for a scatter plot
    x_axis = st.selectbox("X-axis feature", features, index = 0)
    y_axis = st.selectbox("Y-axis feature", features, index = 1)
    
    # Create the scatter plot using selected features, with points colored by target label
    if len(features) >= 2:  # The dataset must have at least two features to create a scatter plot
        fig, ax = plt.subplots(figsize = (8, 5))
        sns.scatterplot(data = df, x = x_axis, y = y_axis, hue = target, palette = "muted", ax = ax)
        plt.title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig)
    else:  # Guardrail displays a warning if the dataset does not have at least two features to visualize
        st.warning("This dataset requires at least two features for visualization.") 


# Step 4: Finish setting up sidebar once dataset has been selected and cleaned, and key parameters have been defined
st.sidebar.header("Adjust Parameters")
st.sidebar.markdown("**n_clusters**")
k = st.sidebar.slider("", 2, 10, 2)  # Slider selects k values between 2 and 10, with a default k=2 (all defaults set to minimum values to encourage users to experiment with parameter settings)
st.sidebar.markdown("**init**")
init = st.sidebar.radio("", ("k-means++", "random"))  # Select "k-means++" or "random" for initialization method
st.sidebar.markdown("**n_init**")
n_init = st.sidebar.slider("", 1, 100, 1)  # Slider selects number of initializations between 1 and 100, with a default n_init=1
st.sidebar.markdown("**max_iter**")
max_iter = st.sidebar.slider("", 1, 30, 1)  # Slider selects maximum iterations between 1 and 30, with a default max_iter=1
st.sidebar.markdown("**algorithm**")
algorithm = st.sidebar.radio("", ("lloyd", "elkan"))  # Select "lloyd" or "elkan" for algorithm


# Step 5: Build tab 3
# Tab 3 builds a K-Means Clustering unsupervised machine learning model using the selected dataset and parameters
with tab3: 
    X = df.drop(columns = [target])  # Designate features as X and drop the target variable column from the dataframe; K-Means Clustering is an unsupervised learning model, so it should not use labels for training
    feature_names = X.columns.tolist()
    
    # Center and scale the features since clustering is sensitive to the variable scales; this ensures that all features contribute equally to distance calculations
    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)

    # Compute clustering using the user's parameter selections
    kmeans = KMeans(n_clusters = k, init = init, n_init = n_init, max_iter = max_iter, algorithm = algorithm, random_state = 42)
    clusters = kmeans.fit_predict(X_std)


# Step 5.1: Visualize K-Means Clustering Results
# Visualization allows users to observe how well KMeans grouped the data
    st.header("Visualize K-Means Clustering Model Output")
    # Use PCA to reduce multidimentional datasets to 2 dimensions to facilitate visualization
    pca = PCA(n_components = 2)
    X_pca = pca.fit_transform(X_std)
    plt.figure(figsize = (10, 6))
    sns.scatterplot(x = X_pca[:, 0], y = X_pca[:, 1], hue = clusters, palette = "Set2", s = 100, alpha = 0.7)  # Plot PCA scores, colored by cluster assignment
    plt.title("K-Means Clustering Results (PCA Visualization)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend(title="Cluster")
    st.pyplot(plt) 


# Step 5.2: Define evaluation metrics used for K-Means Clustering Model performance
    from sklearn.metrics import silhouette_score
    silhouette = silhouette_score(X_std, clusters)
    st.subheader("**Silhouette Score**: {:.2f}%".format(silhouette_score(X_std, clusters) * 100))


# Step 5.3: Plot the elbow method graph and silhouette scores for a range of k values to help users understand how to choose the optimal number of clusters.
    st.header("Choosing the Optimal Number of Clusters (k)")
    st.markdown("To determine the optimal number of clusters (k), we can use the elbow method and silhouette scores. The elbow method helps identify the point where adding more clusters does not significantly improve the model, while silhouette scores provide insight into the quality of the clustering.")
    
    st.markdown("Click the button below to visualize the elbow method and silhouette score graphs for a range of k values.")  # Button allows users to choose when to reveal information relevant to optimal cluster selection, giving users the chance to experiment with parameters and learn firsthand how they influence model performance
    if st.button("Visualize Elbow Method and Silhouette Scores"):
        st.markdown("Use both methods together when considering an optimal k value. A high silhouette score with a clear elbow provides the most robust choice for optimal k.")

        # Define the range of k values to try
        ks = range(2, 11)  # Starting from 2 clusters to 10 clusters
        wcss = []  # Within-Cluster Sum of Squares for each k
        silhouette_scores = []  # Silhouette scores for each k
        
        # Loop over the range of k values
        for k in ks:
            km = KMeans(n_clusters=k, random_state=42)
            km.fit(X_std)
            wcss.append(km.inertia_)  # Inertia: sum of squared distances within clusters
            labels = km.labels_
            silhouette_scores.append(silhouette_score(X_std, labels))

        # Plot the Elbow Method graph
        plt.figure(figsize = (12, 5))
        plt.subplot(1, 2, 1)  # Prepare to display the two plots side-by-side, placing the Elbow Method graph on the left
        plt.plot(ks, wcss, marker = 'o')
        plt.title('Elbow Method for Optimal k')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
        plt.xticks(ks)
        plt.grid()
        
        # Plot the Silhouette Scores graph
        plt.subplot(1, 2, 2) # Prepare to display the two plots side-by-side, placing the Silhouette Scores graph on the right
        plt.plot(ks, silhouette_scores, marker = 'o')
        plt.title('Silhouette Scores for Optimal k')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Silhouette Score')
        plt.xticks(ks)
        plt.grid()
        st.pyplot(plt)