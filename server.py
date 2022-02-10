
# Imports
from flask import Flask  # Import Flask to allow us to create our app


# Instatiating from Flask
app = Flask(__name__) # Create a new instance of the Flask class called "app"









# Routing Methods
@app.route('/')             # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Default!'  # Return the string 'Hello World!' as a response

@app.route('/test')
def wow():
    return 'TEST!'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "TEST: " + name

