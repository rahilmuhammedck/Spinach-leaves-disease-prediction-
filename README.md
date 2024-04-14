

# Spinach Leaves Disease Prediction App File Structure

This Flask application is structured as follows:

```
flask_app/
│
├── static/
│   ├── css/
│   │   ├── styles.css
│   │   └── welcome.css
│   └── images/
│       ├── background.jpg
│       ├── spinach1.jpg
│       └── spinach2.jpg
│
├── templates/
│   ├── main-page.html
│   ├── result-page.html
│   └── welcome-page.html
│
├── app.py
└── README.md
```

## Directory Structure

- **static/**: Contains static files such as CSS stylesheets and images.
  - **css/**: Contains CSS files for styling.
    - **styles.css**: CSS file for styling the main and result pages.
    - **welcome.css**: CSS file for styling the welcome page.
  - **images/**: Contains image files used in the application.
    - **background.jpg**: Background image for pages.
    - **spinach1.jpg**, **spinach2.jpg**: Images for displaying spinach leaves.
  
- **templates/**: Contains HTML templates.
  - **main-page.html**: HTML template for the main page.
  - **result-page.html**: HTML template for the result page.
  - **welcome-page.html**: HTML template for the welcome page.

- **app.py**: Flask application file containing routes and logic.

## Usage

To run the Flask app:

1. Make sure you have Flask installed. If not, install it using pip:

    ```
    pip install Flask
    ```

2. Run the Flask app by executing the `app.py` file:

    ```
    python app.py
    ```

3. Access the application in your web browser by navigating to `http://localhost:5000`.

## Notes

- Adjust the file names and paths as needed to match your project structure.
- Customize the HTML templates, CSS files, and Flask routes according to your requirements.

--- 