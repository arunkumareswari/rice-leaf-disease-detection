# 🌾 Rice Leaf Disease Detection

This project aims to detect diseases in rice leaves using machine learning techniques. The best-performing model is deployed using Streamlit for easy interaction.

## 📁 Dataset
- Source: [Rice Leaf Diseases | Kaggle](https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases)
- Classes:
  - Bacterial leaf blight
  - Brown spot
  - Leaf smut

## 🧠 Models Used
- SVM (with GridSearchCV optimization) ✅ Best Performing
- Decision Tree Classifier
- Random Forest Classifier

## 🧪 Preprocessing
- Convert to grayscale
- Resize to 28x28 pixels
- Normalize pixel values (0-1)

## 📊 Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report
- Pie chart of prediction distribution

## 💡 Deployment
- Built using Streamlit
- Upload an image to get real-time disease prediction

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/rice-leaf-disease-detection.git
cd rice-leaf-disease-detection
