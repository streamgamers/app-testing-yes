from flask import request
from flask import Flask
from pytube import YouTube
import jsonpickle
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        url = request.form['d_url']
        yt_video = YouTube(url)
        videos = yt_video.streams
        res_list = list(enumerate(videos))
        j = jsonpickle.encode(res_list)

        return j
        
    else:
        return "Get Method"
    
if __name__ == "__main__":
    app.run(debug =True)
