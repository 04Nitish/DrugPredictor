from django.shortcuts import render
import os
import pickle
import numpy as np  # type: ignore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

def home(request):
    result = None

    if request.method == "POST":
        age = request.POST.get("age", "0")
        sex = request.POST.get("sex", "").upper()
        bp = request.POST.get("bp", "").upper()
        cholesterol = request.POST.get("Cholesterol", "").upper()
        na_to_k = request.POST.get("Na_to_K", "0")

        try:
            sexa = {"MALE": 1, "FEMALE": 0}[sex]
            bpa = {"LOW": 0, "NORMAL": 1, "HIGH": 2}[bp]
            cholesterola = {"NORMAL": 0, "HIGH": 1}[cholesterol]
            age = int(age)
            na_to_k = float(na_to_k)

            total = np.array([[age, sexa, bpa, cholesterola, na_to_k]])
            prediction = model.predict(total)
            result = prediction[0]
        except (KeyError, ValueError):
            result = "Invalid input. Please check your form values."

    return render(request, "index.html", {'result': result})
