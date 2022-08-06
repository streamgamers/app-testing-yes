from flask import request
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Post Method"
    else:
        return "Get Method"
    
if __name__ == "__main__":
    app.run(debug =True)
