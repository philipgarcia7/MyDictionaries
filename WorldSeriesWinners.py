WS = open("WorldSeriesWinners.txt", "r")
# year = input("What year do you want the know the World Series Winner or?:")
ws_count = 0
teamnum = {}
yearteam = {}

for team in WS:
    team = team.strip()
    if team in yearteam:
        y += 1
    if team in teamnum:
        teamnum[team] += 1
    else:
        teamnum[team] = 1

for year in range(1903, 2009):
    if year != 1904 and 1994:
        yearteam[year][teamnum] = [team]

print(teamnum)
print(yearteam)
