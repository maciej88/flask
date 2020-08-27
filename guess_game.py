#Warsztat: Gra w zgadywanie liczb 3
#
#Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy Flaska. Użytkownik dostaje
# do dyspozycji formularz z trzema guzikami: więcej, mniej, trafiłeś.
#
#Informacje o aktualnych zmiennych min i max przechowuj w ukrytych polach formularza (pole typu hidden).
#
#Uwaga - nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla,
# np. przy pomocy Firebuga. Ale w tej sytuacji zupełnie wystarczające, co najwyżej zepsuje sobie zabawę ;)
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')
min = 0
max = 1000 + 1
guess = round((max - min) / 2) + min

@app.route('/', methods=['GET', 'POST'])

def computer_guess():
    global min
    global max
    global guess

    if request.method == 'POST':
        answers = request.form['choice']

        if answers == "You get it!":
            return 'I win!!!'
        if answers == 'Too high':
            max = guess
            guess = round((max - min) / 2) + min
        if answers == 'Too low':
            min = guess
            guess = round((max - min) / 2) + min
        if min == max or min == 1000 or min >= max:
            return "don't cheat!"
        if min == max:
            return "don't cheat!"
        return render_template('guess_game.html', max=max, min=min, guess=guess)
    else:
        return render_template('guess_game.html', max=max, min=min, guess=guess)

if __name__ == '__main__':
    app.run(debug=True)
