from flask import render_template, url_for, request, redirect, Blueprint
import stripe

sales = Blueprint('shop', __name__)

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
public_key = 'pk_test_TYooMQauvdEDq54NiTphI7jx'
YOUR_DOMAIN = 'http://localhost:80'


@sales.route('/shop', methods=['GET', 'POST'])
def shop_page():
    print(request.form.get('a'))
    return render_template("shop.html",
                           public_key=public_key)


@sales.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@sales.route('/payment', methods=['GET', 'POST'])
def payment():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': "price_1NEGDD2eZvKYlo2Cpft6TINs",
                    'quantity': 5,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/thankyou',
            cancel_url=YOUR_DOMAIN + '/shop',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def basket():
    pass


# stripe.Product.create(
#   name="Strawberry",
#   default_price_data={
#     "unit_amount": 10000,
#     "currency": "try",
#   },
#   expand=["default_price"],
# )
