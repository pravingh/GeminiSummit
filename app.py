import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    return """
    <!DOCTYPE html>
<html>
<head>
  <title>Welcome to Infosys Gemini Summit!</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to bottom, #f0f0f0, #e0e0e0);
      margin: 0;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .container {
      background-color: white;
      padding: 50px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
      text-align: center;
    }

    h1 {
      color: #007bff;
    }

    p {
      font-size: 1.2em;
      margin-bottom: 20px;
    }

    .gradient-text {
      background: linear-gradient(to right, #f06, #36f);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="gradient-text">Welcome to Infosys Gemini Summit</h1>
	<h2 class="gradient-text">Build with Gemini Pro 1.5</h2>
    <p>Get ready to accelerate human progress!</p>
  </div>
</body>
</html>
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
