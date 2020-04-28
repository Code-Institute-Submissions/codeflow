from flask import Flask, render_template, url_for


app = Flask(__name__)

projects = [
    {
        'owner': "Sue Holder",
        'title': "Flask Web App",
        'brief': "Web App project brief",
        'date_posted': 'April 27, 2020'
    },
    {
        'owner': "John Doe",
        'title': "Static Website",
        'brief': "Website project brief",
        'date_posted': 'April 26, 2020'
    },
    {
        'owner': "Jane Doe",
        'title': "E-commerce Website",
        'brief': "E-commerce project brief",
        'date_posted': 'April 25, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/")
@app.route("/projects")
def project():
    return render_template('projects.html', title='Projects', projects=projects)


@app.route("/register")
def register():
    return render_template('register.html', title='Register')
