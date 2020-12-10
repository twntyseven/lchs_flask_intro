from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/hex_form', methods=['GET', 'POST'])
def hex_form():    
    return render_template('hex_form.html')

if __name__ == '__main__':
    app.run()
