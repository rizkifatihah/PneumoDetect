from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO
import base64
from io import BytesIO

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load YOLO model
model = YOLO("best.pt")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(image_path):
    # Read image
    image = cv2.imread(image_path)
    
    # Perform prediction
    results = model.predict(source=image, conf=0.25)
    
    # Get the first result
    result = results[0]
    
    # Draw predictions on image
    annotated_image = result.plot()
    
    # Convert to PIL Image
    img_pil = Image.fromarray(annotated_image)
    
    # Save to buffer
    buffered = BytesIO()
    img_pil.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    # Get the highest confidence prediction
    probs = result.probs 
    conf_value = float(probs.top1conf)  
    class_name = result.names[probs.top1]
    
    # Format the confidence result
    confidence = {
        'class': class_name,
        'confidence': f"{conf_value:.2%}"
    }
        
    return img_str, confidence


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
            
        if file and allowed_file(file.filename):
            # Save uploaded file
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            
            # Perform prediction
            predicted_image, confidence = predict_image(filename)
            
            return render_template('index.html', 
                                 original_image=file.filename,
                                 predicted_image=predicted_image,
                                 confidence=confidence)
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
