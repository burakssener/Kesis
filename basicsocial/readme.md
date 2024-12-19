# KESIS: A Social Media for Private Communities

# Video Demo:
To learn better in a shorter time,[Watch this short video!](google.com)

## What is KESIS?

This is KESIS. You can find your community that you are seeking here!

## Features
KESIS is a social media that allows you:
* To create your own private communities
* Share posts and communicate with other members.
* Explore and discover new communities and topics that interest you.

## Technologies and Tools
**_Python-Flask, Jinja2, sqlite3, html, css, bootstrap_**

## Functionality

### SQLite3 Database Diagram:
![Sql Structure](database.png)


### Python-Flask and Jinja2:
#### /:
Displaying homepage that can direct users and inform.

#### /register, /login /logout:
Registering users and by hashing storing people's passwords to ensure security.And after authorization storing in the sqlite3.


#### /feed:
In the feed there is 2 different part.
* People can share posts the groups that they choosed.
* can see all the posts from the groups that they joined

For the database I used SQL library function of cs50. To show all options in group people can choose when publishing and also seeing all posts that from the groups that they joined by getting data from sql Jinja2 template

/groups:

/profile:

/groups/<group_name>:

/groups/<group_name>/lock:



