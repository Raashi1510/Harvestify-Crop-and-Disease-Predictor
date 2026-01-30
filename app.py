from flask import Flask, render_template, request
import pickle
import requests
import os
import json

app = Flask(__name__)

# ------------------- Crop Model -------------------
model = pickle.load(open('models/crop_model.pkl', 'rb'))

# ------------------- Weather API -------------------
API_KEY = "6bb1678a4205d7244369281775d8585e"
CITY = "Mumbai"

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temperature = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        return temperature, humidity
    return None, None


# ------------------- Home -------------------
@app.route('/')
def home():
    temperature, humidity = get_weather()
    return render_template("index.html", temperature=temperature, humidity=humidity)


# ------------------- Crop Prediction -------------------
@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['nitrogen'])
    P = int(request.form['phosphorus'])
    K = int(request.form['potassium'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    temperature, humidity = get_weather()

    data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(data)[0]

    return render_template(
        "predict.html",
        prediction=prediction,
        temperature=temperature,
        humidity=humidity
    )


# ------------------- Fertilizer Form (with Soil Images) -------------------
@app.route('/fertilizer_form')
def fertilizer_form():
    return render_template("fertilizer_form.html")


# ------------------- Fertilizer Suggestion -------------------
fertilizer_dict = {
    "Clayey": "Use Urea and DAP for better nitrogen fixation.",
    "Sandy": "Use Organic manure and Compost to improve fertility.",
    "Loamy": "Balanced NPK fertilizers recommended.",
    "Black": "Potash and Zinc fertilizers are useful.",
    "Red": "Add Phosphorus fertilizers like SSP.",
}

@app.route('/fertilizer', methods=['POST'])
def fertilizer():
    soil = request.form.get('soil', '').strip()
    crop = request.form.get('crop', '').strip()
    recommendation = fertilizer_dict.get(soil.capitalize(), "General NPK fertilizer is recommended.")
    return render_template("fertilizer.html", soil=soil, crop=crop, recommendation=recommendation)


# ------------------- Disease Detection -------------------
API_KEY_PLANTID = "rfQB5Az6i1nrZhyYdSMRf8O5r6g1UV3HbhyLtht8lc8NliEFmh"

def detect_disease(image_path):
    url = "https://api.plant.id/v2/health_assessment"
    files = [("images", open(image_path, "rb"))]
    data = {"organs": ["leaf"]}
    headers = {"Api-Key": API_KEY_PLANTID}
    response = requests.post(url, headers=headers, files=files, data=data)
    result = response.json()

    if "health_assessment" in result and "diseases" in result["health_assessment"]:
        suggestions = result["health_assessment"]["diseases"]
        if suggestions:
            return suggestions[0]["name"]
    return "No disease detected"

@app.route('/disease', methods=['POST'])
def disease():
    crop = request.form['crop']
    file = request.files['file']

    if file:
        upload_folder = os.path.join("static", "uploads")
        os.makedirs(upload_folder, exist_ok=True)
        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)
        prediction = detect_disease(filepath)

        return render_template("disease.html", crop=crop, prediction=prediction, image=file.filename)

    return render_template("disease.html", crop=crop, prediction="No file uploaded", image=None)


# ------------------- Roadmap -------------------
@app.route('/roadmap')
def roadmap():
    return render_template("roadmap.html")


if __name__ == "__main__":
    app.run(debug=True)
