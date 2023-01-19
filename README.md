# Welcome to Likha!

Likha is a pretty simple tool. It's a writing application that forces you to be creative!

Here there are **no backspaces**, **no grammar highlighting**, and **no chances to hold yourself back**.

Writers can be our own biggest impediment. We bog ourselves down, constantly rethinking the scraps of thoughts we manage to type out before deleting them and starting a new. In the process we snuff out any potential sparks of creativity. People say the cure to writers block is to just write, and thats where Likha comes in.
Likha frees you from the self imposed line edits and overthinking. All you can do is write and keep writing.


## How to start
Head over to https://likha-app.herokuapp.com/ and make an account. Then go to [create](https://likha-app.herokuapp.com/create) to start writing. The "just write" settings can be toggled on and off and when you're done just save your work to view and and continue later.


## The code itself

Likha is written *almost* entirely in flask.

### Flask
Likha follows the flask blueprint approach separation of concerns. Main.py handles the non security routes, while those can be found in auth.py. 
SQL-Alchemy and SQLite are used for the models.
The frontend UI is rendered on the server through templates.
TLS security is enforced via flask-talisman.
### Javascript
In the app.py you can find the only non python part of this project- a simple javascript function that prevents the use of the backspace and delete keys.
### Deployment
The application is currently deployed to Heroku using Hypercorn for the WSGI server.


## Development Status

### Live

 - Editor with "no backspace" mode
 - Ability to save your work and view it later

### In development

 - Removal of grammer highlighting
 - Timer for edit and edit free modes
 - Ability to open and edit previous work
 - Ability to follow other users
 - Google drive integration

## Next steps
Likha really started as an idea for a tool that I would want to use in my own writing. I couldn't find one that I loved out there already and decided to build one!
The plan is for Likha to be a seed for a fully featured world building application but that's a ways away.

Hopefully it scratches an itch for other writers as well!

