from flask import Flask, flash, redirect, render_template, request, session

import tensorflow as TF
# Create a Flask application instance
app = Flask(__name__)

# Define a route and corresponding view function
@app.route('/')
def index():
    return 'Hello, World! My name is Enes yo'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

