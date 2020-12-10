from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

# Code the 'valid_hex_chars' function here:

@app.route('/hex_form')
def hex_form():    
    return render_template('hex_form.html')

if __name__ == '__main__':
    app.run()

# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
