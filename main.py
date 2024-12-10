import datetime
from espn_api.football import League
import pandas as pd
import os

# create separate script
# Increase maximum width in characters of columns - will put all columns in same line in console readout
pd.set_option('expand_frame_repr', False)
# Increase number of rows printed out in console
pd.set_option('display.max_rows', 250)
# Able to read entire value in each column (no longer truncating values)
pd.set_option('display.max_colwidth', None)


def get_attributes(obj: object) -> list:
       """Retrieve attributes of obj."""
       return sorted([x for x in dir(obj) if not x.startswith('_') if not (x.startswith('__') and x.endswith('__'))])

year_begin, year, league = 2011, datetime.datetime.today().year, []
for y in range(year_begin, year+1):
    _ = League(league_id=160370, year=y, espn_s2=os.environ.get('ESPN_S2'), swid=os.environ.get('ESPN_SWID'))
    league.extend([_])

for ind, l in enumerate(league):
    if ind == 0:
        league_attrib = get_attributes(l)

league_data, team_data, roster_data, player_data = [], [], [], []
for ind,l in enumerate(league):
    if ind == 0:
        league_attrib = get_attributes(l)
    l_ = {a: getattr(l, a) for a in league_attrib}
    league_data.append(l_)
    for ind, t in enumerate(league.teams:
        t_d = {a: getattr(t, a) for a in t_attrib}
        t_.append(t_d)
        for p in t.roster:
            p_d = {a: getattr(p, a) for a in p_attrib}
            p_.append(p_d)










draft = league.draft
for d in draft:
    break

for l in _:
    break

for p in t.roster:
    break

l_attrib = get_attributes(l)
t_attrib = get_attributes(t)
p_attrib = get_attributes(p)



l = pd.DataFrame(l_)
t = pd.DataFrame(t_)
p = pd.DataFrame(p_)
t[0] = t[0].apply(lambda x: x[0].get('firstName') + ' ' + x[0].get('lastName'))

c = ['owners', 'acquisitions', 'drops', 'losses', 'standing','ties', 'trades', 'wins', 'acquisition_budget_spent',
     'division_id', 'division_name', 'playoff_pct']
t_= t.iloc[:, :len(c)]
t_.columns = c

['owners', 'scores', 'mov', 'outcomes', 'roster', 'schedule']

scoreboard = league.scoreboard(1)
for score in scoreboard:
    break

l = league.settings









score_attrib = get_public_attributes(score)
d_attrib = get_public_attributes(d)
l_attrib = get_public_attributes(l)


df = []
for team in teams:
       df.append([team.acquisitions, team.drops, team.losses, team.mov, team.outcomes, team.owners, team.schedule,
                  team.scores, team.standing, team.stats, team.ties, team.trades, team.wins])
pd.DataFrame(df)

team_overall, team_season = [], []
player_list = []
for team in teams:
       team_overall.append([team.owners, team.acquisitions, team.drops, team.losses, team.standing, team.stats,
                            team.ties, team.trades, team.wins])
       team_season.append([team.owners, team.scores, team.mov, team.outcomes, team.roster, team.schedule])
       roster = team.roster
       for player in roster:
           player_list.append([player.acquisitionType, player.eligibleSlots, player.injured, player.injuryStatus,
                    player.lineupSlot, player.name, player.onTeamId, player.playerId, player.posRank, player.position,
                    player.proTeam, player.schedule, player.stats])


team_overall = pd.DataFrame(team_overall, columns=)
team_overall.owners = team_overall.owners.apply(lambda x: x[0].get('firstName') + ' ' + x[0].get('lastName'))

team_season = pd.DataFrame(team_season, columns=)


player = pd.DataFrame(player_list)

set(team_attrib) - set(team_overall.columns)


print(league.teams)
d = dir(team)
r = team.roster

[x for x in dir(p) if '__' not in x and '_' not in x]
[x for x in dir(team) if '__' not in x and '_' not in x]
p.stats[0].keys()

teams = league.teams
