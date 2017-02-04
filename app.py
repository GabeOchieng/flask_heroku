from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    """
    This method will render the home.html template
    """
    return render_template('home.html')

if __name__ == "__main__":
    # Run with debug=True so that you can see detailed error reports in case
    # something went wrong inside your code!
    app.run(debug=True)
