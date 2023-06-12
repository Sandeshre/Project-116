# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sandesh" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def father_flask():
    nm="Father"
    fag:"40"
    return render_template("father.html",index_variable=nm,index_variable=fag)

# define the route to mother webpage
def mother_flask():
    nm="Mother"
    mag="38"
    return render_template("mother.html",index_variable=nm,index_variable=mag)
# define the route to friends webpage
def friend_flask():
    nm="Friend"
    frag="14"
    return render_template("friend.html",index_variable=nm,index_variable=frag)
# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
