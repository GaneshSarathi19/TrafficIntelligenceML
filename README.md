# Traffic Intelligence ML

## Data-Driven Traffic Analysis Using Machine Learning

A three-track Machine Learning capstone project covering **Regression, Classification, and Clustering** for traffic analysis.

The project investigates traffic volume prediction, traffic Level of Service classification, and unsupervised traffic regime discovery using three different real-world/synthetic traffic datasets.

---

## Team

| Team Member | Track |
|---|---|
| Ganesh Sarathi | Regression |
| Dayanitha B| Classification |
| Nithin Sivakumar | Clustering |


---

# 1. Project Overview

Traffic conditions are influenced by several interacting factors such as time of day, weather, road characteristics, accessibility, vehicle behaviour, and environmental conditions.

This project applies different Machine Learning approaches to analyse these patterns through three independent tracks:

1. **Regression** – Predict traffic volume using temporal, weather, and traffic-related features.
2. **Classification** – Classify urban traffic conditions into different Levels of Service.
3. **Clustering** – Discover naturally occurring traffic regimes using unsupervised learning.

The three tracks use separate datasets and are implemented as independent Machine Learning pipelines while following a common project structure and methodology.

---

# 2. Project Objectives

The major objectives of the project are:

- Perform systematic Exploratory Data Analysis (EDA).
- Clean and preprocess traffic datasets appropriately.
- Engineer meaningful features from raw data.
- Apply multiple Machine Learning algorithms.
- Compare algorithms using appropriate evaluation metrics.
- Tune selected models using cross-validation.
- Visualize model behaviour and results.
- Avoid data leakage during preprocessing and model evaluation.
- Maintain reproducible experiments using consistent train/test splits and random states.
- Develop a structured Machine Learning workflow suitable for academic evaluation and future deployment.

---

# 3. Project Tracks

| Track | Objective | Dataset | Learning Type |
|---|---|---|---|
| Regression | Predict hourly traffic volume | UCI Metro Interstate Traffic Volume | Supervised |
| Classification | Predict urban Traffic Level of Service | Causal Feature Importance Dataset for Urban Traffic Level of Service | Supervised |
| Clustering | Discover traffic congestion/regime patterns | VANET Traffic Congestion Dataset | Unsupervised |

---

# 4. Track 1 – Regression

## Problem Statement

Predict the traffic volume on an interstate highway using temporal, weather, and environmental features.

## Research Focus

The regression track investigates how temporal and environmental variables can be used to predict traffic volume and which Machine Learning algorithms are most effective at capturing the underlying nonlinear relationships.

---

## Dataset

### UCI Metro Interstate Traffic Volume

**Source:** UCI Machine Learning Repository

Dataset:
https://archive.ics.uci.edu/dataset/492/metro%2Binterstate%2Btraffic%2Bvolume

The dataset contains hourly westbound traffic volume for Interstate 94 in the Minneapolis-St Paul area.

### Dataset Information

- Instances: **48,204**
- Input features: **8**
- Target: `traffic_volume`
- Time period: **2012–2018**
- Location: **Minneapolis-St Paul, Minnesota**
- Missing values in the original dataset: **None**

### Original Features

| Feature | Description |
|---|---|
| `holiday` | Holiday information |
| `temp` | Temperature in Kelvin |
| `rain_1h` | Rainfall in the previous hour |
| `snow_1h` | Snowfall in the previous hour |
| `clouds_all` | Cloud coverage |
| `weather_main` | Main weather category |
| `weather_description` | Detailed weather description |
| `date_time` | Timestamp |
| `traffic_volume` | Hourly traffic volume – target |

---

## Regression Preprocessing

The following preprocessing steps were performed:

1. Loaded and inspected the dataset.
2. Checked data types and missing values.
3. Checked duplicate records.
4. Removed duplicate records.
5. Converted `date_time` into a datetime format.
6. Extracted temporal features.
7. Checked numerical feature distributions.
8. Checked and treated numerical outliers using IQR-based clipping.
9. Encoded categorical variables using One-Hot Encoding.
10. Standardized numerical features using `StandardScaler`.
11. Created an 80:20 train-test split.
12. Used target-based stratification to preserve the distribution of traffic volume across the split.
13. Fit preprocessing transformations only on the training data.

---

## Feature Engineering

The following features were derived from `date_time`:

- `hour`
- `day_of_week`
- `month`
- `is_weekend`
- `is_rush_hour`
- `hour_sin`
- `hour_cos`

### Rush Hour Definition

The following hours were treated as rush-hour periods:

- 07:00
- 08:00
- 09:00
- 16:00
- 17:00
- 18:00

Cyclical encoding using `hour_sin` and `hour_cos` was also used to represent the circular nature of time.

---

# 5. Regression Algorithms

All ten algorithms required by the project guidelines are implemented using the same overall preprocessed dataset and held-out test set.

### Algorithms

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. ElasticNet
5. Polynomial Regression
6. Decision Tree Regressor
7. Random Forest Regressor
8. Gradient Boosting Regressor
9. Support Vector Regression (SVR)
10. K-Nearest Neighbors Regressor

---

## Regression Evaluation Metrics

The models are evaluated using:

- **R² Score**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**

Five-fold cross-validated R² is also used for the selected top-performing models.

---

# 6. Regression Results

The following results were obtained on the held-out test set.

| Rank | Model | R² | RMSE | MAE |
|---:|---|---:|---:|---:|
| 1 | Random Forest | 0.939376 | 487.691 | 264.266 |
| 2 | Decision Tree | 0.929952 | 524.230 | 290.197 |
| 3 | Gradient Boosting | 0.919145 | 563.220 | 359.587 |
| 4 | KNN | 0.836066 | 801.971 | 523.767 |
| 5 | Lasso | 0.361201 | 1583.091 | 1368.076 |
| 6 | Ridge | 0.361191 | 1583.104 | 1368.040 |
| 7 | Linear Regression | 0.361183 | 1583.113 | 1368.056 |
| 8 | ElasticNet | 0.360341 | 1584.157 | 1370.953 |
| 9 | SVR | 0.356944 | 1588.357 | 1394.584 |
| 10 | Polynomial Regression | 0.047679 | 1932.927 | 1680.798 |

These values represent the model evaluation results currently recorded in the regression notebook.

---

## Regression Analysis

The EDA showed a strong relationship between traffic volume and time of day.

Temporal feature engineering therefore provided important information for the models.

Tree-based models were able to capture nonlinear relationships and interactions between temporal and environmental variables more effectively than the basic linear models.

The Random Forest model achieved the highest test-set R² among the implemented models.

Feature importance from the tree-based model showed that `hour` was the dominant feature, followed by features such as `day_of_week`, `is_weekend`, and `temp`.

---

## Regression Visualizations

The regression notebook includes:

- Numerical feature distribution plots
- Categorical feature distributions
- Target distribution
- Target boxplot
- Correlation heatmap
- Feature-target scatter plots
- Traffic volume over time
- Average traffic volume by hour
- Model comparison
- Predicted vs Actual plot
- Residual analysis
- Tree-based feature importance

---

## Polynomial Regression Note

Polynomial feature expansion across all 70 processed features resulted in excessive memory usage.

Therefore, polynomial expansion was restricted to the relevant numerical/engineered features before applying Polynomial Regression.

This allowed the degree comparison to be performed without creating an impractically large feature matrix.

---

# 7. Track 2 – Classification

## Problem Statement

Classify urban traffic conditions into three Levels of Service categories:

- Good
- Medium
- Poor

The classification track investigates how built environment, accessibility, safety, demographic, mode-choice, and land-use variables can be used to classify urban traffic conditions.

---

## Dataset

### Causal Feature Importance Dataset for Urban Traffic Level of Service Across Four U.S. Metropolitan Areas

**Source:** Mendeley Data

Dataset:
https://data.mendeley.com/datasets/tbdn8yhs83/3

DOI:

`10.17632/tbdn8yhs83.3`

### Dataset Information

- Version: **3**
- Published: **27 April 2026**
- Number of census blocks: **134,530**
- Cities:
  - Chicago
  - Houston
  - Los Angeles
  - New York City
- Predictor features: **46 causally upstream features**
- Classification target: `LOS_3Class`
- Additional outcome: `Congestion Index`

The predictor variables are grouped into categories including:

- Built Environment
- Accessibility / Network
- Safety & Environment
- Demographics
- Mode Choice
- Land Use

---


# 8. Classification Algorithms

The classification track contains ten algorithms required by the project guidelines.

## Part A – Review 1

1. Logistic Regression
2. K-Nearest Neighbors Classifier
3. Gaussian Naive Bayes
4. Decision Tree Classifier
5. Support Vector Machine

## Part B – Review 2

6. Random Forest Classifier
7. AdaBoost
8. Gradient Boosting Classifier
9. Bagging Classifier
10. MLP Classifier

---

## Classification Evaluation Metrics

The classification models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

For the multiclass problem, ROC-AUC is evaluated using a One-vs-Rest approach.

The final comparison will contain the required evaluation metrics for all ten classification algorithms.

---

# 9. Track 3 – Clustering

## Problem Statement

Discover naturally occurring traffic congestion regimes from traffic, vehicle, environmental, communication, and road-condition features using unsupervised Machine Learning.

The clustering track investigates whether meaningful traffic regimes can be identified without using the provided congestion labels during model training.

---

## Dataset

### VANET Traffic Congestion Dataset

**Source:** Kaggle

Dataset:
https://www.kaggle.com/datasets/ucimachinelearning/vanet-traffic-congestion-dataset

### Dataset Information

- Records: **195,714**
- Attributes: **27**
- CSV file: `vanet_traffic_data.csv`
- License: **CC0 Public Domain**

The dataset was originally published as a traffic congestion classification dataset. In this project, it is used as an **unsupervised clustering dataset**.

The provided congestion labels are not used during clustering model fitting.

---

## Major Feature Groups

The dataset contains features related to:

### Traffic Conditions

- Average speed
- Traffic density
- Average waiting time
- Occupancy
- Traffic flow
- Queue length

### Vehicle Dynamics

- Average acceleration
- Heading

### Traffic Control and Incidents

- Signal state
- Incident information

### Environmental Conditions

- Temperature
- Visibility
- Rain intensity

### VANET Communication

- Channel busy ratio
- Message rate
- Communication delay
- RSSI
- Packet loss

### Engineered Features

Examples include:

- Speed-density ratio
- Congestion pressure
- Wireless congestion intensity
- Throughput per queued vehicle
- Acceleration directionality
- Weather factor

---

# 10. Clustering Algorithms

The clustering track implements:

1. K-Means Clustering
2. Agglomerative Hierarchical Clustering

The provided congestion labels are not used during model fitting.

They may only be used afterward for interpretation or validation where appropriate.

---

## Clustering Evaluation Metrics

The clustering algorithms are evaluated using:

- Silhouette Score
- Davies-Bouldin Index
- Calinski-Harabasz Index


# 11. Common Machine Learning Workflow

Each track follows a structured Machine Learning workflow.

```text
Dataset
   ↓
Data Loading
   ↓
Dataset Audit
   ↓
Exploratory Data Analysis
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Encoding
   ↓
Train/Test Split
   ↓
Scaling / Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Hyperparameter Tuning
   ↓
Model Comparison
   ↓
Visualization
   ↓
Interpretation 
