from flask import request
from flask import Flask
from pytube import YouTube
import jsonpickle
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.form['d_url']
#         yt_video = YouTube(url)
#         videos = yt_video.streams.filter(only_audio=True).all()
#         res_list = list(videos)
#         return jsonpickle.encode(res_list)

        
    else:
        return "Get Method"
    
if __name__ == "__main__":
    app.run(debug =True)
