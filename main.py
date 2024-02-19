from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

client_names = []

def save_name(name):
    client_names.append(name)

@app.route('/name', methods=['GET', 'POST'])
def display_name():
    if request.method == 'POST':
        name = request.form['name']
        save_name(name)
        return redirect(url_for('next_page'))
    return render_template('index.html', name="")

@app.route('/next_page')
def next_page():
    from main import client_names

    if client_names:
        return render_template('record.html', name=client_names[-1])
    else:
        return render_template('record.html', name="No names available")


if __name__ == "__main__":
    app.run(debug=True)
