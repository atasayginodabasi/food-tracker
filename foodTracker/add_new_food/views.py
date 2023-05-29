from flask import render_template, url_for, flash, redirect, Blueprint
from foodTracker.add_new_food.forms import NewFoodForm
from foodTracker.models import Foods
from foodTracker import db, login_manager

add_new_food = Blueprint('add_new_food', __name__)


@add_new_food.route('/add-new-food', methods=['GET', 'POST'])
def create_new_food():
    form = NewFoodForm()

    if form.validate_on_submit():

        if not Foods.query.filter_by(food_name=form.food_name.data).first():
            entry = Foods(food_name=form.food_name.data,
                          protein=form.protein.data,
                          carbohydrates=form.carbohydrates.data,
                          fat=form.fat.data)

            db.session.add(entry)
            db.session.commit()

            return redirect(url_for('add_new_food.create_new_food'))

        else:
            flash('This food is already registered!')
            form = NewFoodForm(formdata=None)

    return render_template('add_food.html',
                           form=form)
