from flask import render_template, url_for, \
    request, abort, Blueprint
from sqlalchemy import func
from flask_login import current_user, login_required
from foodTracker.models import Entries, Foods

home_page = Blueprint('home_page', __name__)


@home_page.route('/')
@login_required
def home():
    page = request.args.get('page', 1, type=int)

    entries = Entries.query.join(Foods, Foods.id == Entries.food_selection). \
        filter(Entries.user_id == str(current_user.id)). \
        with_entities(
        Entries.date,
        func.sum(Foods.protein).label('total_protein'),
        func.sum(Foods.carbohydrates).label('total_carbohydrates'),
        func.sum(Foods.fat).label('total_fat'),
        func.sum(Foods.fat * 9 + Foods.protein * 4 + Foods.carbohydrates * 4).label('calories')).\
        group_by(Entries.date). \
        order_by(Entries.date.desc()). \
        paginate(page=page, per_page=5)

    return render_template('home.html',
                           entries=entries)
