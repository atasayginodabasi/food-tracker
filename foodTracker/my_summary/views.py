from flask import render_template, session, url_for, request, redirect, Blueprint
from flask_login import current_user, login_required
import plotly.graph_objects as go
import pandas as pd
from foodTracker.my_summary.forms import DateSelectionForm
from foodTracker.models import Entries, Foods
from sqlalchemy import and_
from sqlalchemy import func

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
    print(data)

    # Create a scatter plot using Plotly
    fig = go.Figure(data=go.Scatter(
        x=data['date'],
        y=data['total_protein'],
        mode='markers+text+lines',
        text=data['total_protein'],
        textposition='top center',
    ))

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Value'
    )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_xaxes(title_text="Days",
                     patch=dict(tickmode='array',
                                tickvals=list(data['date']),
                                ticktext=list(data['date'].dt.strftime("%Y-%m-%d"))))
    graph = fig.to_html(full_html=False)

    return render_template("my_summary.html",
                           form=form,
                           graph=graph)


def retrieve_data(start_date, end_date):

    # data = pd.DataFrame({
    #     'Date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    #     'Value': [i ** 2 for i in range(365)]
    # })
    #
    # data["Date"] = pd.to_datetime(data["Date"]).dt.date
    #
    # # Filter the data based on the selected date range
    # mask = (data['Date'] >= start_date) & (data['Date'] <= end_date)
    # filtered_data = data.loc[mask]

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
