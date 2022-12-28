from flask import *
from random import randint
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
      return render_template("home.html")
    else:
        pc = randint(0, 10)
        palpite = int(request.form.get('input'))
        print(pc)
        if pc == palpite:
            return f"""<body style="Background-color: black; text-aligm: center; justify-content: center; aligm-items: center;">
                            <p style="background-color: black; color: green;">Você ganhour, o valor era {pc}.</p>
                        </body>"""
        else:
            return f"""<body style="Background-color: black; text-aligm: center; justify-content: center; aligm-items: center;">
                            <p style="background-color: black; color: green;">Você perdeu, o valor era {pc}.</p>
                        </body>"""
if __name__ == "__main__":
    app.run(debug=True)