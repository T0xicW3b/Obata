from app import app
from flask import render_template, request, session, send_file
import pandas as pd
from game import Question, gen_questions

df = pd.read_csv('data.csv')

@app.get("/")
def index():
    allPlants = len(df)
    return render_template("index.html", allPlants=allPlants)

@app.get('/data.csv')
def serve_csv():
    return send_file('data.csv', mimetype='text/csv')

@app.get("/plantas/<plantName>")
def plant_info(plantName):
    result = df[df['Nome Popular'].str.lower() == plantName.lower()]
    
    if not result.empty:
        plant = result.iloc[0].to_dict()
        return render_template("search.html", plant=plant)
    
    else:
        return render_template("error.html")

@app.route("/game", methods=["POST", "GET"])
def game():
    if "index" not in session:
        questions = gen_questions("data.csv", 60, "Nome Popular", "Nome Científico")
        session["questions"] = [
            {"ask": q.ask, "a": q.a, "b":q.b, "c": q.c, "d": q.d, "e": q.e, "correct": q.correct}
            for q in questions
        ]
        session["index"] = 0
        session["score"] = 0

    if request.method == "POST":
        r = request.form.get("qu")
        correct = session['questions'][session["index"]]['correct']
        if r and r.strip().lower() == correct.strip().lower():
            session["score"] += 1
        session["index"] += 1

    if session["index"] >= len(session['questions']):
        score = session["score"]
        session.clear()
        return render_template("results.html", score=score)

    q = session['questions'][session["index"]]
    return render_template("game.html", question=q)