from app import app
from flask import render_template, request, session
import pandas as pd
from game import Question, gen_questions

df = pd.read_csv('data.csv')

@app.get("/")
def index():
    allPlants = len(df)
    return render_template("index.html")

@app.route("/pesquisa", methods=['POST'])
def search_plant():
    plantName = request.form.get('search-input')
    result = df[df['Nome Popular'].str.lower() == plantName.lower()]

    if not result.empty:
        plant = result.iloc[0].to_dict()
        return render_template("search.html", plant=plant)
    
    else:
        return "Planta não encontrada! <a href='/'>Voltar</a>"
    
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