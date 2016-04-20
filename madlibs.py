from random import choice

from flask import Flask, render_template, request, make_response


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    html = render_template("compliment.html",
                               person=player,
                               compliment=compliment,
                               )
    resp = make_response(html)
    resp.set_cookie('player', 'person')

    return resp

@app.route('/game')
def show_game_form():
    """play a game"""

    play = request.args.get("game")
    player = request.args.get("person")

    player = request.cookies['player']

    if play == 'yes':
        return render_template("game.html",
                                )
    else:
        return render_template("goodbye.html",
                                person=player,
                                )


@app.route('/madlib')
def show_madlib():
    """creates story"""

    frienemy = request.args.get("people")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template("madlib.html",
                        people=frienemy,
                        color=color,
                        noun=noun,
                        adjective=adjective,
                        )

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
