# Golden Estate

Golden Estate is an website for estate agencies where they can display their contents making esier 
to users find their properties in one place insted search for a single agency website at time.

As users can find all kind of properties they are looking for in a single place would become more dificult to reach
all agencies website to search for properties. So based on this principle for a estate agency
would be a great value to display their properties inside Golden Estate and get more chances to be seen 
by users.


### UX

This web site was designed to be simple to the user interact with. 
The colors choosen make a greate contrast to each other looking very nice.

To users its provided a index page to view all properties listed independent if is buy or rent. To filter all that we have a seach bar where user 
can choose to buy or rent, the max and min value, number of bedrooms and city. if no properties is found it will display a message to the user
In the navbar its possible to enter a buy or rent page if user prefer that way intead where in each page they find a properties to buy or Rent only
also we have a link to contact us in case a user need some assistence. If user is a estate agency they can log in access or if they don't have an account
they can use the signup link and buy our package where give them the oportunity to choose how many months of subscription they want from 1 - 12 months
and pay with a credit card that payment is via STRIPE and they take care of all transactions security so it's very safe to agencies.
If user enter on property details they can see all informations displayed such as photos of the property and a map showing its exactly location, but to 
save the maps account intead leave a free search bar based on adreess o button was created to protection, so to user view a location it must click on that
button and the location will be displayed on the map. If user is agency and it is logged in inside the details they can edit or delete their properties added.
To folow us on our social media in the footer of the page user can find all our social media and follow us.

 - As a user i want search for a specific property so that i can use the search bar.
 - As a user i want to view all details so that i can press details button.
 - As a user i want to contact the website managment so that i can use contact us link.
 - As a agency user i want to login so that o can i can use login link.
 - As a agency user i wanto to add a property so that i can login and add a property.
 - As a agency user i wanto to view my properties so that i can login and view my properties.
 - As a agency user i want to edit or delete my properties so that i can login and inside my properties details i can delete or edit my specific property.
 - As a agency user i want to register so i can use signup link and follow the steps until be able to resgister. 
 - As a user i want to view the map location so that i can go inside property details and press the address button in the map to display the location.
 - As a user i want to contact the agency for more details so i can go inside property details and get the agency email to get more info about the property.
 - As a user i want to find social medias so that i can go to the footer and find a link to our social media.

In this project we dont have wireframes or mockups to display besucse the design as base on a website template, i decide not to use a ready template
so i could pratice and learn more frontend and backend skills.
Underneath is the link where my website design was based.
http://haintheme.com/demo/html/realand/index.html


### Features

 - Basic user registration and authentication
 - Navbar with links to buy, rent, contact, login and signup
 - Search bar with filters to buy or rent, min and max price, bedrooms and city
 - Full details of the property
 - Map showing the property location

 - Features Left to Implement:
    - As this is a academic project i tried to get close as possible to a real website, and some features can be impemented as:
    - A seach bar more robust with more things to filter for exemple: furnished, pool, air con, heat and etc, depending on the needs of the customer
    - find a server to django email
    - find a way to user not jump to register without a payment
    - Add more details about agencies
    - Add a reference number in each property to be esier to agecy locate the specific property when emailed or called
    - A map with all properties locations
    - More filter such as House or Flat, Order by ... 
    

### Technologies Used

 - Html
 - Css
 - Javascript
 - Python
 - Django 
 - Stripe
 - Bootstrap
 - Jquery
 - Ajax
 - Google Fonts
 - Font Awesome
 - Emailjs
 - Goole Maps Api 
 - Pillow
 - Gunicorn
 - Psycopg2
 - Aws S3 
 - env.py
 - Coverage
 - Heroku
 - Sqlite3
 - Github


 ### Testing 

This website has been tested in three ways, as this project runs in Django the framework itself already have some internal tests in order to make
your codes run, also i have made couple tests using Coverage wich is a good way to make UnitTest in Python/Django framework. It shows the developer
the percentage of what has been tested and what part of your code you may need to test, I've done around 62% of this project tests.
The main test was made manually in the website testing every functionality because as a developer i know this kind of website need a lot 
assistence so some codes might change.

    1 - Main page you can access all the links and signup to site as well, view all the properties listed but 6 each page.
    2 - Property details works well and display everythin proposed
    3 - Maps also display the location if it is a real location, it's based on Full address, so if the Full address is wrong the map won't display
    4 - The Photos Carrousel also works perfect
    5 - The search bar filter all the proposed and when the search don't meet the properties it display a message
    6 - Login form when you complete them if you are register it redirects you to a "profile" page with some instructions how to use the website 
    7 - Signup start working on buying the packege, pass throughout stripe payment after payment is made then agent will be able to register
    8 - To add a property agent must fill a form, after form is submited the form turn back into blank fields
    9 - Edit property works similar as add property but by the submission goes back to property details.
    10 - when delete the property it redrect the user back to view properties that is exclusive for agencies logged.

The whole webpage has been tested in a Full Responsive design meaning that it's suitble to PC, Mobile and Tablets. After my deployment to heroku i have
open on my phone and soem configurations don't work properly, but i have passed a link from my herokuapp to my mentor and when he opened on his phone 
it was perfect as i tested in my pc using chome inspect button. All responsive design has been tested in a Chrome inspect button way. 

The emailjs works as it should be deliver the message to the site admin, but when form is submited the all the details stay in form and the page dont 
reload, if the page reload when submit the email the email wont be send, so i decide to leave the page reloading and dont submit a real email but i 
left all the codes on it, i coould do it by django email as well but i dont have a server for email so i decide to use emailjs, but the django email
configurations is in place.

When user click to reset the password after submission appears a message to the user, as i dont have a server to email in django the user
probably wont recieve tha email with the link to reset the password.


### Deployment

The Dployment was made throughout Heroku plataform. Inside heroku plataform was created a Postgree, and some Var configurations
wich is the same keys that we hide in our env.py file pro protect our Keys so other people dont see them when we push to github repository
besucse we ignore the env. Insted use the command line CLI to push the project to Heroku i have made the deploy manualy via plataform dashboard
in the deploy link. For the first time i had no problem in deploy my project everything ran just perfect.

To run Localy:
To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type: `python3 -m http.server`
A blue button should appear to click: *Expose*,
Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 manage.py runserver`
A blue button should appear to click: *Expose*,
Another blue button should appear to click: *Open Browser*.

To view my project deployed click on the link below:
https://golden-estate.herokuapp.com/



### Credits

    - Media 
        - All photos has been download from: https://www.pexels.com/photo/home-real-estate-106399/

    - Acknowledgements
        - I decide to make a real estate website to be a challenge and learn and pratice skills
        - Making this website made me feel a bit work of what can be a work enviroment and gave me more passion about code 
          specialy when you see results, even if what you have done its not as perfect as expected, but im sure the challenge
          during the project as fix some bugs, get stucked in the code and find a solution make me passionate and excited about code.

           


