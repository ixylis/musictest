from flask import Flask
app = Flask(__name__)
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask import request, render_template
import mps_youtube

class RegistrationForm(Form):
    url = StringField('URL')
    #username = StringField('Username', [validators.Length(min=4, max=25)])
    #email = StringField('Email Address', [validators.Length(min=6, max=35)])
    #password = PasswordField('New Password', [
    #    validators.DataRequired(),
    #    validators.EqualTo('confirm', message='Passwords must match')
    #])
    #confirm = PasswordField('Repeat Password')
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.url.data)
        mps_youtube.commands.play.play_url(url, override)
        return "Hello"
        
    return render_template('register.html', form=form)
