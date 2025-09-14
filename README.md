🧮 Basic Calculator

A simple calculator project built in Python that performs basic arithmetic operations.
It works both as a console program and as a web app (via Flask, deployed on Render).

🌐 Live Demo: Basic Calculator on Render

🔗 URL: https://basic-calculator-zw7g.onrender.com

🚀 Features

Supports addition, subtraction, multiplication, division

Handles invalid inputs & division by zero

Two versions:

Console mode → run calculator.py

Web mode → Flask app (app.py) deployed online

Modern styled interface for easy use

📂 Project Structure
Basic-Calculator/
├── calculator.py       # Console-based calculator
├── app.py              # Flask web app (deployed)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

🖥️ Console Usage

Run locally:

python calculator.py


Example:

Enter first number: 10
Enter operator (+ - * /): *
Enter second number: 5
Result: 50

🌐 Web App Usage
Run locally:

Install dependencies:

pip install -r requirements.txt


Start the app:

python app.py


Open browser → http://127.0.0.1:5000

Online Deployment:

This app is live on Render:
👉 https://basic-calculator-zw7g.onrender.com

🔗 URL: https://basic-calculator-zw7g.onrender.com

If you want to deploy your own:

Push this repo to GitHub.

Go to Render
 → create New Web Service.

Set:

Build Command → pip install -r requirements.txt

Start Command → gunicorn app:app

Deploy 🚀

⚠️ Disclaimer

This project is for educational purposes only.
Not intended for production use.
