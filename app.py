from flask import Flask, render_template

app = Flask(__name__)

# Route for the welcome page (first page)
@app.route('/')
def welcome_page():
    return render_template('welcome-page.html')

# Route for the main page
@app.route('/main-page')
def main_page():
    return render_template('main-page.html')

# Route for the result page
@app.route('/result-page')
def result_page():
    return render_template('result-page.html')

if __name__ == '__main__':
    app.run(debug=True)