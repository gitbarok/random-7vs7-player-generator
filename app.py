import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('index.html')
 
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/result')
def get_value():
    argument = request.args.to_dict()
    player = argument['player']
    player = player.split()

    keeper = argument['keeper']
    keeper = keeper.split()

    team = {}
    TOTAL_PLAYER = 6
    TEAM_NUMBER=1
    while (len(player) or len(keeper)) > 0:
        team[TEAM_NUMBER] = {}
        team[TEAM_NUMBER]['player'] = []
        team[TEAM_NUMBER]['keeper'] = []
        for i in range(TOTAL_PLAYER):
            if not len(player) == 0:
                p = random.choice(player)
                team[TEAM_NUMBER]['player'].append(p)
                player.remove(p)
            else:
                team[TEAM_NUMBER]['player'].append('No-Player')

        if not len(keeper) == 0:
            k = random.choice(keeper)
            team[TEAM_NUMBER]['keeper'].append(k)
            keeper.remove(k)
        else:
            team[TEAM_NUMBER]['keeper'].append('No-Kiper')
        TEAM_NUMBER = TEAM_NUMBER + 1
    # return team
    return render_template('formations.html', team=team)



if __name__ == "__main__":
    app.run()