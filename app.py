from pytube import YouTube
from flask import request
# from flask import Flask

# import jsonpickle
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
#            return request.form['d_url']
         yt_video = YouTube(str(request.form["d_url"]))
         return yr_video.title
#          videos = yt_video.streams
#          res_list = list(videos)
#          return jsonpickle.encode(res_list)
#            return yt_video

        
    else:
        return request.args.get('d_url')
    
if __name__ == "__main__":
    app.run(debug =True)
