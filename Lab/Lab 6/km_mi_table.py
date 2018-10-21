from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def form_example():
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '<table border = 1>\n'
    html += '<th style = "text-align: left">kilometers</th>\n'
    html += '<th style = "text-align: left">miles</th>\n'
    for i in range(10, 110, 10):
        html += '<tr>'
        html += '<td>' + str(i) + '</td>'
        miles = float(i) * 0.6213712
        html += '<td>' + str(miles) + '</td>'
        html += '</tr>'

    html += '</table>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


if __name__ == '__main__':
    app.run()