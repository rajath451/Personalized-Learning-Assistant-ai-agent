from flask import Flask, render_template
from src.api.routes import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)