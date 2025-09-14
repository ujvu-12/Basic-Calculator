🧮 Basic Calculator

A simple calculator project built in Python that performs basic arithmetic operations.
It works both as a console program and as a web app (via Flask, deployed on Render).

🚀 Features

Supports addition, subtraction, multiplication, division

Handles invalid inputs & division by zero

Two versions:

Console mode → run calculator.py

Web mode → Flask app (app.py)

Deployed on Render for online access

📂 Project Structure
Basic-Calculator/
├── calculator.py       # Console-based calculator
├── app.py              # Flask web app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

🖥️ Console Usage
Run locally:
python calculator.py


Then follow the prompts:

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

This app can be deployed for free on Render.

Steps:

Push your code to GitHub (done ✅)

Go to Render

Create New Web Service

Connect repo & set:

Build Command → pip install -r requirements.txt

Start Command → gunicorn app:app

Deploy 🎉 → You’ll get a public link like:

https://basic-calculator.onrender.com

⚠️ Disclaimer

This project is for educational purposes only.
Not intended for production use.
