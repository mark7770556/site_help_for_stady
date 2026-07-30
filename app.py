from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


# создание базы
def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ratings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()



# главная страница
@app.route("/")
def index():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(score), COUNT(score)
    FROM ratings
    """)

    result = cursor.fetchone()

    conn.close()


    if result[0]:
        average = round(result[0], 1)
    else:
        average = 0


    count = result[1]


    return render_template(
        "index.html",
        average=average,
        count=count
    )



# сохранение оценки
@app.route("/rate", methods=["POST"])
def rate():

    # проверка cookie
    if request.cookies.get("rated"):
        return jsonify({
            "status": "already"
        })


    data = request.json

    score = int(data["score"])


    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()


    cursor.execute(
        "INSERT INTO ratings(score) VALUES(?)",
        (score,)
    )


    conn.commit()
    conn.close()



    response = jsonify({
        "status": "success"
    })


    # запоминаем голос на год
    response.set_cookie(
        "rated",
        "true",
        max_age=60*60*24*365
    )


    return response




if __name__ == "__main__":

    create_db()

    app.run(host="0.0.0.0", port=5000)