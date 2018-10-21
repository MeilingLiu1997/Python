# displays the contents of the dictionary to the user in the form of a table with a table heading for Word and Count.


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
    html += 'Enter:<input type="float" name="input"/>\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


@app.route('/form_input', methods=['Post'])
def form_input():

    string = request.form['input']
    word = {}
    wordsList = string.split()

    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '<table border = 1>\n'
    html += '<th style = "text-align: left">Word</th>\n'
    html += '<th style = "text-align: left">Count</th>\n'
    html += '<tr>'
    for item in wordsList:
        if item not in word:
            word[item] = 1
        else:
            word[item] += 1
    for c in word:
        html += '<td>' + c + '</td>'
        html += '<td>' + str(word[c]) + '</td>'
        html += '</tr>'

    html += '</table>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


if __name__ == '__main__':
    app.run()