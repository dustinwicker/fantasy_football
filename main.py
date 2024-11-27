import datetime
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
       return sorted([x for x in dir(obj) if not x.startswith('_') if not (x.startswith('__') and x.endswith('__'))])

year_begin, year, _ = 2011, datetime.datetime.today().year, []
for y in range(year_begin, year+1):
    league = League(league_id=160370, year=y,
           espn_s2=os.environ.get('ESPN_S2'),
           swid=os.environ.get('ESPN_SWID'))
    _.extend([league])

#league.box_scores()

currentMatchupPeriod = league.currentMatchupPeriod
league.current_week
league.espn_request
league.finalScoringPeriod
league.firstScoringPeriod
league.free_agents()
league.get_team_data()
league.league_id
league.load_roster_week()
league.logger
league.members
league.message_board

league.nfl_week
league.player_info
league.player_map
league.power_rankings
league.previousSeasons
league.recent_activity
league.refresh
league.refresh_draft
league.scoreboard
league.scoringPeriodId
league.settings
league.standings()
league.standings_weekly
league.year()

league.least_scored_week()
league.least_scorer()
league.most_points_against()
league.top_scored_week()
league.top_scorer()

draft = league.draft
for d in draft:
    break

t_, r_, p_ = [], [], []
for l in _:
    print(f"\n{l}")
    for t in l.teams:
        t_.append([t.owners, t.acquisitions, t.drops, t.losses, t.standing, t.ties, t.trades, t.wins,
                  t.acquisition_budget_spent, t.division_id, t.division_name, t.playoff_pct,
                  t.owners, t.scores, t.mov, t.outcomes, t.roster, t.schedule, t.final_standing, t.get_player_name, t.logo_url, t.playoff_pct,
                    t.points_against, t.points_for, t.schedule, t.scores, t.stats, t.streak_length,
                    t.streak_type, t.team_abbrev, t.team_id, t.team_name, t.waiver_rank, t.stats, t.draft_projected_rank, t.standing])
        for p in t.roster:
            p_.append([p.acquisitionType, p.eligibleSlots, p.injured, p.injuryStatus,
                                p.lineupSlot, p.name, p.onTeamId, p.posRank,
                                p.position,
                                p.proTeam, p.schedule, p.stats])

t = pd.DataFrame(t_)
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
for _ in l:
    break

l_attrib = get_public_attributes(l)
t_attrib = get_public_attributes(t)
p_attrib = get_public_attributes(p)
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
