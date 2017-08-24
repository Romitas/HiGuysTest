# MyAuth Backend Test Application

## Features

- Session authorization
- Extended User model
- REST API
- Basic administration tools

## Usage

1. Open the app: https://higuys-auth.herokuapp.com
2. Log in (admin:adminpassword) to view API in browser
3. Get the authorization token: https://higuys-auth.herokuapp.com/account/token, POST {'email':'admin@admin.net', 'password':'adminpassword'}
4. Include header {'Authorization':'Token yourauthorizationtokenhere'} in the requests to gain access to Users REST API (CRUD)

## Hints

- Creating a new user automatically creates a unique API token for him
- New UserTypes can be added ONLY with admin panel
- Users can be created, modified or deleted using the API (with POST, PUT and DELETE requests accordingly)
- You may also view, add and edit Users and UserTypes with administration tools

Denis Surdeykin, surdeykin.denis@gmail.com, 2017
