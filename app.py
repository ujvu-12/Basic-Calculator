from flask import Flask, request, render_template_string

app = Flask(__name__)

# ✅ Replace old HTML with this new styled version
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Basic Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            text-align: center;
            width: 300px;
        }
        input, button {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            background: #4CAF50;
            color: white;
            cursor: pointer;
            border: none;
        }
        button:hover {
            background: #45a049;
        }
        h2 {
            margin-bottom: 20px;
        }
        .result {
            margin-top: 15px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Basic Calculator</h2>
        <form method="post">
            <input type="number" step="any" name="num1" placeholder="First number" required><br>
            <input type="text" name="op" placeholder="+ - * /" required><br>
            <input type="number" step="any" name="num2" placeholder="Second number" required><br>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
        <div class="result">Result: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["op"]
            if op == "+": result = num1 + num2
            elif op == "-": result = num1 - num2
            elif op == "*": result = num1 * num2
            elif op == "/": result = "Error (div by 0)" if num2 == 0 else num1 / num2
            else: result = "Invalid operator"
        except:
            result = "Invalid input"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
