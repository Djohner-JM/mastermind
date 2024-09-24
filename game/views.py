from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


from random import choice

from game.models import Game
from game.forms import TurnForm


User = get_user_model()
#CONSTANTS
MSG_WIN = "Félicitations vous avez gagner !"
MSG_LOOSE = "Dommage, vous avez perdu..."
SQUARE_LIST = {"Jaune": f"{chr(0x1F7E8)}",
               "Bleue": f"{chr(0x1F7E6)}",
               "Rouge": f"{chr(0x1F7E5)}",
               "Vert": f"{chr(0x1F7E9)}",
               "Violet": f"{chr(0x1F7EA)}",
               "Marron": f"{chr(0x1F7EB)}",
}
SYMBOLS = [chr(0x1F7E2), chr(0x1F534)]

#VIEWS
def index(request):
    return render(request, "game/index.html")

def new_game(request):
    if request.method == "POST":
        form = TurnForm(request.POST) 
        if form.is_valid():      
            game_id = form.cleaned_data["game_id"]
            user_comb = form.cleaned_data
        
        game = Game.objects.get(id=game_id)
        game.winning_combination = game.winning_combination.replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
        user_comb = [elem for elem in user_comb.values()][:-1]
        display = turn_treatment(user_comb, game.winning_combination)
        game.number_of_turns -= 1
        if game.turns:
            game.turns = game.turns.replace("[","").replace("]","").replace("'","").replace(", ","\n")
        game.turns += display
        game.turns = game.turns.split("\n")
        game.end_game = game.winning_combination == user_comb
        
        if game.end_game or not game.number_of_turns:
            game.msg_end_game = f"{MSG_WIN if game.end_game else MSG_LOOSE}\n La bonne combinaison était {' '.join(SQUARE_LIST[elem] for elem in game.winning_combination)}"       
    else:  
        games = Game.objects.all()
        if len(games) > 25:
            for game in games[10:]:
                game.delete()
        
        game = Game()
        game.winning_combination = [choice([elem for elem in SQUARE_LIST]) for _ in range(4)]
        game.end_game = False
        game.save()
        form = TurnForm(data={"game_id": game.id})
            
    game.save()
    
    return render(request, "game/game.html", context={"form":form,
                                                      "game": game,
                                                      })

#LOGIC
  
def turn_treatment(comb, win_comb):
    indicators = []
    comb_copy = list(comb)
    win_comb_copy = win_comb.copy()

    for i, elem in enumerate(comb):
        if comb[i] == win_comb[i]:
            indicators.append(SYMBOLS[0])
            comb_copy.remove(elem)
            win_comb_copy.remove(elem)

    for i, elem in enumerate(comb_copy):
        if comb_copy[i] in win_comb_copy:
            indicators.append(SYMBOLS[1])
            win_comb_copy.remove(elem)
                  
    return f"{' '.join(SQUARE_LIST[elem] for elem in comb)}: {''.join(indicators)}\n"
