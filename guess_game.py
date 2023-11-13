#Warsztat: Gra w zgadywanie liczb 3
#
#Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy Flaska. Użytkownik dostaje
# do dyspozycji formularz z trzema guzikami: więcej, mniej, trafiłeś.
#
#Informacje o aktualnych zmiennych min i max przechowuj w ukrytych polach formularza (pole typu hidden).
#
#Uwaga - nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla,
# np. przy pomocy Firebuga. Ale w tej sytuacji zupełnie wystarczające, co najwyżej zepsuje sobie zabawę ;)
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__, template_folder='.')

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


def initialize_game():
    session['min'] = 0
    session['max'] = 1000 + 1
    session['guess'] = round((session['max'] - session['min']) / 2) + session['min']


@app.route('/', methods=['GET', 'POST'])
def computer_guess():
    if 'min' not in session:
        initialize_game()

    if request.method == 'POST':
        answers = request.form['choice']

        if answers == "You get it!":
            session.pop('min')
            session.pop('max')
            session.pop('guess')
            return 'I win!!!'
        if answers == 'Too high':
            session['max'] = session['guess']
            session['guess'] = round((session['max'] - session['min']) / 2) + session['min']
        if answers == 'Too low':
            session['min'] = session['guess']
            session['guess'] = round((session['max'] - session['min']) / 2) + session['min']
        if session['min'] == session['max']:
            return "You cheated!"
        return render_template('guess_game.html', max=session['max'], min=session['min'], guess=session['guess'])
    else:
        initialize_game()
        return render_template('guess_game.html', max=session['max'], min=session['min'], guess=session['guess'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

