from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)

from main import client_names

def save_name(name):
    client_names.append(name)

@app.route('/next_page')
def next_page():
    if request.method == 'POST':
        name = request.form['name']
        save_name(name)
        return redirect(url_for('record'))
    return render_template('record.html', name="")

    


if __name__ == "__main__":
    app.run(debug=True)
