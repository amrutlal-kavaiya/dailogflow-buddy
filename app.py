from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/intent')
def intent():
    return render_template('intent.html')

@app.route('/entities')
def entities():
    return render_template('entities.html')

@app.route('/animation')
def animation():
    return render_template('aanimation.html')

# ...additional routes if needed...

if __name__ == '__main__':
    app.run(debug=True)
