# CITS3403-Project

## CITS3403 Project: Pixel Perfect

### By Sean Ledesma, Mohammed Maaz Ahmed, Pablo Nayendov, and Cameron Roth.

#### Individual Roles:

Sean: Database management and implementation

Maaz: Server implementation and database reworking

Pablo: Keyboard JS, Statistics Implementation

Cameron: Front-end HTML, CSS, JS

## How to run:
1. Install Python, if you haven't already. This can be done through the official website (https://www.python.org) or through the Microsoft Store.
2. Open command prompt, and navigate to the project folder.
3. Type the command '-r requirements.txt' to install packages/modules.
4. Activate virtual environment by typing 'python3 -m venv venv', followed by 'source venv/bin/activate'.
5. Finally, type 'flask run' into terminal, and the program should start to run. Click or type the link into your favourite browser.

## Design and Development Structure
Our team implemented Agile philosophy in the development of Pixel Perfect. From the outset, we divided ourselves into 4 different groups, chaarcterised by the goal each of us wanted to achieve by the end of the project. 
Cameron was responsible for the front-end, including the HTML, CSS, and JS that the game would plug in to to make the game work. 
Maaz was responsible for the back-end, creating the Flask server and determining the flow of the application server-side. 
Sean was responsible for the Database implementation, creating an efficient database to store usernames, passwords, daily images, and user statistics.
Pablo was responsible for the development of game statistics: what statistics should be used, and how they should be implemented.

We facilitated frequent communication with one another through Discord, allowing us to update each other frequently on progress made, ask for help on stubborn questions, and question each other in a constructive way. We would use scrum meetings every second day in the morning to ensure noone was falling behind and that our goals for the present were aligned.

##Testing
We used the Agile philosophy of constant testing in order to iterate upon our program. From our meetings, we determined several key goals that we wanted the application to achieve. Once these goals were all met and validated, we reconvened to create stretch goals for the application, and built the tests that would confirm achievement of these goals.

Tests for 'PixelPerfect.py', the initialisation function, are available in the 'test' folder, and run on startup of the Flask server. A User DB test is also stored in this folder, to check the adding and deleting of users from the database.

## App Design
The flexible design of Pixel Perfect came about because of a disagreement on what the general theme of the application should be. A compromise was reached, and thus the theme menu was created to house both visions (of Maaz and Cameron), as well as a generic light and dark theme.
The app is designed to be as flexible and easy to navigate as possible. Google Fonts was used to create the striking font pack, and jQuery to make some functions in the index.js and login.js. Bootstrap was used to restrict the application to the middle third of the screen, allowing for a simple port to mobile.

Most of the app is designed client-side, with certain elements being added in through Flask and WTForms. The daily photo, login forms, and user statistics are created and sent to the application via Flask, but everything else is client-side from the outset. This makes the application slower to load on first boot, but responsive once the first load is complete, which was an initial aim of the design.

## App structure:
Images/daily puzzles are stored in the ./app/static/images/images directory.
The names of each image are stored in the database along with its deploy date, pixelfactors,and answer to the puzzle.
Pixelated versions of the daily image will be named 1.png,2.png ... 5.png with 1 being the most pixelated and 5 being the least.
On initialisation of the flask server ('flask run'), the __init__.py will create 3 folders with yesterday's, today's, and tomorrows date through the PixelPerfectinitilization() function.
It will then pull the image names from the database corresponding to these dates. Dates are formated month-day-year with leading zeros.
it will then create 5 versions of each image with varying degrees of the pixelation and store them to the folder corresponding to their date.
Pixelfactors are 5 digits, stored as a string and separated by a '/' in the database. Each digit indicates the degree of pixelation of the image.
JS in the front formats the date client side to match the format in the database, appends it to the image path, and alters the img src in the HTML to display
each image. The image number is incremented with each guess.
After every 25 hours, the create_new_puzzle() function will  be called, which will remove the folder with the date two days from now, and will create another folder with tomorrow's date and will populate it with the daily image corresponding to that date.

The decision to render the pixelated images server side rather than client side was made due to the inefficiency of the pixelation algorithm, and rather than having it be pixelated on the fly for each user everytime on loading, it was decided to render each image once for every user.
