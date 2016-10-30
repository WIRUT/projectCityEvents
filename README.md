Simon Fraser University - CMPT 470: Web Development 
Project Name: Project City Events
Authors: Ross Kwong
		 Daniel Russell
		 Ian Pun
		 Jacques Wong

Description: 
This project will implement a web application centered around
listing events around the City. This includes compedy, sports,
nightlife, and concerts that will be displayed on a search list
and on Google Maps.

It will utilize several API's including Facebook, Google, and
Eventful.

To Run:
1. Install VirtualBox (https://www.virtualbox.org)

2. Install Vagrant (https://www.vagrantup.com)

3. Run command "vagrant up" to start webserver

4. Go to: "localhost:8080"

5. Run command "vagrant destroy" to stop


Setting Up Social Integration:
Events Ahead has the feature to allow users to login/signup with Facebook and Google. In order to use these features, you must add the proper tokens/keys into the database.

Steps:
1) Log in as a superuser into localhost:8080/admin
2) In the 'Sites' table, add a new site entry with domain name 'localhost:8000' and display name 'local machine'. Go back to the main page after creating.
3) Under 'Social Accounts', click the add button next to 'social applications'
4) Configure like this:

Provider : Facebook
Name : Fb_login
Client id: 1087693501272314
Secret key: 2bc3990a8489fd099b7c0cf8a32a36d6
Sites-> Chosen sites: localhost:8000

hit save.

5 Under 'Social Accounts', click the add button again next to 'social applications'
6) Create the Gmail one like this:

Provider : Google
Name : gmail_login
Client id: 409343455037-6k588vcit0vjf25kfhet177ca1bgisc0.apps.googleusercontent.com
Secret key: sBVtdAi-XU4t9hyr5UmN9Eul
Sites-> Chosen sites: localhost:8000


hit save.

You should now be able to login/sign up with Facebook and google on both the navigation bar as well as the login landing page.

