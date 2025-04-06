# 🌾 Rice Leaf Disease Detection using Machine Learning

![rice-leaf](https://img.shields.io/badge/Streamlit-Deployed-green?style=flat-square)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-Dataset-blue?style=flat-square)](https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases)
[![Live App](https://img.shields.io/badge/Live_App-Click_Here-brightgreen?style=flat-square)](https://rice-leaf-disease-detection.streamlit.app/)

A mini project to detect rice leaf diseases using image classification. This project uses machine learning algorithms to identify three types of rice leaf diseases from images.

---

## 📂 Dataset

- **Source**: [Kaggle - Rice Leaf Diseases Dataset](https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases)
- **Classes**:
  - Bacterial Leaf Blight
  - Brown Spot
  - Leaf Smut

---

## 🔧 Technologies Used

- **Language**: Python  
- **Libraries**: OpenCV, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Web App**: Streamlit  
- **Model Deployment**: Streamlit Cloud

---

## 🎯 Project Workflow

1. **Image Preprocessing**  
   - Convert image to grayscale  
   - Resize to 28x28  
   - Normalize pixel values  

2. **Model Training (Jupyter Notebook)**  
   - Used three classifiers:  
     - Support Vector Machine (SVM)  
     - Decision Tree Classifier  
     - Random Forest Classifier  
   - GridSearchCV for hyperparameter tuning  
   - Performance evaluation using:
     - Accuracy
     - Classification Report
     - Confusion Matrix

3. **Model Deployment (Streamlit)**  
   - The best model (SVM) is saved using `joblib`  
   - Real-time image upload and disease prediction using Streamlit UI

---

## 🖥️ Live App

Click here to try the deployed app:  
👉 [https://rice-leaf-disease-detection.streamlit.app/](https://rice-leaf-disease-detection.streamlit.app/)

---

## 📁 Project Structure

