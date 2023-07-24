# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(P, C):
    # Implement your solution here
    # Calculate the maximum number of games that can be played with the given number of players
    max_games_players = P // 2

    # The maximum number of games that can be played simultaneously is the smaller of max_games_players and C
    max_games = min(max_games_players, C)

    return max_games

print(solution(5, 3))

# First compute the maximum number of games possible based on the number of players (each game requires two players),
# and then they return the smaller number of this maximum and the number of available courts.
# The smaller value of the two is the maximum number of games that can be hosted simultaneously.