# WEB APPLICATION FOR HOSPITAL-VENDOR CREDENTIALISING

AVA ORG is a Hospital - Vendor medical device management portal, where the Vendor is a medical device manufacturer who publishes their respective products on the portal. Hospital representatives register themselves, browse published medical device products, and can contact vendors for buying the product. Also, they can add their requests for any unpublished/ unavailable medical devices. Vendors can explore these hospital requests and can connect with them for the production of specified devices. Hospitals will have to take into consideration the time required for the vendor to deliver the product. This project acts as a proof of concept.

## CONTRIBUTORS
@Anirudh-Chandran: 10626568
@Ameya-Khandekar: 10547037
@vicky-motwani: 10632013

## TECHNOLOGIES USED
 - Front end
	- HTML
	- CSS
	- JS
 - Middleware
	- Python
		- flask
		- flask session
		- pyodbc
	- Azure app services 
 - Backend
	- Azure SQL
	- XML
## TECHNICAL DESCRIPTION 
The landing page of the web application is the homepage.html which displays images and texts loaded by the Python flask framework and jinja template. The data is fetched from the backend Azure SQL database using the python pyodbc module. The home page has the below navigations: - Home
- Products
- OnDemand Requests
- About Us 
- Login/Register. 
Each navigation is associated with respective flask API routing.

### homepage.html: 
This HTML page is specifically available for unauthorized guests below limited options. We used CSS and Jinja template representations to design the HTML page. The interface has been designed to match an unauthorized view and feel that a guest user shall have. This page showcases the latest six products that get added to the database. Each product displayed has a link that will route the user to the individual product page, with a better view and further detailing about the product. All the data displayed on this page is fetched from the backend database every time the page is loaded.

### user_homepage.html: 
This is the authorized counterpart of homepage.html with further navigation accessibility.

### products.html: 
A guest user can view the available products and access each product separately.

### new_products.html: 
Authorized users will have an additional navigation option on the products.html page, which takes the user to create a new product via the provided form. Post form submission new entry is added to the database using the python "/New_Products" API.

### about_us.html: 
This page highlights the aim of the project.

### login.html: 
It shows fields to enter credentials. As for new users, the sign-up button is provided for registration at the bottom.

### registration.html: 
This page loads a form with two options to either select vendor or hospital based on which the below fields toggle. Javascript embedded ensures this toggling feature. There are validations set on the password field to ensure a strong password is accepted.Credentials.xml stores the credentials of registered users.

### on_demand_request.html: 
It is a page showcasing on-demand requests raised for products that are unavailable on the products page. Users can view the listed requests and access each request separately. Only authorized users are allowed to view this page.

### new_request_form.html: 
Authorized users will have an additional navigation option on the on_demand_request.html page, which takes the user to create a new request via the provided form. Post form submission new entry is added to the database using the python "/New_Request" API.

### user_profile.html:
For authorized users, the page shows the user profile information. This page allows users to edit the details of their profile. There is an option to delete the account.

### App.py
	| APIs                       | Navigations                     | Action -Performed
	========================================================================================================================================================
	| /                          | homepage.html                   | Loads the homepage of the application
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /Home                      | user_homepage.html              | Loads the homepage for authorized user
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /Login                     | login.html                      | Provides the login form and routes back to user_homepage.html after login
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /Logout                    | -----                           | Logs out the user, clears the session, and routes the user to homepage.html
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /Registration              | registration.html               | Registration of a new user
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /Products                  | products.html                   | Products are shown on this page
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /<int:prod_id              | product_page.html               | Used to showcase individual product details
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /New_Products              | new_product_form.html           | Used to create a new product and routes back to the same page
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /OnDemandRequest           | on_demand_request.html          | Used to show the new requests
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /New_Request               | new_request_form.html           | Used to create a new request and routes back to the same page
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /Requests/<int:req_id      | request_page.html               | Individual requests are shown in this page
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /My_Profile                | user_profile.html               | User profile - allows viewing, editing and deleting
	--------------------------------------------------------------------------------------------------------------------------------------------------------
	| /DeleteAccount             | -----                           | Initialised when delete button is clicked on user_profile.html and routes back to homepage.html
	=========================================================================================================================================================
 
## CONTRIBUTION REPORT
 - @Anirudh-Chandran
 - @Ameya-Khandekar
 - @vicky-motwani
## ATTRIBUTION REPORT
### Bootstrap CSS,JS
 - file path: https://github.com/Anirudh-Chandran/B9CY100_2223_APT_10626568_10632013_10547037/tree/main/Python_Code/static/css/
 - copyrights: Bootstrap
 - License: MIT 
### JQuery
 - filepath: https://github.com/Anirudh-Chandran/B9CY100_2223_APT_10626568_10632013_10547037/blob/main/Python_Code/static/js/jquery-3.4.1.min.js
 - copyrights: JS Foundation
 - License: MIT 
### Popper
  - filepath: https://github.com/Anirudh-Chandran/B9CY100_2223_APT_10626568_10632013_10547037/blob/main/Python_Code/static/js/popper.min.js
  - copyrights: Federico Zivolo
  - License: MIT 



 
