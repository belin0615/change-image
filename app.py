import os
import uuid
from flask import Flask, render_template, request, jsonify, send_from_directory

# Optional: uncomment when using the real API
# import openai

app = Flask(__name__)
app.config['GENERATED_FOLDER'] = os.path.join('static', 'generated')
os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

# Simple in-memory history of generated images
HISTORY = []

# Preset styles with example colors used for the demo
STYLES = [
    {'id': 'watercolor', 'name': 'Watercolor', 'color': '#add8e6'},
    {'id': 'oil', 'name': 'Oil Painting', 'color': '#f0e68c'},
    {'id': 'sketch', 'name': 'Sketch', 'color': '#d3d3d3'},
    {'id': 'custom', 'name': 'Custom', 'color': '#ffffff'},
]

@app.route('/')
def index():
    return render_template('index.html', styles=STYLES, history=HISTORY)

@app.route('/pay', methods=['POST'])
def pay():
    """Simulated payment endpoint."""
    # Here you would integrate with a real payment gateway (WeChat/Alipay)
    return jsonify({'status': 'success'})

@app.route('/generate', methods=['POST'])
def generate():
    img_file = request.files['image']
    style_id = request.form.get('style')
    custom_style = request.form.get('custom_style', '')

    style_text = custom_style if style_id == 'custom' else style_id

    # In a real implementation you would send img_file and style_text to the
    # OpenAI API to generate a styled image. This demo simply returns the
    # original image to keep the example self contained.
    filename = f"{uuid.uuid4().hex}.png"
    save_path = os.path.join(app.config['GENERATED_FOLDER'], filename)
    img_file.save(save_path)

    HISTORY.append({'style': style_text, 'filename': filename})

    return jsonify({'url': f"/static/generated/{filename}"})

@app.route('/static/generated/<path:filename>')
def generated(filename):
    return send_from_directory(app.config['GENERATED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
