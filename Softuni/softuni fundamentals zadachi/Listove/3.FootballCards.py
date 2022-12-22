info = input()
list = info.split()
list_team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for el in list:
    element = el.split("-")
    team = element[0]
    player = int(element[1])
    if team == "A":
        if player in list_team_A:
            list_team_A.remove(player)
    elif team == "B":
        if player in list_team_B:
            list_team_B.remove(player)
    if len(list_team_A) < 7 or len(list_team_B) < 7:
        break

print(f"Team A - {len(list_team_A)}; Team B - {len(list_team_B)}")

if len(list_team_A) < 7 or len(list_team_B) < 7:
    print("Game was terminated")