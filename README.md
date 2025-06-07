# Image Style Transformer

This project provides a minimal web application that demonstrates how a user can
upload an image and transform it into a different artistic style using the
OpenAI GPT-4o image generation API. It includes a very simple pay-per-use flow
and keeps a history of generated images during a session.

## Features

* Upload an image and choose among preset styles or provide a custom style.
* Example style previews are shown as colored blocks.
* A simulated payment step is performed before image generation.
* Generated images can be downloaded and are listed in a history section.
* Server built with Flask (Python) for simplicity.

The actual call to the OpenAI API is represented by a placeholder that simply
saves the original image. Integrate the real API by replacing that section in
`app.py`.

## Running the app

1. Install dependencies (Flask, OpenAI SDK and Pillow if needed):
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000` in your browser.

This repository contains only minimal styling and a very small example
implementation. Payment and OpenAI integration need to be replaced with real
code for production use.
