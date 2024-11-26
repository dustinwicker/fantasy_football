from espn_api.football import League
import pandas as pd

# create separate script
# Increase maximum width in characters of columns - will put all columns in same line in console readout
pd.set_option('expand_frame_repr', False)
# Increase number of rows printed out in console
pd.set_option('display.max_rows', 250)
# Able to read entire value in each column (no longer truncating values)
pd.set_option('display.max_colwidth', None)


def get_public_attributes(obj: object) -> list:
       """Retrieve public attributes of obj."""
       return sorted([x for x in dir(obj) if '__' not in x and '_' not in x])

league = League(league_id=160370,
       year=2011,
       espn_s2=os.environ.get('ESPN_S2'),
       swid=os.environ.get('ESPN_SWID'))


teams = league.teams
for team in teams:
    roster = team.roster
    for player in roster:
        break
    break

roster = team.roster

league_attrib = get_public_attributes(league)
team_attrib = get_public_attributes(team)
player_attrib = get_public_attributes(player)


df = []
for team in teams:
       df.append([team.acquisitions, team.drops, team.losses, team.mov, team.outcomes, team.owners, team.schedule,
                  team.scores, team.standing, team.stats, team.ties, team.trades, team.wins])
pd.DataFrame(df)

team_overall, team_season = [], []
for team in teams:
       team_overall.append([team.owners, team.acquisitions, team.drops, team.losses, team.standing, team.stats,
                            team.ties, team.trades, team.wins])
       team_season.append([team.owners, team.scores, team.mov, team.outcomes, team.roster, team.schedule])
       roster = team.roster
       roster[0]
       for i, p in enumerate(roster):
              for k in p.stats[0].keys():
                     print(p.name, k, p.stats[0].keys(), p.stats[0][k])


player_attrib = get_public_attributes(roster[0])

team_overall = pd.DataFrame(team_overall, columns=['owners', 'acquisitions', 'drops', 'losses', 'standing', 'stats',
                                                   'ties', 'trades', 'wins'])
team_overall.owners = team_overall.owners.apply(lambda x: x[0].get('firstName') + ' ' + x[0].get('lastName'))

team_season = pd.DataFrame(team_season, columns=['owners', 'scores', 'mov', 'outcomes', 'roster', 'schedule'])
team_season.owners = team_season.owners.apply(lambda x: x[0].get('firstName') + ' ' + x[0].get('lastName'))

set(team_attrib) - set(team_overall.columns)


print(league.teams)
d = dir(team)
r = team.roster

[x for x in dir(p) if '__' not in x and '_' not in x]
[x for x in dir(team) if '__' not in x and '_' not in x]
p.stats[0].keys()

teams = league.teams
