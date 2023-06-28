# Food Tracker

The Food Tracker app helps you to track your daily consumed foods. 

You can add your daily consumed foods to the website easily. Hence, you can track your daily consumed protein, carbohydrate, fat, and calories.

*Motivation*: I'm currently learning Flask and following a Coursera course (course_link_here). This project idea was homework of this course, I wanted to add something from myself to increase functionalities and have some fun.

*Used Technologies*: Python, Flask, HTML, CSS, PostgreSQL, Docker, Stripe, Plotly and some JS. 

---

This app contains 8 different views:
- Login Page
- Register Page
- Main Page
- Create New Entry
- My Summary
- Add New Food Item
- Shop
- Checkout

---

## Login Page

![login-page](https://github.com/atasayginodabasi/food-tracker/assets/89684816/52e46523-7aeb-4d3f-a826-d464ab3db88b)


You are able to enter your username and password to login in this page. If you are not registered, you can use the "Register" page.

---

## Register Page

![register-page](https://github.com/atasayginodabasi/food-tracker/assets/89684816/c8820b7a-bada-4312-b3ba-c1c1a8141ec9)


To register to Food Tracker, you need to fill in all the inputs. Name and Surname are not unique fields but your user name must be unique. I store the passwords in their hashed format. Finally, your "password" input and "verify password" fields must match.

---

## Main Page

![main-page](https://github.com/atasayginodabasi/food-tracker/assets/89684816/76a18284-aadf-4e6e-9e67-b418ca4ccf68)


Once you entered your correct username and password, you redirect to the main page. At the top of the page, a jumbotron welcomes you with your name.

You can use this page to create a new entry using the "Create a New Entry" button. So, you will be redirected to the entry creation page.

Just below this button, you can reach your past nutrition consumption data sorted by the date. The 4 bullet badges show the corresponding page's summation of the nutrition.

To reach more details of the desired day, you are able to click the "View Detail" button. On this page, you can see the corresponding day's consumed foods and their nutrition. In addition to that, you can add new foods to this day or delete the foods if you like.

![view-details](https://github.com/atasayginodabasi/food-tracker/assets/89684816/09efd98e-e7ab-4b1b-8e97-6c7f464f8245)

At the bottom of the page, you can see the total sum of the metrics for this corresponding day.

---

## My Summary Page

My Summary Page shows the daily protein, carbohydrates fat, and total calories for the desired date range. At the bottom of the page, you can also reach the favorite goods for this date range. To reach desired date range, feel free to use the date time picker on the top and click the "Query" button!

![my-summary-1](https://github.com/atasayginodabasi/food-tracker/assets/89684816/a2b5a933-8ce1-476c-bcc1-97e89f274e62)

![my-summary-2](https://github.com/atasayginodabasi/food-tracker/assets/89684816/f354c3d1-f00a-412c-b58d-c70b079c853f)

---

## Add New Food Item

If you are not able to see your consumed food on the food list, you can create your own using the "Add New Food Item" page. On this page, you need to enter the name of the new food, protein, carbohydrates, and fat inputs. Finally, click the "Create the new Food" button.

![add-new-food-item](https://github.com/atasayginodabasi/food-tracker/assets/89684816/edbfdfe3-450d-4fd7-89e8-47e6efe275db)

---

## Shop

I used Stripe integration to take payments. It was my first time using this API and it was fun. I'm using the test API of the Stripe so I added some foods and prices to my Stripe session.

Here how it looks when you clicked the "Shop" tab:

![shop](https://github.com/atasayginodabasi/food-tracker/assets/89684816/ebf7b3a7-589a-4d86-a24c-82d8698aef23)

You can reach all of the Stripe products that I added in a 3 columned manner. It shows the image of the product, name, and finally price. You can add products to your cart using the "-" and "+" buttons.

Your basket will be stored in the session data. So, if you do not reset your local storage the basket will be the same.

I added 2 Mantı, 1 Sushi, and 3 Noodles to my basket using this feature. You can reach your number of basket items just by looking the green basket icon:

![shop-1](https://github.com/atasayginodabasi/food-tracker/assets/89684816/e2d8ee2e-21bc-4df0-9aa8-bd881e97e40b)

Totally I have 6 items in my basket.

---

## Checkout

You can reach the Checkout Page just clicking the green basket icon on the top right-hand-side of the navbar. The checkout page is Stripe's website and users would make transactions here. You can see your added cart products and their prices here.

![checkout](https://github.com/atasayginodabasi/food-tracker/assets/89684816/49832609-d6b2-422f-ba05-d3d434cb852e)

If the transaction is completed successfully, you will be redirected to a small "Thank you" page.


---

### Future Work
- Creating a basket page to the user would delete or add more products to the cart
- Adding more analytics to the "My Summary" page
- Google Analytics integration for learning
