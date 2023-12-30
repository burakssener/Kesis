# Kesis: A Social Media for Private Communities

# Video Demo:
To learn more in a shorter time,[Watch this short video!](https://www.youtube.com/watch?v=1YXpfPYnxjE)

# Description:
## What is Kesis?

Kesis is where you can find the community you're seeking!

## Features
KESIS is a social media platform that allows you to:
*Create your own private communities
*Share posts and communicate with other members
*Explore and discover new communities and topics that interest you

## Technologies and Tools
**_Python-Flask, Jinja2, sqlite3, html, css, bootstrap_**

## Briefly Functionality of Kesis

### SQLite3 Database Diagram:
<img src="./static/database.png"/>



## Function Explanations:
### /:
Displays the homepage that can direct users and inform.

### /register, /login /logout:
Registers users and securely stores their passwords by hashing. After authorization, the information is stored in SQLite3.


### /feed:
* Users can share posts in the groups they have chosen.
* Users can see all posts from the groups they have joined.

To display all options for a user's groups and all posts from the groups they have joined, I used SQLite3 and Jinja2 templates. For the database, I utilized the SQL library function of cs50.

### /groups:
* Creating Groups
* Joining Groups

I used two different forms, and users can see all group and create group options on the same page. New groups are created according to the given form in the backend. When users click the join button for other groups, they are redirected to groups/<group_name>/lock.

### /profile:
* Profile Information
* View options for all groups that the user has joined

Jinja2 and SQLite3 are used to display the information, and users are redirected to /groups/{{group['group_name']}} with Jinja2.


### /groups/<group_name>:
* View all group posts
* Share posts to these gorup

Validate if the logged-in user is already in the group_members table. If the person is not eligible, redirect to groups/<group_name>.

### /groups/<group_name>/lock:
* Join groups from here by entering the password.
* Protection system to ensure that people who don't know the group password can't access content

When users join the group, if any user tries to access groups they haven't joined, they will automatically be redirected to this page.



