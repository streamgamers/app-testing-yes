
from flask import Flask, jsonify, request
from pytube import YouTube
import jsonpickle
app = Flask(__name__)

@app.route('/youtube', methods=['POST'])
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    url = request.form['d_url']
    yt_video = YouTube(url)
    videos = yt_video.streams
    res_list = list(enumerate(videos))
    j = jsonpickle.encode(res_list)

    return j

    
    
    
if __name__ == "__app__":
    app.run(debug =True)
