# Food Tracker

Food Tracker app helps you to track your daily consumed foods. 

You can add your daily consumed foods to website easily. Hence, you are able to track your daily consumed protein, carbohydrate, fat and calories.

*Motivation*: I'm currently learning Flask and following a Coursera course (course_link_here). This project idea was a homework of this course, I wanted to add something from myself to increase functionalities and have some fun.

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

![login-page](https://github.com/atasayginodabasi/food-tracker/assets/89684816/d1c69083-d559-4797-b4e6-56fceb72fdda)

You are able to enter your username and password to login in this page. If you are not registered, you can use the "Register" page.

---

## Register Page

![register-page](https://github.com/atasayginodabasi/food-tracker/assets/89684816/e1b018b4-0c26-41fd-9dd2-8cbff32c9ad7)

To register to Food Tracker, you need to fill all the inputs. Name and Surname is not unique fields but your user name must be unique. I store the passwords in their hashed format. Finally, your "password" input and "verify password" fields must match.

---

## Main Page

![main-page](https://github.com/atasayginodabasi/food-tracker/assets/89684816/1fc473b6-0573-4373-ad57-65247293a22b)

Once you entered your correct username and password, you redirect to the main page. At the top of the page a jumbotron welcomes you with your name.

You can use this page to create a new entry using "Create a New Entry" button. So, you will be redirected to entry creation page.

Just below of this button, you can reach your past nutrition consumption data sorted by the date. The 4 bullet badges shows the corresponding page's summation of the nutritions.

To reach the more details of the desired day, you are able to click the "View Datail" button. In this page, you can see the corresponding day's consumed foods and their nutritions. In addition to that, you can add new foods to this day or delete the foods if you like.

![view-details](https://github.com/atasayginodabasi/food-tracker/assets/89684816/80f28b5c-2f10-4340-b05b-004f19a8a384)

At the bottom of the page, you can see the total summ of the  metrics for this correcponding day.

---

## My Summary Page

My Summary Page shows the daily protein, carbohydrates fat and total calories for desired date range. At the bottom of the page, you can also reach the favorite goods for this date range. To reach desired date range, feel free to use dat time picker on the top and click the "Query" button!

![my-summary-1](https://github.com/atasayginodabasi/food-tracker/assets/89684816/22e441f6-e2b9-4dd4-ace7-d384bc5a248e)

![my-summary-2](https://github.com/atasayginodabasi/food-tracker/assets/89684816/3cd43b9b-892a-4efa-a7cc-4c1a690fd54a)

---

## Add New Food Item

If you are not able too see your consumed food at the food list, you can create your own using "Add New Food Item" page. At this page you need to enter name of the new food, protein, carbohydrates and fat inputs. Finally, click the "Create the new Food" button.

![add-new-food-item](https://github.com/atasayginodabasi/food-tracker/assets/89684816/f07db1cd-9332-424f-8366-83a9b3101143)

---

## Shop
