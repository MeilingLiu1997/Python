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
    html += 'Fahrenheit: <input type="text" temperature="Fahrenheit"/>\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


@app.route('/form_input', methods = ['Post'])
def form_input():
    Fahrenheit = request.form['Fahrenheit']
    #Celsius = 5/9(Fahrenheit-32)
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += 'Fahrenheit:' + Fahrenheit +'\n'
    html += '<body>\n'
    html += '<html>\n'
    return html
if __name__== '__main__':
    app.run()