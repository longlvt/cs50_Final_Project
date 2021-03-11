# My Book Store
#### Video Demo:  <URL HERE>
#### Description:
A Website to search, buy book
- Login page: Allow user to login if he/she has an account.
    + User "werkzeug" to check for the hashed-password.
    + Remember user in browser's Cookies for next visit.

- Register page: Allow user to register new account.
    + Use "werkzeug" library for password hashing.
    + It will not allow user to register a new account which has the same name with old account.

- Header: 
    + Icon of the website, clickable. Redirect users to the Homepage("/") after clicking.
    + Search button: Only displayed if user logged-in. Allow users to search for the book (search criteria by book title).
    + User icon: Only displayed if user logged-in. Display drop down menu, in which:
        ++ Logout button
        ++ Account information.
        ++ Cart: All the books that user has put into his/her cart before.

- Homepage: Only displayed if user logged-in.
    + Route: "/"
    + Description:
        ++ Display top 5 rated books.
        ++ Amount balance
        ++ Display 5 books for recommendation

- Account Information:
    + Account Balance: Display the remaining balance of user. Also allow users to top-up their amount.
    + Transaction: Display all purchase of user.
    + Reset Password: Allow user to reset password.

- Search: Allow user to search for book by book's title
    ++ Book Detail: Display detailed information if the desired book existed in DB
        ++ Add to Cart: Add book to user's cart

- Cart: Display all books that user has added to cart.
    ++ Stick option on each book help user select book again.
    ++ Buy button: purchase for book(s). The amount of book(s) will be deducted in user's balance.
        +++ If user's balance is not enough, this button will be disabled, and there's a warning message.

- Logout: Logout user and delete cookies.


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

- Login: DONE
- Register: DONE
- Search: IN PROGRESS
  + Need to have a template for displaying detail. (search/detail -> bookDetail.html) => DONE
  + Need to have a template for input search information (/search -> search.html) => DONE
  + Need to redirect user to other route (/search/detail) for book detail showing. => DONE

- Cart: IN PROGRESS
  + Need route, function for adding book to cart.
  + Need template to display cart information.
  + Need new table for "Cart".

