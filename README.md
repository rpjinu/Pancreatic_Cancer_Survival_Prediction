# Pancreatic_Cancer_Survival_Prediction
"Pancreatic Cancer Survival Prediction: A machine learning-based API and Streamlit web app for predicting survival outcomes, using SMOTE-balanced data and deployed for real-time inference." 🚀

<img src="https://github.com/rpjinu/Pancreatic_Cancer_Survival_Prediction/blob/main/project_imge.png">

# 🏥 Pancreatic Cancer Survival Prediction

## 📌 Project Overview
This project predicts **pancreatic cancer survival** using **machine learning**. The model is trained on a dataset containing various patient attributes, such as age, lifestyle, medical history, and treatment details. The final deployment is done using **Streamlit** via an interactive web interface.

## 🛠️ Tech Stack
- **Python** 🐍
- **Pandas & NumPy** 📊
- **Scikit-learn** 🤖
- **Joblib** 📦 (For model saving & loading)
- **Streamlit** 🌐 (For API & UI)
- **Git & GitHub** 🛠️

## 📂 Project Structure
```
Pancreatic_Cancer_Survival_Prediction/
│── .gitattributes             # Git LFS tracking file
│── Best_model.pkl             # Trained ML model
│── label_encoders.pkl         # Encoded categorical data mappings
│── app.py                     # Streamlit application
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation
└── dataset/
    ├── final_dataset.csv       # Preprocessed dataset
```

## 🚀 Features
- **Preprocessed & Feature-Selected Dataset** 📊
- **Label Encoding for Categorical Data** 🔠
- **SMOTE for Handling Imbalanced Data** ⚖️
- **ML Model Selection via Accuracy Comparison** 🎯
- **Deployment via Streamlit** 🖥️

## 📜 Dataset Overview
The dataset contains the following **features**:

| Feature Name              | Description |
|---------------------------|-------------|
| Age                       | Patient's age |
| Gender                    | Male (1) / Female (0) |
| Smoking                   | Smoker (1) / Non-Smoker (0) |
| Obesity                   | Obese (1) / Not Obese (0) |
| Abdominal_Discomfort      | Yes (1) / No (0) |
| Back_Pain                 | Yes (1) / No (0) |
| Weight_Loss               | Yes (1) / No (0) |
| Diabets_Type2             | Yes (1) / No (0) |
| Stage_at_Diagnosis        | Categorical (Encoded) |
| Treatment_Type            | Categorical (Encoded) |
| Alcohol_Consumption       | Low/Medium/High (Encoded) |
| Physical_Activity_Level   | Low/Medium/High (Encoded) |
| Diet                      | Low/Medium/High (Encoded) |
| Access_to_Healthcare      | Low/Medium/High (Encoded) |

## 🎯 Machine Learning Workflow
1. **Data Preprocessing** 🧹
   - Handle missing values
   - Encode categorical variables
   - Balance dataset using **SMOTE**
2. **Feature Selection** 🔍
   - Choose top 15 most relevant features
3. **Model Selection** 🏆
   - Train multiple classifiers in a loop
   - Select the best model based on accuracy
4. **Model Deployment** 🚀
   - Save the model using `joblib`
   - Deploy using `streamlit`

## 🔥 Streamlit API (app.py)
### **User Input via Web Interface**
- User enters **age, lifestyle, medical conditions, and treatment details**
- Categorical data is **label-encoded** automatically
- ML model predicts **survival status** ✅

### **Run Locally** 🏠
```sh
pip install -r requirements.txt
streamlit run app.py
```

## 📝 How to Use Git LFS for Model Files
```sh
git lfs track "*.pkl"
git add .gitattributes Best_model.pkl label_encoders.pkl
git commit -m "Added model files using LFS"
git push origin main
```

## 📸 Screenshots
🚧 (apt deploy image)
<img src="">
<img src="">



