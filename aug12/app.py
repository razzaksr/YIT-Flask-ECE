from flask import *

app = Flask(__name__)

# in memory data
games = [
    {"name":"gta5","genre":"arcade","space":12.780},
    {"name":"free fire","genre":"mission","space":7.2},
    {"name":"god of war","genre":"story","space":9.5},
    {"name":"call of duty","genre":"arcade","space":20.780}
]

# routers

@app.route("/delete/<one>")
def remove(one):
    global games
    games = [each for each in games if each["name"]!=one]
    return redirect("/")
@app.route("/add",methods=["GET","POST"])
def showAdd():
    if request.method == "GET": return render_template('add.html')
    else:
        newName = request.form["name"]
        newGenre = request.form["genre"]
        newSpace = float(request.form["space"])
        newGame = {"name":newName,"genre":newGenre,"space":newSpace}
        games.append(newGame)
        return redirect("/")

@app.route("/",methods=["GET"])
def viewList(): return render_template('index.html',wish = games)
@app.route("/restapi")
def viewJson(): return jsonify(games)

if __name__ == "__main__":
    app.run('localhost',8888)