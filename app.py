from flask import Flask,render_template
from flask_dance.contrib.github import github
from flask_wtf import CSRFProtect
from uuid import uuid4

from views.auth import gh_blueprint,auth
from views.visitors import visitor


app = Flask(__name__)
app.secret_key = uuid4().hex

app.register_blueprint(gh_blueprint, url_prefix="/login")
app.register_blueprint(auth)
app.register_blueprint(visitor)

# CSRFProtect(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":    

    app.run()