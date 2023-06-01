from flask import render_template, url_for, request, redirect, Blueprint
import stripe

sales = Blueprint('shop', __name__)

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
public_key = 'pk_test_TYooMQauvdEDq54NiTphI7jx'


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
    # CUSTOMER INFORMATION
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])

    # CHARGE/PAYMENT INFORMATION
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=2000,
        currency='usd',
        description='Shopping'
    )

    return redirect(url_for('shop.thankyou'))


def basket():
    pass
