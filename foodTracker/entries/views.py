from datetime import datetime
from flask import render_template, url_for, abort, redirect, Blueprint
from sqlalchemy import func
from foodTracker.entries.forms import NewEntryForm
from foodTracker.models import Entries, User, Foods
from foodTracker import db
from flask_login import current_user, login_required
from sqlalchemy import and_

day_details = Blueprint('entries', __name__)


@day_details.route('/create-new-entry', methods=['GET', 'POST'])
@login_required
def create_new_entry():
    form = NewEntryForm()

    if form.validate_on_submit():
        entry = Entries(food_selection=form.food_selection.data,
                        user_id=current_user.id,
                        date=form.date.data)

        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('entries.entries', date=form.date.data.strftime("%Y-%m-%d")))

    return render_template('create_new_entry.html',
                           form=form)


@day_details.route('/entries/<date>', methods=['GET', 'POST'])
@login_required
def entries(date):
    totals = Entries.query. \
        join(Foods, Foods.id == Entries.food_selection). \
        filter(and_(Entries.user_id == str(current_user.id), Entries.date == date)). \
        with_entities(
            Entries.user_id.label('user_id'),
            Entries.date.label('date'),
            func.sum(Foods.protein).label('total_protein'),
            func.sum(Foods.carbohydrates).label('total_carbohydrates'),
            func.sum(Foods.fat).label('total_fat'),
            func.sum(Foods.fat * 9 + Foods.protein * 4 + Foods.carbohydrates * 4).label('calories')). \
        group_by(Entries.date, Entries.user_id).all()

    entry = Entries.query.join(Foods, Foods.id == Entries.food_selection). \
        filter(and_(Entries.user_id == str(current_user.id), Entries.date == date)). \
        with_entities(
        Entries.id,
        Entries.user_id,
        Entries.date,
        Foods.protein,
        Foods.food_name,
        Foods.carbohydrates,
        Foods.fat,
        (Foods.fat * 9 + Foods.protein * 4 + Foods.carbohydrates * 4).label('calories')
    )

    if len(entry.all()) == 0:
        return redirect(url_for('home_page.home'))

    form = NewEntryForm()
    try:
        form.date.data = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        form.date.data = datetime.strptime(date, '%Y-%m-%d')

    if form.validate_on_submit():
        entry = Entries(food_selection=form.food_selection.data,
                        user_id=current_user.id,
                        date=form.date.data)

        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('entries.entries', date=date))

    return render_template('entry.html',
                           totals=totals,
                           entry=entry,
                           form=form)


@day_details.route('/entries/<int:entry_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_entry(entry_id):
    entry = Entries.query.get_or_404(entry_id)

    if current_user.id == entry.user_id:
        db.session.delete(entry)
        db.session.commit()
    else:
        abort(403)

    return redirect(url_for('entries.entries', date=entry.date.strftime('%Y-%m-%d')))
