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


# vars()
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

# players on teams, not all (need to get free agents)
player_data = pd.DataFrame(player_data)

d = player_data.loc[(player_data.year==2024) & (player_data.position=="D/ST")]
d.reset_index(inplace=True, drop=True)
capture_info = []
for ind, keys in enumerate(d.stats.apply(lambda x: x.keys())):
    capture_ind_info = {}
    for key in keys:
        info = d.loc[ind, 'stats'].get(key).keys()
        for i in info:
            result = d.loc[ind, 'stats'].get(key).get(i)
            if isinstance(result, float) or (result==0):
                result = {i: result}
                capture_ind_info.update(result)
            elif isinstance(result, dict):
                result = d.loc[ind, 'stats'].get(key).get(i)
                for k, v in result.items():
                    r = {k: v}
                    capture_ind_info.update(r)
    capture_info.append(capture_ind_info)
df = pd.DataFrame(capture_info)
d = d.merge(df, left_index=True, right_index=True)

capture_info = []
free_agents = l.free_agents(position='D/ST')
for index, free_agent in enumerate(free_agents):
    capture_free_agent_info = {}
    free_agent_available_data = vars(free_agent)
    for key, value in free_agent_available_data.items():
        if isinstance(value, float) or isinstance(value, str) or (value == 0):
            result = {key: value}
            capture_free_agent_info.update(result)
        elif isinstance(value, dict):
            free_agent_available_data = value
            for key, value in free_agent_available_data.items():
                if isinstance(value, float) or isinstance(value, str) or (value == 0):
                    result = {key: value}
                    capture_free_agent_info.update(result)
                elif isinstance(value, dict):
                    free_agent_available_data = value
                    for key, value in free_agent_available_data.items():
                        if isinstance(value, float) or isinstance(value, str) or (value == 0):
                            result = {key: value}
                            capture_free_agent_info.update(result)
                        elif isinstance(value, dict):
                            free_agent_available_data = value
                            for key, value in free_agent_available_data.items():
                                if isinstance(value, float) or isinstance(value, str) or (value == 0):
                                    result = {key: value}
                                    capture_free_agent_info.update(result)
                                elif isinstance(value, dict):
                                    print(result)
    capture_info.append(capture_free_agent_info)
df_ = pd.DataFrame(capture_info)

cols = sorted(set(d.columns) & set(df_.columns))
d = d[cols]
df_ = df_[cols]
df = pd.concat([d, df_])