import os
from flask import Flask, render_template  # request


app = Flask(__name__)


@app.route("/")
def do_this():
    return "Hello World"


@app.route("/banana")
def banana():
    return "banana"


def get_the_usernames_of_the_people_in_the_class():
    return ["Anna", "Davie", "Jon", "Louie", "Marcus", "Tristan", "Marc"]


@app.route("/class")
def get_class():

    student_a = "Mark"
    student_b = "Brigit"
    student_c = "Romeo"

    my_class = student_a + " " + student_b + " " + student_c

    return my_class


@app.route("/orange")
def orange():
    return render_template("orange.html")


@app.route("/greeting")
def greeting():
    title = "Some title"
    names = get_the_usernames_of_the_people_in_the_class()  # some data coming from some database
    return render_template("greeting.html", names=names, title=title)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
