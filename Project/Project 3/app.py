from flask import Flask
import tmdbsimple as tmdb
from flask import request

app = Flask(__name__)
tmdb.API_KEY = '2fcfbb28e86668ee1578a9814a747a51'


@app.route('/form_input', methods=['POST'])
def form_input():
    search1 = request.form['search']
    search = tmdb.Search()
    response = search.movie(query=search1)
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '<table border = 1>\n'
    html += '<th style = "text-align: left">Movie Name</th>\n'
    html += '<th style = "text-align: left">Popularity</th>\n'
    html += '<th style = "text-align: left">Release date</th>\n'
    html += '<th style = "text-align: left">Movie ID</th>\n'
    for s in search.results:
        html += '<tr>'
        html += '<td>' + '<p>' + str(s['title']) + '</td>'
        html += '<td>' + '<p>' + str(s['popularity']) + '</td>'
        html += '<td>' + '<p>' + str(s['release_date']) + '</td>'
        html += '<td>' + '<p>' + str(s['id']) + '</td>'
        html += '</tr>'
    html += '</table>\n'

    html += '<p>1.Which of the Star Wars movie is the most popular?'+'\n'
    search = tmdb.Search()
    response = search.movie(query='the Star Wars')
    listp = []
    listt = []
    for s in search.results:
        listp.append(s['popularity'])
        listt.append(s['title'])
    i = 0
    while listp[i] != listp[len(listp) - 1] and i < len(listp):
        if listp[i] > listp[i + 1]:
            listp[i + 1] = listp[i]
            listt[i + 1] = listt[i]
        else:
            i += 1
    html += '<p>' + str(listt[i]) + '\n'
    answers = open('answers.txt', 'a')
    answers.write('a1: '+ '\n')
    answers.write(str(listt[i]) + '\n')
    answers.close()

    html += '<p>2.Which of the two movies, according to their popularity score, was more popular - ' \
            'Toy Story or Finding Nemo?'+'\n'
    search = tmdb.Search()
    response = search.movie(query='Toy Story')
    listT = []
    for s in search.results:
        listT.append(s['popularity'])
    response = search.movie(query='Finding Nemo')
    listF = []
    for s in search.results:
        listF.append(s['popularity'])
    if listT[0] < listF[0]:
        html += '<p>' + 'Finding Nemo'+'\n'
    else:
        html += '<p>' + 'Toy Story' + '\n'
    answers = open('answers.txt', 'a')
    answers.write('a2: '+ '\n')
    answers.write('Finding Nemo'+ '\n')
    answers.close()

    html += '<p>3.Which was the first X-men movie ever made and when was it released?'+'\n'
    search = tmdb.Search()
    response = search.movie(query='X-men')
    listD = []
    listTitle = []
    for s in search.results:
        listD.append(s["release_date"])
        listTitle.append(s['title'])
    i = 0
    listD.remove('')
    listD.remove('1978-01-01')
    while listD[i] != listD[len(listD)-1] and i < len(listD):
        if listD[i] < listD[i + 1]:
            listD[i + 1] = listD[i]
            listTitle[i+1] = listTitle[i]
        else:
            i += 1
    html += '<p>' + str(listTitle[i]) + '; ' + 'Release Date:' + str(listD[i]) + '\n'
    answers = open('answers.txt', 'a')
    answers.write('a3: '+ '\n')
    answers.write(str(listTitle[i]) + '; ' + 'Release Date:' + str(listD[i]) + '\n')
    answers.close()



    html += '<p>4.List one other interesting fact that you found about a movie or a movie franchise of your choice.'+'\n'
    search = tmdb.Search()
    response = search.movie(query='X-men')
    listpopular = []
    listTitle = []
    for s in search.results:
        listpopular.append(s["popularity"])
        listTitle.append(s['title'])
    i = 0
    while listpopular[i] != listpopular[len(listp) - 1] and i < len(listpopular):
        if listpopular[i] > listpopular[i + 1]:
            listpopular[i + 1] = listpopular[i]
            listTitle[i + 1] = listTitle[i]
        else:
            i += 1

    html += '<p> The most popular of the Star War:' + str(listt[i])+'\n'
    html += '<p> The most popular of the X-men:' + str(listTitle[i])+'\n'
    html += '<p>'+str(listTitle[i])+ ' '+ 'is more popular than'+' '+ str(listt[i])+'\n'
    answers = open('answers.txt', 'a')
    answers.write('a4: '+ '\n')
    answers.write('The most popular of the Star War:' + str(listt[i])+ '\n')
    answers.write('The most popular of the X-men:' + str(listTitle[i])+ '\n')
    answers.write(str(listTitle[i]) + ' ' + 'is more popular than' + ' ' + str(listt[i]) + '\n')
    answers.close()

    html += '<a href="/">'+'\n'+'Back</a>'
    html += '</body>\n'
    html += '</html>\n'
    return html


@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method= "POST" action = "form_input">\n'
    html += 'Search:<input type = "text" name = "search" />\n'
    html += '<p>\n'
    html += '<input type = "submit" value = "submit" />\n'
    html += '</form>\n'
    html += '</body></html>'
    return html

if __name__ == '__main__':
    app.run()