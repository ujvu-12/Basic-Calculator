from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h2>Basic Calculator</h2>
<form method="post">
    <input type="number" step="any" name="num1" placeholder="First number" required>
    <input type="text" name="op" placeholder="+ - * /" required>
    <input type="number" step="any" name="num2" placeholder="Second number" required>
    <button type="submit">Calculate</button>
</form>
{% if result is not none %}
<p><b>Result: {{ result }}</b></p>
{% endif %}
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
