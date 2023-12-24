# Django Project

## Overview

This is a Django project that includes three apps: `users`, `products`, and `api`. 

## Project Structure
```bash
django_project/
|-- django_project/
| |-- settings.py
| |-- urls.py
|-- api/
| |-- views.py
| |-- serializers.py
| |-- urls.py
|-- products/
| |-- models.py
| |-- views.py
| |-- forms.py
| |-- templates/
| |-- home.html
| |-- new_product.html
| |-- product.html
| |-- edit_product.html
| |-- my_products.html
|-- users/
| |-- models.py
| |-- forms.py
| |-- views.py
| |-- templates/
| |-- registration/
| |-- signup.html
| |-- profile.html
| |-- profile_update.html
|-- manage.py
|-- requirements.txt
```

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:jakhongirodilov/task1_cosinus.git
   cd task1
   
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Apply Migrations:**
    ```bash
    python manage.py migrate
4. **Create a Superuser:**
    ```bash 
    python manage.py createsuperuser

5. **Run the development server:**
    ```bash 
   python manage.py runserver

6. **Access the Admin Interface:**

    Open your browser and go to http://localhost:8000/admin/ to log in with the superuser credentials.


8. **Access the Home Page:**

    Open your browser and go to http://localhost:8000/ to access the home page.

---
## API App

The api app provides additional functionalities via API endpoints.

1. **Serializers**

    * ProductSerializer: Serializes product data.
    * UserSerializer: Serializes user data.


2. **Views**
    
    * UserList: Lists all users (admin only).
    * UserDetail: Retrieves, updates, or deletes a user (admin only).
    * ProductListAPIView: Lists all products.
    * ProductCreateAPIView: Creates a new product.
    * ProductDetailAPIView: Retrieves, updates, or deletes a product (only the owner of the product can update or delete).

---
## API Endpoints
### Authentication and Registration
* /api-auth/: Authentication endpoint.
* /api/dj-rest-auth/: Authentication endpoint.

   #### Registration endpoints:
   * /api/dj-rest-auth/registration/: User registration endpoint.

   #### Login and Logout Endpoints:
   * /api/dj-rest-auth/login: Login endpoint.
   * /api/dj-rest-auth/logout: Logout endpoint.
  
   #### Password Reset Endpoints:
   * /dj-rest-auth/password/reset/ - Initiate a password reset.
   * /dj-rest-auth/password/reset/confirm/ - Confirm password reset.

   #### Password change endpoints:
   * /api/dj-rest-auth/password/change/: Password change endpoint.

   #### User Profile Endpoints:
   * /dj-rest-auth/user/ - Retrieve and Update user profile.


### Products
* /api/products/: List all products.
* /api/products/create/: Create a new product.
* /api/products/<<int:pk>>/: Retrieve, update, or delete a product.

### Users

* /api/users/: List all users (admin only).

* /api/users/<<int:pk>>/: Retrieve, update, or delete a user (admin only).


## Additional Information

    Database: SQLite is used as the default database.
    Static Files: Static files are served at /static/.
    Media Files: User-uploaded files are stored at /media/.
