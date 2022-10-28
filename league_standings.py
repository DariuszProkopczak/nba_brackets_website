from nba_api.stats.endpoints import leaguestandings
import json


def getStandings():
    # Creates dictionary of conference position to team name for each conference. I.e. east_standings[2] = "Bucks",
    # west_standings[4] = "Lakers". Uses nba_api to get current standings.
    #
    # reference:
    # https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguestandings.py
    # https://github.com/swar/nba_api/blob/001c38958605719995f1bee7ed53899c4ecac5a2/src/nba_api/stats/endpoints/_base.py#L13
    standings_dict = json.loads(leaguestandings.LeagueStandings().get_json())

    east_standings = []
    west_standings = []

    for _ in range(8):
        east_standings.append("")
        west_standings.append("")

    for team in standings_dict["resultSets"][0]["rowSet"]:

        team_name = _mapTeamName(team[4])
        conference = team[5]
        ranking = team[7]

        if ranking <= 8:
            if conference == "East":
                east_standings[ranking - 1] = team_name
            if conference == "West":
                west_standings[ranking - 1] = team_name

    return east_standings, west_standings

def _mapTeamName(team_name):

    if team_name == "Timberwolves":
        return "Twolves"
    if team_name == "Trail Blazers":
        return "Tblazers"
    else:
        return team_name
