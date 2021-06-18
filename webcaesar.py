from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/user_message')
def user_message():    
    return render_template('user_message.html')

if __name__ == '__main__':
    app.run()

# Instructions for this project can be found here:
# https://education.launchcode.org/lchs/chapters/flask-intro/project.html
