# My Book Store
#### Video Demo:  <URL HERE>
#### Description:
A Website to search, buy book
##### Folder Structure **
/app
    /controllers
        /dashboardHandler.py -> dashboard
        /userHandlers.py -> login, register, logout
        /userInfoHandlers.py -> userInfo, bookmarked, transaction, topup, reset-password
    /static
        /script.js
        /style.css
    /templates
        /login.html
        /apology.html
        /index.html
        /layout.html
        /register.html
    /app.py
    /requirements.txt

#### Use "werkzeug" library for password hashing.
- Login: DONE
- Register: DONE
- Search: IN PROGRESS
  + Need to have a template for displaying detail. (search/detail -> bookDetail.html)
  + Need to have a template for input search information (/search -> search.html)