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
        l.teams

league_data, team_data, roster_data, player_data = [], [], [], []
for l in league:
    l_ = {a: getattr(l, a) for a in get_attributes(l)}
    league_data.append(l_)
    for t in l.teams:
        t_ = {a: getattr(t, a) for a in get_attributes(t)}
        t_['year'] = l.year
        team_data.append(t_)
        for p in t.roster:
            p_ = {a: getattr(p, a) for a in get_attributes(p)}
            p_['year'] = l.year
            player_data.append(p_)

player_data = pd.DataFrame(player_data)
player_data
p = player_data.stats.apply(lambda x: list(x.values()))
p = p[p.apply(lambda x: len(x)>0)]
p.apply(lambda x: len(x)).value_counts()
p.apply(lambda x: x[0].keys())
p = p[p.apply(lambda x: len(x)>1)]
len(p.loc[1400])
p.apply(lambda x: x[1])
p = p[p.apply(lambda x: len(x)>2)]


d = player_data.loc[(player_data.year==2024) & (player_data.position=="D/ST")]
d.reset_index(inplace=True)
for ind, keys in enumerate(d.stats.apply(lambda x: x.keys())):
    capture_info = []
    for key in keys:
        info = d.loc[ind, 'stats'].get(15).keys()
        for i in info:
            print(f'---{i}')
            result = d.loc[ind, 'stats'].get(key).get(i)
            print(result)
            if isinstance(result, float) or (result==0):
                result = [[i], [result]]
            elif isinstance(result, dict):
                result = d.loc[ind, 'stats'].get(key).get(i)
                list(result.keys()), list(result.values())
                result = [list(result.keys()), list(result.values())]
                print(result)
                print(len(result))
            capture_info.append(result)