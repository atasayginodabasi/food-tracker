from flask import render_template, session, url_for, request, redirect, Blueprint
from flask_login import current_user, login_required
import plotly.graph_objects as go
import pandas as pd
from foodTracker.my_summary.forms import DateSelectionForm
from foodTracker.models import Entries, Foods
from sqlalchemy import and_
from sqlalchemy import func
from plotly.subplots import make_subplots

my_summary = Blueprint('my_summary', __name__)


@login_required
@my_summary.route('/my-summary', methods=['GET', 'POST'])
def summary():
    form = DateSelectionForm()

    start_date = form.start_date.default
    end_date = form.end_date.default

    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data

        # Retrieve data based on the selected date range
    data = retrieve_data(start_date, end_date)

    fig = make_subplots(
        rows=2, cols=2,
        specs=[
            [{}, {}],
            [{}, {}],
        ],
        subplot_titles=("Daily Total Protein Consumption",
                        "Daily Total Carbohydrates Consumption",
                        "Daily Total Fat Consumption",
                        "Daily Calories",
                        ))

    fig.add_trace(go.Bar(
        y=data['total_protein'],
        x=data['date'],
        text=data['total_protein'],
        textposition='auto',
        name=f"Total Protein",
        showlegend=False,
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        y=data['total_carbohydrates'],
        x=data['date'],
        text=data['total_carbohydrates'],
        textposition='auto',
        name=f"Total Carbohydrates",
        showlegend=False,
    ), row=1, col=2)

    fig.add_trace(go.Bar(
        y=data['total_fat'],
        x=data['date'],
        text=data['total_fat'],
        textposition='auto',
        name=f"Total Fat",
        showlegend=False,
    ), row=2, col=1)

    fig.add_trace(go.Bar(
        y=data['calories'],
        x=data['date'],
        text=data['calories'],
        textposition='auto',
        name=f"Calories",
        showlegend=False,
    ), row=2, col=2)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})

    fig.update_layout(title_text='Daily Nutritions', title_x=0.5)
    graph = fig.to_html(full_html=False)

    return render_template("my_summary.html",
                           form=form,
                           graph=graph)


def retrieve_data(start_date, end_date):
    totals = Entries.query. \
        join(Foods, Foods.id == Entries.food_selection). \
        filter(and_(Entries.user_id == str(current_user.id),
                    Entries.date >= start_date,
                    Entries.date <= end_date)). \
        with_entities(
            Entries.date.label('date'),
            func.sum(Foods.protein).label('total_protein'),
            func.sum(Foods.carbohydrates).label('total_carbohydrates'),
            func.sum(Foods.fat).label('total_fat'),
            func.sum(Foods.fat * 9 + Foods.protein * 4 + Foods.carbohydrates * 4).label('calories')). \
        group_by(Entries.date).all()

    totals = pd.DataFrame(totals)

    return totals
