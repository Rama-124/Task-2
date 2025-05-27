# 🧼 Titanic Exploratory Data Analysis & Cleaning

## 📌 About the Task

This task involved performing **Exploratory Data Analysis (EDA)** and **data cleaning** on the Titanic dataset. The objective was to understand the structure and characteristics of the data, clean and preprocess it, and generate meaningful visual insights before applying machine learning techniques.

---

## ⏳ Time Frame

✅ Completed within the scheduled internship window:  
**🕙 10:00 AM – 10:00 PM (Same Day)**

---

## 🧠 What I Learned

- How to perform **EDA using Pandas, Matplotlib, Seaborn, and Plotly**
- Handling missing values using **median** and **mode**
- **Boxplot and histogram analysis** for outlier detection
- Feature transformation using **label encoding** and **one-hot encoding**
- **Scaling numeric features** using `StandardScaler`
- Calculating and visualizing **correlation** and feature relationships
- Identifying **skewness** and potential multicollinearity

---

## 🛠 Tools and Libraries Used

- Python 🐍
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/python/) (optional for interactive plots)
- [Scikit-learn](https://scikit-learn.org/)

---

## 📁 Dataset Information

- Dataset: [Titanic Dataset – by Yasserh](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- File used: `titanic.csv`
- Source: Kaggle

---

## 🔧 What I Did

1. **Loaded the dataset** using Pandas and explored the first few rows.
2. Checked for **null values** using `isnull().sum()` and visual inspection.
3. Filled missing values:
   - Replaced missing values in `Age` with **median**
   - Replaced missing values in `Embarked` with **mode**
4. Dropped columns:
   - `Cabin` due to high percentage of missing values
   - `Name` and `Ticket` due to low predictive value
5. Converted categorical values:
   - Used **label encoding** and **one-hot encoding** for `Sex` and `Embarked`
6. Detected and removed **outliers** in `Age` and `Fare` using **boxplots** and **IQR method**
7. **Standardized numeric columns** using `StandardScaler`
8. Created visualizations:
   - Histograms and boxplots for distribution and outliers
   - Heatmaps and pairplots for feature relationships
   - KDE plots and count plots for survival analysis

---

## 📊 Key Visual Insights

- **Higher survival rates** among females and first-class passengers
- Most passengers were between **20–40 years**
- `Fare` had a **long right tail** (positive skew)
- `Age` and `Fare` showed several outliers

---

## 📸 Screenshots (Optional)

You can add screenshots of:
- Heatmaps
- Pairplots
- Boxplots for `Age` and `Fare`
- KDE plots for survival comparison by age

---

## ✅ Final Output

- Cleaned and transformed dataset ready for ML modeling
- Code structured and reusable
- Insights documented and visualized clearly

---

## 📦 How to Run the Code

1. Make sure you have Python installed.
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn plotly


## Screenshots
![alt text](<Screenshot 2025-05-27 185523.png>)
![alt text](<Screenshot 2025-05-27 185546.png>)