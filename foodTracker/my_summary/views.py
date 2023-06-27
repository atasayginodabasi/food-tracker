from flask import render_template, session, url_for, request, redirect, Blueprint
from flask_login import current_user, login_required

my_summary = Blueprint('my_summary', __name__)


@login_required
@my_summary.route('/my-summary', methods=['GET', 'POST'])
def summary():
    return render_template("my_summary.html")
