from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

# Load your pre-trained model
model = load_model("model/catsdogs.h5")  # Adjust path to your model

classes = ['Cat', 'Dog']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get file from form
        file = request.files["image"]
        if file:
            # Process the image
            img = load_img(file, target_size=(128, 128))  # Adjust to your model's input size
            img_array = img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Predict
            prediction = model.predict(img_array)
            predicted_class = classes[np.argmax(prediction)]

            return render_template("index.html", prediction=predicted_class)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
