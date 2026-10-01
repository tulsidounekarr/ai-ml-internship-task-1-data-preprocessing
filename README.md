# AI \& ML Internship – Task 1



## Data Cleaning \& Preprocessing



## 1. Objective



The objective of this task was to clean and prepare a raw dataset for machine learning.



The Titanic dataset was used to perform missing-value handling, categorical encoding, feature scaling, and outlier detection and removal.



## 2. Tools Used



- Python 3.13.5

- Pandas 2.2.3

- NumPy 1.26.4

- Matplotlib 3.10.0

- Scikit-learn 1.6.1



## 3. Dataset



Dataset: Titanic Dataset



Original dataset shape:



- 891 rows

- 12 columns



Original columns:



- PassengerId

- Survived

- Pclass

- Name

- Sex

- Age

- SibSp

- Parch

- Ticket

- Fare

- Cabin

- Embarked



## 4. Data Exploration



The dataset was inspected for:



- Number of rows and columns

- Column names

- Data types

- Missing values

- Basic dataset information



Missing values found:



| Column | Missing Values |

|---|---:|

| Age | 177 |

| Cabin | 687 |

| Embarked | 2 |



## 5. Missing Value Handling



The following methods were used:



- `Age` → median imputation

- `Embarked` → mode imputation

- `Cabin` → replaced missing values with `Unknown`



After cleaning, there were no missing values.



## 6. Categorical Encoding



Categorical features were converted into numerical form using one-hot encoding.



The `Cabin` column was simplified into a `Deck` feature using the first character of the cabin value.



Examples:



- `C85` → `C`

- `B96` → `B`

- Missing cabin → `U`



The original `Name`, `Ticket`, and `Cabin` columns were removed from the modeling dataset.



Encoded features included:



- `Sex\_male`

- `Embarked\_Q`

- `Embarked\_S`

- `Deck\_B`

- `Deck\_C`

- `Deck\_D`

- `Deck\_E`

- `Deck\_F`

- `Deck\_G`

- `Deck\_T`

- `Deck\_U`



## 7. Outlier Detection and Removal



Outliers were visualized using boxplots.



The IQR (Interquartile Range) method was used on:



- `Age`

- `Fare`



Results:



- Original rows: 891

- Outlier rows removed: 170

- Rows after outlier removal: 721



The following boxplots were generated:



- `boxplots\_before\_outliers.png`

- `boxplots\_after\_outliers.png`



## 8. Feature Standardization



The following numerical features were standardized using `StandardScaler`:



- `Age`

- `Fare`

- `SibSp`

- `Parch`

- `Pclass`



After standardization, the means of these features were approximately zero.



## 9. Final Dataset



The final preprocessed dataset is:



`titanic\_preprocessed.csv`



Final dataset shape:



- 721 rows

- 18 columns



Final checks:



- Missing values: 0

- Categorical features converted to numerical values

- Numerical features standardized



## 10. Project Structure



Task-1/

│

├── README.md

│

├── code/

│   ├── data\_exploration.py

│   ├── data\_cleaning.py

│   ├── encoding.py

│   ├── outlier\_handling.py

│   └── scaling.py

│

├── data/

│   ├── titanic.csv

│   ├── titanic\_cleaned.csv

│   ├── titanic\_encoded.csv

│   ├── titanic\_outlier\_cleaned.csv

│   └── titanic\_preprocessed.csv

│

└── outputs/

&#x20;   ├── boxplots\_before\_outliers.png

&#x20;   └── boxplots\_after\_outliers.png



## 11. Conclusion



This task provided practical experience in data cleaning and preprocessing for machine learning.



The Titanic dataset was explored, missing values were handled, categorical variables were encoded, numerical features were standardized, and outliers were visualized and removed.



