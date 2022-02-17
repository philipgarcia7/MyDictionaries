WS = open("WorldSeriesWinners.txt", "r")
WS1 = open("WorldSeriesWinners.txt", "r")

teamnum = {}
yearteam = {}
result = 0
for team in WS:
    team = team.strip()
    if team in teamnum:
        teamnum[team] += 1
    else:
        teamnum[team] = 1

year = 1902

for y in WS1:
    y = y.strip()
    if year == 1903:
        year += 2
        yearteam[year] = y
    elif year == 1993:
        year += 2
        yearteam[year] = y
    else:
        year += 1
        yearteam[year] = y
print(teamnum)
print(teamnum[team])
print(yearteam)

user_year = int(input("What year do you want to know the World Series winner of? "))
if user_year == 1904 or user_year == 1994:
    print("There was no World Series in that year")


else:
    y = user_year
    print(
        "The team that won in "
        + str(y)
        + " was "
        + str(yearteam[y])
        + ". They have "
        + str(teamnum[team])
        + " total wins."
    )
