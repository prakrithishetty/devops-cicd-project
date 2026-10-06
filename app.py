from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps CI/CD Demo Application</h1>
    <p>Status: Running</p>
    <p>Version: 1.0</p>
    <p>Environment: Development</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



