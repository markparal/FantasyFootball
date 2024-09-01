import numpy as np
import pandas as pd
import cvxpy as cp
from dataclasses import dataclass
from enum import Enum

# Player Cap Definitions
TOTAL_PLAYERS = 16          # Total players on team
MAX_QB = 3                  # Maximum allowable Quarterbacks
MIN_QB = 1                  # Minimum allowable Quarterbacks
MAX_RB = 6                  # Maximum allowable Running Backs
MIN_RB = 4                  # Minimum allowable Running Backs
MAX_WR = 7                  # Maximum allowable Wide Receivers
MIN_WR = 4                  # Minimum allowable Wide Receivers
MAX_TE = 3                  # Maximum allowable Tight Ends
MIN_TE = 1                  # Minimum allowable Tight Ends
MAX_K = 1                   # Maximum allowable Kickers
MIN_K = 1                   # Minimum allowable Kickers

# Points breakdown for league
PASS_YD_POINTS = 0.05       # Fantasy points per passing yard
PASS_TD_POINTS = 4          # Fantasy points per passing touchdown
PASS_INT_POINTS = -2        # Fantasy points per passing interception
RUSH_YD_POINTS = 0.1        # Fantasy points per rushing yard
RUSH_TD_POINTS = 6          # Fantasy points per rushing touchdown
REC_YD_POINTS = 0.1         # Fantasy points per receiving yard
REC_POINTS = 1              # Fantasy points per reception
REC_TD_POINTS = 6           # Fantasy points per receiving touchdown
FUMBLE_POINTS = -2          # Fantasy points per fumble

@dataclass
class Position(Enum):
    QB = "QB"               # Quarterback
    RB = "RB"               # Running Back
    WR = "WR"               # Wide Receiver
    TE = "TE"               # Tight End
    K = "K"                 # Kicker
    DEF = "DEF"             # Defense

@dataclass
class player:
    name: str               # Player name
    position: Position      # Player position
    age: float              # Player age
    pass_yds: float         # Passing yards
    pass_tds: float         # Passing touchdowns
    pass_ints: float        # Passing interceptions
    rush_yds: float         # Rushing yards
    rush_tds: float         # Rushing touchdowns
    rec_yds: float          # Receiving yards
    rec_tds: float          # Receiving touchdowns
    rec_tot: float          # Total receptions
    fum: float              # Fumbles lost

def read_player_stats(csv:str):
    """
    Given csv containing player stats for a given year, build player profiles.

    Parameters
    ----------
    csv: str
        Address of csv containing player statistics for a given year
    
    Returns
    -------
    draftees: list
        List of player objects describing each player in the given statistics csv
    draftee_name: list
        List of strings containing the player names from the csv file
    """
    # Read csv into dataframe
    df = pd.read_csv(csv,skiprows=1)

    # Player name
    draftee_name = df.iloc[:,1].tolist()
    draftee_name = [n.replace('*','').replace('+','') for n in draftee_name]

    # Player position
    draftee_position = df.iloc[:,3].tolist()

    # Player age
    draftee_age = df.iloc[:,4].tolist()

    # Player passing yards
    draftee_pass_yds = df.iloc[:,9].tolist()

    # Player passing TDs
    draftee_pass_tds = df.iloc[:,10].tolist()

    # Player passing Ints
    draftee_pass_ints = df.iloc[:,11].tolist()

    # Player rushing yards
    draftee_rush_yds = df.iloc[:,13].tolist()

    # Player rushing TDs
    draftee_rush_tds = df.iloc[:,15].tolist()

    # Player receiving yards
    draftee_rec_yds = df.iloc[:,18].tolist()

    # Player receptions
    draftee_rec_tot = df.iloc[:,17].tolist()

    # Player receiving TDs
    draftee_rec_tds = df.iloc[:,20].tolist()

    # Player fumbles (unrecovered)
    draftee_fum = df.iloc[:,22].tolist()

    # Create player profiles
    draftees = list()
    for _i in range(len(draftee_name)):
        draftees.append(player(
            name=str(draftee_name[_i]),
            position=str(draftee_position[_i]),
            age=float(draftee_age[_i]),
            pass_yds=float(draftee_pass_yds[_i]),
            pass_tds=float(draftee_pass_tds[_i]),
            pass_ints=float(draftee_pass_ints[_i]),
            rush_yds=float(draftee_rush_yds[_i]),
            rush_tds=float(draftee_rush_tds[_i]),
            rec_yds=float(draftee_rec_yds[_i]),
            rec_tds=float(draftee_rec_tds[_i]),
            rec_tot=float(draftee_rec_tot[_i]),
            fum=float(draftee_fum[_i])
        ))

    return draftees,draftee_name

def merge_player_stats():
    """
    Given a list of the 
    """

if __name__ == "__main__":
    # Inputs
    first_season_year = 2020
    current_season_year = 2024
    drafted_players_csv = "players_drafted.csv"

    # Get data csv files
    stat_dir = "Player_Statistics/"
    seasons_csv = [stat_dir+str(season)+".csv" for season in range(first_season_year,current_season_year)]

    # Get all potential players to draft (for now no rookies, only players from last year)
    # Read last years data TODO Add 2pt conversions?
    df = pd.read_csv(seasons_csv[-1],skiprows=1)
    drafted_players = pd.read_csv(drafted_players_csv, header=None).values.flatten().tolist()

    # Player name
    draftee_name = df.iloc[:,1].tolist()
    draftee_name = [n.replace('*','').replace('+','') for n in draftee_name]

    # Player position
    draftee_position = df.iloc[:,3].tolist()

    # Player age
    draftee_age = df.iloc[:,4].tolist()
    draftee_age = [float(age)+1. for age in draftee_age]

    # Player passing yards
    draftee_pass_yds = df.iloc[:,9].tolist()
    draftee_pass_yds = [float(yds) for yds in draftee_pass_yds]

    # Player passing TDs
    draftee_pass_tds = df.iloc[:,10].tolist()
    draftee_pass_tds = [float(tds) for tds in draftee_pass_tds]

    # Player passing Ints
    draftee_pass_ints = df.iloc[:,11].tolist()
    draftee_pass_ints = [float(ints) for ints in draftee_pass_ints]

    # Player rushing yards
    draftee_rush_yds = df.iloc[:,13].tolist()
    draftee_rush_yds = [float(yds) for yds in draftee_rush_yds]

    # Player rushing TDs
    draftee_rush_tds = df.iloc[:,15].tolist()
    draftee_rush_tds = [float(tds) for tds in draftee_rush_tds]

    # Player receiving yards
    draftee_rec_yds = df.iloc[:,18].tolist()
    draftee_rec_yds = [float(yds) for yds in draftee_rec_yds]

    # Player receptions
    draftee_rec_tot = df.iloc[:,17].tolist()
    draftee_rec_tot = [float(rec) for rec in draftee_rec_tot]

    # Player receiving TDs
    draftee_rec_tds = df.iloc[:,20].tolist()
    draftee_rec_tds = [float(tds) for tds in draftee_rec_tds]

    # Player fumbles (unrecovered)
    draftee_fum = df.iloc[:,22].tolist()
    draftee_fum = [float(fum) for fum in draftee_fum]

    # Player seasons of data
    draftee_seasons = [1] * len(draftee_name)

    # Now step through the rest of the data and add to the data
    for _i in range(len(seasons_csv)-1):
        # Read data csv
        df = pd.read_csv(seasons_csv[-1],skiprows=1)

        # Player name
        name_temp = df.iloc[:,1].tolist()
        name_temp = [n.replace('*','').replace('+','') for n in name_temp]

        # Player passing yards
        pass_yds_temp = df.iloc[:,9].tolist()
        pass_yds_temp = [float(yds) for yds in pass_yds_temp]

        # Player passing TDs
        pass_tds_temp = df.iloc[:,10].tolist()
        pass_tds_temp = [float(tds) for tds in pass_tds_temp]

        # Player passing Ints
        pass_ints_temp = df.iloc[:,11].tolist()
        pass_ints_temp = [float(ints) for ints in pass_ints_temp]

        # Player rushing yards
        rush_yds_temp = df.iloc[:,13].tolist()
        rush_yds_temp = [float(yds) for yds in rush_yds_temp]

        # Player rushing TDs
        rush_tds_temp = df.iloc[:,15].tolist()
        rush_tds_temp = [float(tds) for tds in rush_tds_temp]

        # Player receiving yards
        rec_yds_temp = df.iloc[:,18].tolist()
        rec_yds_temp = [float(yds) for yds in rec_yds_temp]

        # Player receptions
        rec_tot_temp = df.iloc[:,17].tolist()
        rec_tot_temp = [float(rec) for rec in rec_tot_temp]

        # Player receiving TDs
        rec_tds_temp = df.iloc[:,20].tolist()
        rec_tds_temp = [float(tds) for tds in rec_tds_temp]

        # Player fumbles (unrecovered)
        fum_temp = df.iloc[:,22].tolist()
        fum_temp = [float(fum) for fum in fum_temp]

        # Add data to existing players (don't care about players who didn't play last year)
        for _j in range(len(name_temp)):
            try:
                # Check if player played in 2023
                draft_indx = draftee_name.index(name_temp[_j])

                # Add stats
                draftee_pass_yds[draft_indx] += pass_yds_temp[_j]
                draftee_pass_tds[draft_indx] += pass_tds_temp[_j]
                draftee_pass_ints[draft_indx] += pass_ints_temp[_j]
                draftee_rush_yds[draft_indx] += rush_yds_temp[_j]
                draftee_rush_tds[draft_indx] += rush_tds_temp[_j]
                draftee_rec_yds[draft_indx] += rec_yds_temp[_j]
                draftee_rec_tot[draft_indx] += rec_tot_temp[_j]
                draftee_rec_tds[draft_indx] += rec_tds_temp[_j]
                draftee_fum[draft_indx] += fum_temp[_j]

                # Record season played
                draftee_seasons[draft_indx] += 1
            except:
                continue

    # Remove already drafted players
    for _i in range(len(drafted_players)):
        try:
            # Check if player played in 2023
            draft_indx = draftee_name.index(str(drafted_players[_i]))

            # Zero out all entries
            draftee_pass_yds[draft_indx] = 0.
            draftee_pass_tds[draft_indx] = 0.
            draftee_pass_ints[draft_indx] = 0.
            draftee_rush_yds[draft_indx] = 0.
            draftee_rush_tds[draft_indx] = 0.
            draftee_rec_yds[draft_indx] = 0.
            draftee_rec_tot[draft_indx] = 0.
            draftee_rec_tds[draft_indx] = 0.
            draftee_fum[draft_indx] = 0.
        except:
            continue

    # Get average stats
    draftee_pass_yds_avg = [0.] * len(draftee_name)
    draftee_pass_tds_avg = [0.] * len(draftee_name)
    draftee_pass_ints_avg = [0.] * len(draftee_name)
    draftee_rush_yds_avg = [0.] * len(draftee_name)
    draftee_rush_tds_avg = [0.] * len(draftee_name)
    draftee_rec_yds_avg = [0.] * len(draftee_name)
    draftee_rec_tot_avg = [0.] * len(draftee_name)
    draftee_rec_tds_avg = [0.] * len(draftee_name)
    draftee_fum_avg = [0.] * len(draftee_name)
    for _i in range(len(draftee_name)):
        draftee_pass_yds_avg[_i] = draftee_pass_yds[_i] / draftee_seasons[_i]
        draftee_pass_tds_avg[_i] = draftee_pass_tds[_i] / draftee_seasons[_i]
        draftee_pass_ints_avg[_i] = draftee_pass_ints[_i] / draftee_seasons[_i]
        draftee_rush_yds_avg[_i] = draftee_rush_yds[_i] / draftee_seasons[_i]
        draftee_rush_tds_avg[_i] = draftee_rush_tds[_i] / draftee_seasons[_i]
        draftee_rec_yds_avg[_i] = draftee_rec_yds[_i] / draftee_seasons[_i]
        draftee_rec_tot_avg[_i] = draftee_rec_tot[_i] / draftee_seasons[_i]
        draftee_rec_tds_avg[_i] = draftee_rec_tds[_i] / draftee_seasons[_i]
        draftee_fum_avg[_i] = draftee_fum[_i] / draftee_seasons[_i]

    # Split players into position arrays
    # QBs
    qb_name = np.zeros(0)
    qb_pass_yds_avg = np.zeros(0)
    qb_pass_tds_avg = np.zeros(0)
    qb_pass_ints_avg = np.zeros(0)
    qb_rush_yds_avg = np.zeros(0)
    qb_rush_tds_avg = np.zeros(0)
    qb_rec_yds_avg = np.zeros(0)
    qb_rec_tot_avg = np.zeros(0)
    qb_rec_tds_avg = np.zeros(0)
    qb_fum_avg = np.zeros(0)
    for _i in range(len(draftee_position)):
        if draftee_position[_i] == "QB":
            qb_name = np.append(qb_name,draftee_name[_i])
            qb_pass_yds_avg = np.append(qb_pass_yds_avg,draftee_pass_yds_avg[_i])
            qb_pass_tds_avg = np.append(qb_pass_tds_avg,draftee_pass_tds_avg[_i])
            qb_pass_ints_avg = np.append(qb_pass_ints_avg,draftee_pass_ints_avg[_i])
            qb_rush_yds_avg = np.append(qb_rush_yds_avg,draftee_rush_yds_avg[_i])
            qb_rush_tds_avg = np.append(qb_rush_tds_avg,draftee_rush_tds_avg[_i])
            qb_rec_yds_avg = np.append(qb_rec_yds_avg,draftee_rec_yds_avg[_i])
            qb_rec_tot_avg = np.append(qb_rec_tot_avg,draftee_rec_tot_avg[_i])
            qb_rec_tds_avg = np.append(qb_rec_tds_avg,draftee_rec_tds_avg[_i])
            qb_fum_avg = np.append(qb_fum_avg,draftee_fum_avg[_i])

    # RBs
    rb_name = np.zeros(0)
    rb_pass_yds_avg = np.zeros(0)
    rb_pass_tds_avg = np.zeros(0)
    rb_pass_ints_avg = np.zeros(0)
    rb_rush_yds_avg = np.zeros(0)
    rb_rush_tds_avg = np.zeros(0)
    rb_rec_yds_avg = np.zeros(0)
    rb_rec_tot_avg = np.zeros(0)
    rb_rec_tds_avg = np.zeros(0)
    rb_fum_avg = np.zeros(0)
    for _i in range(len(draftee_position)):
        if draftee_position[_i] == "RB":
            rb_name = np.append(rb_name,draftee_name[_i])
            rb_pass_yds_avg = np.append(rb_pass_yds_avg,draftee_pass_yds_avg[_i])
            rb_pass_tds_avg = np.append(rb_pass_tds_avg,draftee_pass_tds_avg[_i])
            rb_pass_ints_avg = np.append(rb_pass_ints_avg,draftee_pass_ints_avg[_i])
            rb_rush_yds_avg = np.append(rb_rush_yds_avg,draftee_rush_yds_avg[_i])
            rb_rush_tds_avg = np.append(rb_rush_tds_avg,draftee_rush_tds_avg[_i])
            rb_rec_yds_avg = np.append(rb_rec_yds_avg,draftee_rec_yds_avg[_i])
            rb_rec_tot_avg = np.append(rb_rec_tot_avg,draftee_rec_tot_avg[_i])
            rb_rec_tds_avg = np.append(rb_rec_tds_avg,draftee_rec_tds_avg[_i])
            rb_fum_avg = np.append(rb_fum_avg,draftee_fum_avg[_i])

    # WRs
    wr_name = np.zeros(0)
    wr_pass_yds_avg = np.zeros(0)
    wr_pass_tds_avg = np.zeros(0)
    wr_pass_ints_avg = np.zeros(0)
    wr_rush_yds_avg = np.zeros(0)
    wr_rush_tds_avg = np.zeros(0)
    wr_rec_yds_avg = np.zeros(0)
    wr_rec_tot_avg = np.zeros(0)
    wr_rec_tds_avg = np.zeros(0)
    wr_fum_avg = np.zeros(0)
    for _i in range(len(draftee_position)):
        if draftee_position[_i] == "WR":
            wr_name = np.append(wr_name,draftee_name[_i])
            wr_pass_yds_avg = np.append(wr_pass_yds_avg,draftee_pass_yds_avg[_i])
            wr_pass_tds_avg = np.append(wr_pass_tds_avg,draftee_pass_tds_avg[_i])
            wr_pass_ints_avg = np.append(wr_pass_ints_avg,draftee_pass_ints_avg[_i])
            wr_rush_yds_avg = np.append(wr_rush_yds_avg,draftee_rush_yds_avg[_i])
            wr_rush_tds_avg = np.append(wr_rush_tds_avg,draftee_rush_tds_avg[_i])
            wr_rec_yds_avg = np.append(wr_rec_yds_avg,draftee_rec_yds_avg[_i])
            wr_rec_tot_avg = np.append(wr_rec_tot_avg,draftee_rec_tot_avg[_i])
            wr_rec_tds_avg = np.append(wr_rec_tds_avg,draftee_rec_tds_avg[_i])
            wr_fum_avg = np.append(wr_fum_avg,draftee_fum_avg[_i])

    # TEs
    te_name = np.zeros(0)
    te_pass_yds_avg = np.zeros(0)
    te_pass_tds_avg = np.zeros(0)
    te_pass_ints_avg = np.zeros(0)
    te_rush_yds_avg = np.zeros(0)
    te_rush_tds_avg = np.zeros(0)
    te_rec_yds_avg = np.zeros(0)
    te_rec_tot_avg = np.zeros(0)
    te_rec_tds_avg = np.zeros(0)
    te_fum_avg = np.zeros(0)
    for _i in range(len(draftee_position)):
        if draftee_position[_i] == "TE":
            te_name = np.append(te_name,draftee_name[_i])
            te_pass_yds_avg = np.append(te_pass_yds_avg,draftee_pass_yds_avg[_i])
            te_pass_tds_avg = np.append(te_pass_tds_avg,draftee_pass_tds_avg[_i])
            te_pass_ints_avg = np.append(te_pass_ints_avg,draftee_pass_ints_avg[_i])
            te_rush_yds_avg = np.append(te_rush_yds_avg,draftee_rush_yds_avg[_i])
            te_rush_tds_avg = np.append(te_rush_tds_avg,draftee_rush_tds_avg[_i])
            te_rec_yds_avg = np.append(te_rec_yds_avg,draftee_rec_yds_avg[_i])
            te_rec_tot_avg = np.append(te_rec_tot_avg,draftee_rec_tot_avg[_i])
            te_rec_tds_avg = np.append(te_rec_tds_avg,draftee_rec_tds_avg[_i])
            te_fum_avg = np.append(te_fum_avg,draftee_fum_avg[_i])

    # Create convex variables for each position
    qbs = cp.Variable(np.shape(qb_name)[0],boolean=True)
    qb_count = cp.Variable()
    rbs = cp.Variable(np.shape(rb_name)[0],boolean=True)
    rb_count = cp.Variable()
    wrs = cp.Variable(np.shape(wr_name)[0],boolean=True)
    wr_count = cp.Variable()
    tes = cp.Variable(np.shape(te_name)[0],boolean=True)
    te_count = cp.Variable()

    # Create objective (maximize TDs)
    obj = qbs@(PASS_YD_POINTS*qb_pass_yds_avg + PASS_TD_POINTS*qb_pass_tds_avg + \
            PASS_INT_POINTS*qb_pass_ints_avg + RUSH_YD_POINTS*qb_rush_yds_avg + \
            RUSH_TD_POINTS*qb_rush_tds_avg + REC_YD_POINTS*qb_rec_yds_avg + \
            REC_POINTS*qb_rec_tot_avg + REC_TD_POINTS*qb_rec_tds_avg + \
            FUMBLE_POINTS*qb_fum_avg)
    obj += rbs@(PASS_YD_POINTS*rb_pass_yds_avg + PASS_TD_POINTS*rb_pass_tds_avg + \
            PASS_INT_POINTS*rb_pass_ints_avg + RUSH_YD_POINTS*rb_rush_yds_avg + \
            RUSH_TD_POINTS*rb_rush_tds_avg + REC_YD_POINTS*rb_rec_yds_avg + \
            REC_POINTS*rb_rec_tot_avg + REC_TD_POINTS*rb_rec_tds_avg + \
            FUMBLE_POINTS*rb_fum_avg)
    obj += wrs@(PASS_YD_POINTS*wr_pass_yds_avg + PASS_TD_POINTS*wr_pass_tds_avg + \
            PASS_INT_POINTS*wr_pass_ints_avg + RUSH_YD_POINTS*wr_rush_yds_avg + \
            RUSH_TD_POINTS*wr_rush_tds_avg + REC_YD_POINTS*wr_rec_yds_avg + \
            REC_POINTS*wr_rec_tot_avg + REC_TD_POINTS*wr_rec_tds_avg + \
            FUMBLE_POINTS*wr_fum_avg)
    obj += tes@(PASS_YD_POINTS*te_pass_yds_avg + PASS_TD_POINTS*te_pass_tds_avg + \
            PASS_INT_POINTS*te_pass_ints_avg + RUSH_YD_POINTS*te_rush_yds_avg + \
            RUSH_TD_POINTS*te_rush_tds_avg + REC_YD_POINTS*te_rec_yds_avg + \
            REC_POINTS*te_rec_tot_avg + REC_TD_POINTS*te_rec_tds_avg + \
            FUMBLE_POINTS*te_fum_avg)
    objective = cp.Maximize(obj)

    # Constrain the convex problem
    constraints = [
        cp.sum(qbs) >= MIN_QB,
        cp.sum(qbs) <= MAX_QB,
        cp.sum(rbs) >= MIN_RB,
        cp.sum(rbs) <= MAX_RB,
        cp.sum(wrs) >= MIN_WR,
        cp.sum(wrs) <= MAX_WR,
        cp.sum(tes) >= MIN_TE,
        cp.sum(tes) <= MAX_TE,
        cp.sum(qbs) + cp.sum(rbs) + cp.sum(wrs) + cp.sum(tes) == TOTAL_PLAYERS
    ]

    # Create convex problem
    problem = cp.Problem(
        objective=objective,
        constraints=constraints
    )

    # Solve problem
    problem.solve()

    # Print players with associated avg TDs
    # QBs
    total_QBs = int(np.linalg.norm(qbs.value,1))
    print("\nNumber of QBs: " + str(total_QBs))
    for _i in range(len(qbs.value)):
        if qbs.value[_i]:
            avg_fantasy_value = PASS_YD_POINTS*qb_pass_yds_avg[_i] + PASS_TD_POINTS*qb_pass_tds_avg[_i] + \
                                PASS_INT_POINTS*qb_pass_ints_avg[_i] + RUSH_YD_POINTS*qb_rush_yds_avg[_i] + \
                                RUSH_TD_POINTS*qb_rush_tds_avg[_i] + REC_YD_POINTS*qb_rec_yds_avg[_i] + \
                                REC_POINTS*qb_rec_tot_avg[_i] + REC_TD_POINTS*qb_rec_tds_avg[_i] + \
                                FUMBLE_POINTS*qb_fum_avg[_i]
            print(" " + str(qb_name[_i]) + ":\n   -Value: " + str(avg_fantasy_value))

    # RBs
    total_RBs = int(np.linalg.norm(rbs.value,1))
    print("\nNumber of RBs: " + str(total_RBs))
    for _i in range(len(rbs.value)):
        if rbs.value[_i]:
            avg_fantasy_value = PASS_YD_POINTS*rb_pass_yds_avg[_i] + PASS_TD_POINTS*rb_pass_tds_avg[_i] + \
                                PASS_INT_POINTS*rb_pass_ints_avg[_i] + RUSH_YD_POINTS*rb_rush_yds_avg[_i] + \
                                RUSH_TD_POINTS*rb_rush_tds_avg[_i] + REC_YD_POINTS*rb_rec_yds_avg[_i] + \
                                REC_POINTS*rb_rec_tot_avg[_i] + REC_TD_POINTS*rb_rec_tds_avg[_i] + \
                                FUMBLE_POINTS*rb_fum_avg[_i]
            print(" " + str(rb_name[_i]) + ":\n   -Value: " + str(avg_fantasy_value))

    # WRs
    total_WRs = int(np.linalg.norm(wrs.value,1))
    print("\nNumber of WRs: " + str(total_WRs))
    for _i in range(len(wrs.value)):
        if wrs.value[_i]:
            avg_fantasy_value = PASS_YD_POINTS*wr_pass_yds_avg[_i] + PASS_TD_POINTS*wr_pass_tds_avg[_i] + \
                                PASS_INT_POINTS*wr_pass_ints_avg[_i] + RUSH_YD_POINTS*wr_rush_yds_avg[_i] + \
                                RUSH_TD_POINTS*wr_rush_tds_avg[_i] + REC_YD_POINTS*wr_rec_yds_avg[_i] + \
                                REC_POINTS*wr_rec_tot_avg[_i] + REC_TD_POINTS*wr_rec_tds_avg[_i] + \
                                FUMBLE_POINTS*wr_fum_avg[_i]
            print(" " + str(wr_name[_i]) + ":\n   -Value: " + str(avg_fantasy_value))

    # TEs
    total_TEs = int(np.linalg.norm(tes.value,1))
    print("\nNumber of TEs: " + str(total_TEs))
    for _i in range(len(tes.value)):
        if tes.value[_i]:
            avg_fantasy_value = PASS_YD_POINTS*te_pass_yds_avg[_i] + PASS_TD_POINTS*te_pass_tds_avg[_i] + \
                                PASS_INT_POINTS*te_pass_ints_avg[_i] + RUSH_YD_POINTS*te_rush_yds_avg[_i] + \
                                RUSH_TD_POINTS*te_rush_tds_avg[_i] + REC_YD_POINTS*te_rec_yds_avg[_i] + \
                                REC_POINTS*te_rec_tot_avg[_i] + REC_TD_POINTS*te_rec_tds_avg[_i] + \
                                FUMBLE_POINTS*te_fum_avg[_i]
            print(" " + str(te_name[_i]) + ":\n   -Value: " + str(avg_fantasy_value))