from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and corresponding view function
@app.route('/')
def index():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
    #helloooooo
    #hello 2

i = 1
while i>=1:
    if i==5:
        break
    else:
        i+=1