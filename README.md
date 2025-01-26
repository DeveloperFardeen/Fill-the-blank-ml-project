# Fill-the-Blank ML Model

This is a machine learning-based web application that uses a pre-trained BERT model to predict missing words in sentences. The app is built with Flask and deployed on Heroku.

## Features

- Predict missing words in sentences using Hugging Face's Transformers BERT's `fill-mask` pipeline.
- User-friendly web interface for entering sentences.
- Real-time predictions with scores for the top predictions.
- Built with Flask for backend and HTML/CSS for frontend.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning Model**: Hugging Face's Transformers (BERT)
- **Deployment**: Heroku

## Prerequisites

- Python 3.7 or later
- `pip` for package management

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fill-in-the-blank-ml.git
   cd fill-in-the-blank-ml
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Open the app in your browser at `http://127.0.0.1:5000`.

## Usage

1. Enter a sentence with `______` to indicate the missing word. For example:
   ```
   The _______ is blue.
   ```

2. Submit the form and view the predictions

## Acknowledgments

- Hugging Face for the amazing BERT model.
- Flask for making web development simple and intuitive.
- Heroku for free and easy deployment.
