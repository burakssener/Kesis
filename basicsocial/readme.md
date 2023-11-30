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

## Functionality of Kesis

### SQLite3 Database Diagram:
![Sql Structure](database.png)


### Python-Flask and Jinja2:
#### /:
Displaying homepage that can direct users and inform.

#### /register, /login /logout:
Registering users and by hashing storing people's passwords to ensure security.And after authorization storing in the sqlite3.


#### /feed:
* People can share posts the groups that they choosed.
* can see all the posts from the groups that they joined

To show all options people's group and all posts that from the groups that they joined, I used this SQLite3 and and Jinja2 template. For the database I used SQL library function of cs50.

/groups:
* Creating Groups
* Joining Groups
I used 2 different form and people can see all groups and creating group options in the same page. According to given form to the backend, new groups are being created. When people click join button for the other groups they are redirecting to the groups/<group_name>/lock:

/profile:
* Profile Information
* View option for all groups that user joined
Jinja2 and sqlite3 is used to show the information. and redirected to the /groups/{{group['group_name']}} with the jinja2.

/groups/<group_name>:
*View all group posts
*Share posts to these gorup
*Validating if the logged in user is already in the group_members table. And if the person is not eligible redirecting to groups/<group_name>.

/groups/<group_name>/lock:
*Join groups from here by entering password.
*Protection system to ensure people that don't know group password don't access content
When people are joining the group and If any user try to access groups that he didn't joined, he will automatically redirected to this page.



