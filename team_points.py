scores = {}
teams = {}
with open("players.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split()
        name = parts[0]
        points = int(parts[1])
        team = parts[2]
        scores[name] = points
        if team not in teams:
            teams[team] = []
        teams[team].append(name)
print("Scores:", scores)
print("Teams:", teams)

def points_by_team(scores, teams):
    result = {}
    for team in teams:
        total = 0
        for name in teams[team]:
            total += scores[name]
        result[team] = total
    return result
print("Points by team:", points_by_team(scores, teams))