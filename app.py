from flask import request
from flask import Flask
from pytube import YouTube
import jsonpickle
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
           return "Post Method"
#          yt_video = YouTube(request.form["d_url"])
#          videos = yt_video.streams.filter(only_audio=True).all()
#          res_list = list(videos)
#          return jsonpickle.encode(res_list)
#            return yt_video

        
    else:
        return "Get Method"
    
if __name__ == "__main__":
    app.run(debug =True)
