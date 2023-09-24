from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Shaprizal Ibrahim',
        'title' : 'First Blog Title',
        'content' : 'First blog post',
        'date_posted' : 'September 23, 2023'
    },
    {
        'author' : 'Priska Andini',
        'title' : 'Second Blog Title',
        'content' : 'Second blog post',
        'date_posted' : 'September 24, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About Us')

if __name__ == '__main__':
    app.run(debug = True)