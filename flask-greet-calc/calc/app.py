# Put your app in here.
from operations import *
from flask import Flask, request


app = Flask(__name__)

# ***/add***   Adds ***a*** and ***b*** and returns result as the body.
# ***/sub***   Same, subtracting ***b*** from ***a***.
# ***/mult***   Same, multiplying ***a*** and ***b***.
# ***/div***   Same, dividing ***a*** by ***b***.

@app.route("/")
def index():
    return "Home"
# /add?a=10&b=20
@app.route('/add')
def add_num():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"<h1>{a}+{b}={add(a,b)}</h1>"
@app.route('/sub')
def sub_num():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"<h1>{a}-{b}={sub(a,b)}</h1>"
@app.route('/mult')
def mult_num():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"<h1>{a}*{b}={mult(a,b)}</h1>"
@app.route('/div')
def div_num():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"<h1>{a}/{b}={div(a,b)}</h1>"

# - ***/math/add***
# - ***/math/sub***
# - ***/math/mult***
# - ***/math/div***
@app.route('/maths')
def add_form():         
    form = """
            <form id="mathForm" method="POST">
                <label for="a">num1</label>
                <input type="text" name="a" id="a">
                <br>
                <input type="radio" id="add" name="operation" value="add" checked />
                <label for="add">Add</label>
                <input type="radio" id="sub" name="operation" value="sub" />
                <label for="sub">Subtract</label>
                <input type="radio" id="mul" name="operation" value="mul" />
                <label for="mul">Multiply</label>
                <input type="radio" id="div" name="operation" value="div" />
                <label for="div">Divide</label>
                <br>
                <label for="b">num2</label>
                <input type="text" name="b" id="b">
                <br>
                <button>Submit</button>
            </form>
            <script>
                document.getElementById('mathForm').onsubmit = function() {
                    let operation = document.querySelector('input[name="operation"]:checked').value;
                    this.action = '/maths/' + operation;
                };
            </script>
        """
    return form
@app.route('/maths/<operation>', methods=["POST"])
def add_result(operation):
    operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
    a = int(request.form["a"])
    b = int(request.form["b"])
    return f"{a} {operation} {b} equals {operators[operation](a,b)}"

# extra
@app.route('/math/<opp>')
def show_opp(opp):
    operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"{operators[opp](a,b)}"