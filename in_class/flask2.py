from flask import Flask
from flask import request

app = Flask(__name__)

app.debug = True


@app.route('/')
def form_example():
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '<form method="Post" action = "form_input">\n'
    html += 'First Name: <input type="text" name="first_name"/>\n'
    html += '<p>\n'
    html += 'Last Name: <input type="text" name="last_name"/>\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


@app.route('/form_input', methods = ['Post'])
def form_input():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += 'Your name:' + first_name + '' + last_name + '\n'
    html += '</body>\n'
    html += '</html>\n'
    return html
if __name__== '__main__':
    app.run()