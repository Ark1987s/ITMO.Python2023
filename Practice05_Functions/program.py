import game

name_player1 = game.input_players(1)
name_player2 = game.input_players(2)
total_score = game.game_dice(name_player1, name_player2)
game.winner(name_player1, name_player2, total_score[0], total_score[1])