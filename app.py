#this file sets the route to begin with. It will automatically set '/' as homepage.
from flask import Flask, render_template
from controllers.tasks_controller import tasks_blueprint

app = Flask(__name__)
app.register_blueprint(tasks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
