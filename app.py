from flask import Flask, render_template, request, session
from game import Question, gen_questions

app = Flask(__name__)
app.secret_key = "abc"

@app.get("/")
def index():

    return render_template("index.html")


@app.get("/game")
def game():
    questions = gen_questions("data.csv", 12, "Nome Popular", "Nome Científico")
    session["questions"] = [
        {
            "id": q.id,
            "ask": q.ask,
            "a": q.a,
            "b": q.b,
            "c": q.c,
            "d": q.d,
            "e": q.e,
            "correct": q.correct,
        }
        for q in questions
    ]
    return render_template("game.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    questions = session.get("questions", [])
    score = 0
    for i in questions:
        r = request.form.get(str(i["id"]))
        if r == i["correct"]:
            score += 1
    return render_template("result.html", score=score)


if __name__ == "__main__":
    app.run(debug=True)