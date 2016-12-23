from flask import Blueprint, render_template


blueprint = Blueprint('africa', __name__)


@blueprint.route("/")
def home():
    return render_template('home.html')
