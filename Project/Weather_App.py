from flask import Flask
from flask import request
import pyowm

app = Flask(__name__)
owm = pyowm.OWM('5f5493c5a13e45bab8f9280cfb23f911')


def getWeather(city, country):
    location = city + ',' + country
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    return w.get_temperature('fahrenheit')


@app.route('/form_input', methods = ['POST'])
def form_input():
    city = request.form['city']
    country = request.form['country']
    temperature = getWeather(city, country)
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += 'City: ' + city + '<br>Country: ' + country + '\n'
    html += ''
    html += '<p>The max temp is:' + str(temperature['temp_max']) + '\n'
    html += '<p>The current temp is:' + str(temperature['temp']) + '\n'
    html += '<p>The minimum temp is:' + str(temperature['temp_min']) + '\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method= "POST" action = "form_input">\n'
    html += 'City:<input type = "text" name = "city" />\n'
    html += '<p>\n'
    html += 'Country:<input type = "text" name = "country" />\n'
    html += '<p>\n'
    html += '<input type = "submit" value = "submit" />\n'
    html += '</form>\n'
    html += '</body></html>'
    return html

if __name__ == '__main__':
    app.run()