# Customer Segmentation using KMeans

## Project Overview
This project applies **KMeans clustering** to segment customers into distinct groups based on their features. The objective is to explore customer data, preprocess it, and identify meaningful clusters for further analysis.

## Dataset
The dataset contains customer-related features such as demographics and spending behavior.  
Before modeling, the following preprocessing steps were applied:
- Handled missing values (if any).
- Scaled numerical features using `StandardScaler`.
- Removed non-numerical columns such as dates.

## Methodology
1. **Exploratory Data Analysis (EDA)**
   - Checked dataset shape, missing values, and datatypes.
   - Examined distributions and correlations.
   - Verified feature scales before clustering.

2. **Preprocessing**
   - Selected numerical features relevant for clustering.
   - Standardized features to zero mean and unit variance.

3. **Clustering with KMeans**
   - Applied KMeans with varying `k` values to identify optimal clusters.
   - Evaluated models using:
     - **Elbow Method**: Examined inertia (within-cluster sum of squares).
     - **Silhouette Score**: Measured cohesion and separation between clusters.
   - Compared results for `k=4` and `k=5`.

## Results
### Elbow Method
The elbow plot showed a sharp drop in inertia between `k=2` and `k=4`, then diminishing returns beyond `k=5`. This indicated that `k=4` or `k=5` are good candidates.

![Elbow Plot](plots\elbow_method.png)

### Silhouette Analysis
- **k=4**: Produced a balanced silhouette distribution with an average score around **X.XX**.
- **k=5**: Produced slightly lower silhouette stability with an average score around **Y.YY**.

![Silhouette Plot](plots\silhouette.png)

Based on these metrics, **k=4 clusters** was selected as the final model.

### Final Model
- Implemented KMeans with `k=4`.
- Assigned each customer to one of the 4 clusters.
- Cluster labels were added back to the dataset for downstream analysis.
