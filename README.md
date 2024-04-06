

# Spinach Disease Prediction Web App

This web application predicts diseases in spinach leaves based on uploaded images. It is implemented using Flask, a Python web framework.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```bash
    python app.py
    ```

## Usage

1. Access the main page by navigating to `http://localhost:5000/main-page` in your web browser.

2. Select an image of a spinach leaf and click the "Predict" button.

3. You will be redirected to the result page (`/result-page`) where the predicted diseases and their accuracies will be displayed.

## Files

- `app.py`: Flask application file containing routes and logic.
- `main-page.html`: HTML template for the main page where users upload images.
- `result-page.html`: HTML template for the result page where prediction results are displayed.
- `styles.css`: CSS file for styling the HTML templates.
- `static/`: Directory containing static files such as images.
- `templates/`: Directory containing HTML templates.

## Dependencies

- Flask
- Other dependencies listed in `requirements.txt`

