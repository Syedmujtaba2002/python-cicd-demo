from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask CI/CD App and welcome to Elevate labs 🚀This is the webhook process and elevate labs"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
