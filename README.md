# Fantasy Football

Python tools for analyzing ESPN Fantasy Football league data, including historical stats from 2011 to present.

## Features

- **Historical Data Retrieval** - Pull league data from 2011 to current year
- **Team & Player Analysis** - Extract detailed stats for all teams and rostered players
- **Free Agent Analysis** - Analyze available free agents by position
- **Defense/Special Teams (D/ST) Focus** - Specialized analysis for D/ST positions

## Setup

### Prerequisites

- Python 3.x
- ESPN Fantasy Football account with league access

### Installation

```bash
pip install espn-api pandas
```

### Environment Variables

You'll need your ESPN authentication cookies. To find these:
1. Log into ESPN Fantasy Football in your browser
2. Open Developer Tools → Application → Cookies
3. Find `espn_s2` and `SWID` values

```bash
export ESPN_S2="your-espn-s2-cookie"
export ESPN_SWID="your-swid-cookie"
```

## Usage

```python
from espn_api.football import League
import os

# Connect to your league
league = League(
    league_id=160370,  # Replace with your league ID
    year=2024,
    espn_s2=os.environ.get('ESPN_S2'),
    swid=os.environ.get('ESPN_SWID')
)

# Access teams
for team in league.teams:
    print(f"{team.team_name}: {team.wins}-{team.losses}")

# Get free agents
free_agents = league.free_agents(position='D/ST')
```

## Data Extracted

| Data Type | Description |
|-----------|-------------|
| League Data | Settings, scoring, schedule |
| Team Data | Wins, losses, points, roster |
| Player Data | Stats, projections, position |
| Free Agents | Available players by position |

## License

MIT
