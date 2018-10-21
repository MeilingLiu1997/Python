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
    html += 'Kilometers: <input type="float" name="kilometers"/>\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


def calulate(form_example):
    miles = float(form_example) * 0.6213712
    mile = format(miles, '.3f')
    return mile


@app.route('/form_input', methods=['Post'])
def form_input():
    kilometers = request.form['kilometers']
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += 'You entered' + ' ' + str(kilometers) + ' ' + 'kilometers. \n The equivalent in miles is' + ' ' + str(calulate(kilometers)) + '\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


if __name__ == '__main__':
    app.run()