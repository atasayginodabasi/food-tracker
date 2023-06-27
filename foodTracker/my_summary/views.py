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
    totals = retrieve_data(start_date, end_date)[0]
    fav_foods = retrieve_data(start_date, end_date)[1]

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
        y=totals['total_protein'],
        x=totals['date'],
        text=totals['total_protein'],
        textposition='auto',
        name=f"Total Protein",
        showlegend=False,
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        y=totals['total_carbohydrates'],
        x=totals['date'],
        text=totals['total_carbohydrates'],
        textposition='auto',
        name=f"Total Carbohydrates",
        showlegend=False,
    ), row=1, col=2)

    fig.add_trace(go.Bar(
        y=totals['total_fat'],
        x=totals['date'],
        text=totals['total_fat'],
        textposition='auto',
        name=f"Total Fat",
        showlegend=False,
    ), row=2, col=1)

    fig.add_trace(go.Bar(
        y=totals['calories'],
        x=totals['date'],
        text=totals['calories'],
        textposition='auto',
        name=f"Calories",
        showlegend=False,
    ), row=2, col=2)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(title_text='Daily Nutritions', title_x=0.5)

    fig.update_xaxes(patch=dict(tickmode='array',
                                tickvals=list(totals['date']),
                                ticktext=list(totals['date'].dt.strftime("%Y-%m-%d"))))

    graph_totals = fig.to_html(full_html=False)

    # ------------

    fig_fav_foods = go.Figure([
        go.Bar(
            y=fav_foods['count'],
            x=fav_foods['food_name'],
            text=fav_foods['count'],
            textposition='auto',
            marker=dict(colorscale='sunset', color=fav_foods['count']),
            showlegend=False,
        )
    ])
    fig_fav_foods.update_layout(title_text='Favorite Foods', title_x=0.5)
    fig_fav_foods.update_layout(xaxis={'categoryorder': 'total descending'})
    fig_fav_foods.update_traces(textposition='auto')
    fig_fav_foods.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig_fav_foods.update_traces(marker=dict(line=dict(color='#000000', width=1)))

    fig_fav_foods.update_xaxes(title_text="Foods")
    fig_fav_foods.update_yaxes(title_text="Number of Consumption")
    graph_fav_foods = fig_fav_foods.to_html(full_html=False)

    return render_template("my_summary.html",
                           form=form,
                           graph_totals=graph_totals,
                           graph_fav_foods=graph_fav_foods)


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

    top_foods = Entries.query. \
        join(Foods, Foods.id == Entries.food_selection). \
        filter(and_(Entries.user_id == str(current_user.id),
                    Entries.date >= start_date,
                    Entries.date <= end_date)). \
        with_entities(
            Foods.food_name,
            func.count(Foods.food_name).label('count')). \
        group_by(Foods.food_name).all()

    totals = pd.DataFrame(totals)
    top_foods = pd.DataFrame(top_foods)

    return totals, top_foods
