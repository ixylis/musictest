from flask import Flask
app = Flask(__name__)
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask import request, render_template
import mps_youtube
import urllib.request
from bs4 import BeautifulSoup

class RegistrationForm(Form):
    url = StringField('URL')
class YoutubeSearchForm(Form):
    searchTerm = StringField('Search Term')

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
        url = "https://www.youtube.com/watch?v=lX44CAz-JhU"
        mps_youtube.commands.play.play_url(url, "")
        return "Hello"
        
    return render_template('register.html', form=form)

@app.route('/search', methods=['Get', 'POST'])
def search():
    form = YoutubeSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        query=form.searchTerm.data
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        results = {}
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            #results[vid['title']]=vid['href'][vid['href'].index("="):-1]
            try:
                i = vid['href'].index("=")
            except:
                i=-1
            if(i!=-1):
                results[vid['title']]=vid['href'][i+1:]
        return render_template('searchresults.html', result=results)
    return render_template('register.html', form=form)

@app.route('/addsong/<href>')
def addsong(href):
    url = "https://www.youtube.com/watch?v="+href
    mps_youtube.commands.play.play_url(url, "")
    return url

if __name__=="__main__":
    app.run()
