# 🌾 Harvestify — Crop & Disease Predictor
🚀 **Live Demo:** [https://harvestify-crop-disease.onrender.com](https://harvestify-crop-and-disease-predictor.onrender.com)  

Harvestify is a machine learning–based web application that helps users:
- 🌱 Recommend the best crop to grow based on soil and environmental parameters
- 🦠 Detect plant diseases from leaf images

The application is built using Flask and ML models trained on agricultural datasets.

---

## 🚀 Features

- Crop Recommendation System
- Plant Disease Detection using Image Processing
- User-friendly Web Interface
- ML Model Integration
- Easy Local & Cloud Deployment

---

## 🗂️ Project Structure

Harvestify-Crop-and-Disease-Predictor/
│
├── app.py                  # Main Flask application

├── train_model.py          # ML model training script

├── models/                 # Saved trained models

├── static/                 # CSS, JS, images

├── templates/              # HTML templates

├── requirements.txt        # Project dependencies

├── README.md               # Project documentation

└── *.jpg                   # Sample crop images

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- TensorFlow / Keras (if applicable)
- HTML, CSS, Bootstrap

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone the Repository

git clone https://github.com/Raashi1510/Harvestify-Crop-and-Disease-Predictor.git

cd Harvestify-Crop-and-Disease-Predictor

### 2️⃣ Create Virtual Environment (Optional but Recommended)

python -m venv env
env\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Train the Model (If not already trained)

python train_model.py

### 5️⃣ Run the Flask App

python app.py

### 6️⃣ Open in Browser

http://127.0.0.1:5000/

---

## 🌐 Live Deployment Links (Free Platforms)

You can deploy this project using the following platforms:

### 🔗 Render (Recommended)
https://render.com/

Steps:
- Create a new Web Service
- Connect GitHub repository
- Set build command: pip install -r requirements.txt
- Set start command: python app.py

### 🔗 Railway
https://railway.app/

### 🔗 Heroku
https://www.heroku.com/

---

## 📌 requirements.txt Example

Flask
numpy
pandas
scikit-learn
tensorflow
opencv-python
Pillow

---

## 🧪 Usage

- Enter soil values to get crop recommendation
- Upload leaf image to detect plant disease

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.


---

## 🙌 Author

Raashi Gada  
GitHub: https://github.com/Raashi1510





