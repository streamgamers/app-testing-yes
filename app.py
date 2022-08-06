from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Post Method"
    else:
        return "Get Method"
