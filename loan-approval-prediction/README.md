# Loan Approval Prediction Model

## Overview
This project predicts **loan approval status** based on applicant financial and demographic details. It covers data preprocessing, handling class imbalance, training, and evaluating machine learning models.

## Dataset
The dataset contains the following columns:

`loan_id`, `no_of_dependents`, `education`, `self_employed`, `income_annum`,  
`loan_amount`, `loan_term`, `cibil_score`, `residential_assets_value`,  
`commercial_assets_value`, `luxury_assets_value`, `bank_asset_value`,  
`loan_status`

## Project Workflow

### 1. Data Exploration
- Inspected dataset structure and identified missing values.
- Found imbalance in the target variable `loan_status`.

### 2. Handling Imbalance
Used oversampling to balance the dataset:

```python
oversampled_df = oversampled_df.groupby('loan_status').apply(
    lambda x: x.sample(max_class_size, replace=True, random_state=42)
).reset_index(drop=True)
```


### 3. Data Preprocessing

Encoding:

Applied LabelEncoder on categorical variables (education, self_employed).

Encoded the target variable loan_status.

Scaling:

Applied StandardScaler on numerical columns for normalization.


### 4. Model Training

Trained a Random Forest Classifier, LogisticRegression models

Evaluated the model using:

- Accuracy

- Precision

- Recall

- F1-Score


## Results

Oversampling improved recall and F1-score for the minority class.

Random Forest provided balanced performance across all metrics.


## Key Insights

Balancing the dataset improved prediction reliability.

Feature scaling and encoding improved model performance.

Random Forest handled feature interactions effectively.


## Next Steps

Test alternative models like XGBoost or Logistic Regression.

Apply cross-validation for robustness.

Build a prediction API or interface using the saved model.
