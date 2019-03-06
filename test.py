import mps_youtube

url = "https://www.youtube.com/watch?v=lX44CAz-JhU"
#parturl = "https://www.youtube.com/playlist?list=PLNndIWxzLYvrRUgTMMf01zD8lmjncB7Gr"
parturl = "https://www.youtube.com/playlist?list=PLNndIWxzLYvqtC-LEorUQcE_PMQMnVEms"
#mps_youtube.commands.play.play_url(parturl,"")
#songrange = mps_youtube.commands.search.search("gao")
#while(True):
#    mps_youtube.commands.songlist.plist(parturl)
    #mps_youtube.commands.play.play("","1")
#mps_youtube.commands.songlist.songlist_rm_add("rm", "1")
#mps_youtube.commands.local_playlist.ls()
#mps_youtube.commands.misc.view_history()
#while(True):
#mps_youtube.commands.play.play_pl("musicpi")
#songrange = mps_youtube.commands.search.yt_url(url, print_title=0)
#mps_youtube.commands.songlist.songlist_rm_add("add", songrange)
#songrange = mps_youtube.commands.songlist.plist(parturl)
#print(songrange)
#mps_youtube.player.play_range(songrange)
#print(mps_youtube.commands.songlist.dump(""))
#mps_youtube.commands.play.play_url(url, "")

import urllib.request
from bs4 import BeautifulSoup

textToSearch = 'hello world'
#query = urllib.parse.quote(textToSearch)
query="gao"
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    print(vid['title'])
    print('https://www.youtube.com' + vid['href'])
