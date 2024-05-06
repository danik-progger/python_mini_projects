from flask import Flask, render_template, flash, redirect, url_for
from forms.login import LoginForm
from forms.register import RegistrationForm

app = Flask(__name__)

app.config['SECRTET_KEY'] = '029df72e72e3730d230dfffc036f1473'

posts = [
    {
        'author': 'Jane Austin',
        'body': 'Beautiful is better than ugly',
        'date': 'September 14th 2023',

    }, {
        'author': 'Sheckspire',
        'body': 'To be or not to be',
        'date': 'June 1st 1904'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('templates/home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('templates/about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}')
        return redirect(url_for('home'))
    return render_template('templates/register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('templates/login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
