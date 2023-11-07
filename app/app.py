from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote = request.form['quote']
        author = request.form['author']
        requests.post('http://api:5001/api/quotes', json={'quote': quote, 'author': author})
        return redirect(url_for('index'))
    else:
        quotes = requests.get('http://api:5001/api/quotes').json()
        return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
