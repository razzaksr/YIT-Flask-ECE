from flask import *
from forms import GSignForm

app = Flask(__name__)
# csrf token
app.config["SECRET_KEY"] = "eceflaskeee"

@app.route("/", methods=["GET","POST"])
def viewSignUp():
    gsign = GSignForm()
    if gsign.validate_on_submit():
        logged = {
            gsign.fullname.name:gsign.fullname.data,
            gsign.password.name:gsign.password.data,
            gsign.gender.name:gsign.gender.data,
            gsign.email.name:gsign.email.data,
            gsign.contact.name:gsign.contact.data,
            gsign.terms.name:gsign.terms.data
        }
        return jsonify(logged)
    return render_template('index.html',form = gsign)

if __name__ == "__main__":
    app.run('localhost',8888)