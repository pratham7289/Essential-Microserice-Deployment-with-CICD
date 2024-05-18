# Importing necessary modules and libraries
from task_services import task_services
from user_services import user_services
from flask import Flask

# Defining the secret key for Flask application
my_secret_key = 'my_secret-key'

# Creating a Flask app instance
app = Flask(__name__)

# Registering blueprints for user and task services
app.register_blueprint(user_services)
app.register_blueprint(task_services)

# Running the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
