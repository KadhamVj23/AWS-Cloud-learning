from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>☁️ Cloud Notes Application</h1>

    <p>Congratulations!</p>

    <p>Your Flask application is running successfully.</p>

    <p>This application will later be deployed using:</p>

    <ul>
        <li>GitHub</li>
        <li>AWS CodeBuild</li>
        <li>Docker Hub</li>
        <li>AWS CodeDeploy</li>
        <li>AWS CodePipeline</li>
        <li>Amazon EC2</li>
    </ul>

    <p><b>AWS End-to-End CI/CD Project</b></p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)