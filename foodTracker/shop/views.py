from flask import render_template, session, url_for, request, redirect, Blueprint
import stripe
import pandas as pd
import itertools

sales = Blueprint('shop', __name__)

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
public_key = 'pk_test_TYooMQauvdEDq54NiTphI7jx'
YOUR_DOMAIN = 'http://localhost:80'


@sales.route('/shop', methods=['GET', 'POST'])
def shop_page():
    items = pd.DataFrame([i for i in stripe.Product.list(limit=50).data if i.default_price is not None])

    prices = pd.DataFrame(stripe.Price.list(limit=50).data)

    products = items[['id', 'default_price', 'name']] \
        .merge(prices[['currency', 'product', 'unit_amount', 'unit_amount_decimal']],
               left_on='id', right_on='product') \
        .drop_duplicates(subset=['name'], keep='first')

    return render_template("shop.html",
                           public_key=public_key,
                           products=products)


@sales.route('/thank-you')
def thankyou():
    return render_template('thankyou.html')


@sales.route('/payment', methods=['GET', 'POST'])
def payment():
    try:
        checkout_session = stripe.checkout.Session.create(
                line_items=session['basket'],
                mode='payment',
                success_url=YOUR_DOMAIN + '/thank-you',
                cancel_url=YOUR_DOMAIN + '/shop',
            )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@sales.route('/basket', methods=['GET', 'POST'])
def basket():
    try:
        new_added_to_cart = {
            'price': request.args.get('id'),
            'quantity': request.form.get('quantity'),
        }

        cart = list(session['basket'])
        cart.append(new_added_to_cart)

        session['basket'] = cart
        print(session['basket'])

    except KeyError:
        session['basket'] = [{
            'price': request.args.get('id'),
            'quantity': request.form.get('quantity'),
        }]

    return redirect(url_for("shop.shop_page"))


def create_stop_item(productName, price, currency='usd'):
    print(stripe.Product.create(
        name=productName,
        default_price_data={
            "unit_amount": price,
            "currency": currency,
        },
        expand=["default_price"],
    ))
