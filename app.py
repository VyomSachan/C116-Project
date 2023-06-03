from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Vyom Sachan" # write your name
    age = "18 Years" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Himanshu Sachan" # write your name
    age = "45 Years" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Pallavi Sachan" # write your name
    age = "45 Years" # write your age

    return render_template('mother.html' , name = name , age = age)

# define the route to brother webpage
@app.route("/brother")
def brother():
    name = "Harshit Sachan" # write your name
    age = "13 Years" # write your age

    return render_template('brother.html' , name = name , age = age)

if __name__  ==  '__main__':
    app.run(debug=True)
