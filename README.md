# Fantasy Football Drafting Optimizer

## Summary
This code uses convex optimization to build for the best possible fantasy football team based on user provided historical data. 

## Convex Problem
To pose the building of a fantasy football team as a convex problem, we first need to define a goal. Our goal is to maximize the total projected fantasy value of the team given a set of constraints on player types and number of players. The convex problem is fully characterized by the convex variables, the objective function, and the constraints.

### Convex Variables:
- $\bar{Q}$ is a vector of boolean values in which each element corresponds to a potential quarterback option
- $\bar{R}$ is a vector of boolean values in which each element corresponds to a potential running back option
- $\bar{W}$ is a vector of boolean values in which each element corresponds to a potential wide receiver option
- $\bar{T}$ is a vector of boolean values in which each element corresponds to a potential tight end option

### Convex Constraints:
- $\sum\bar{Q} \le Q_{max}$
- $\sum\bar{Q} \ge Q_{min}$
- $\sum\bar{R} \le R_{max}$
- $\sum\bar{R} \ge R_{min}$
- $\sum\bar{W} \le W_{max}$
- $\sum\bar{W} \ge W_{min}$
- $\sum\bar{T} \le T_{max}$
- $\sum\bar{T} \ge T_{min}$
- $\sum\bar{Q} + \sum\bar{R} + \sum\bar{W} + \sum\bar{T} = P_{total}$ 

where
- $Q_{max}$ is a scalar corresponding to the maximum allowable quarterbacks on a roster
- $Q_{min}$ is a scalar corresponding to the minimum allowable quarterbacks on a roster
- $R_{max}$ is a scalar corresponding to the maximum allowable running backs on a roster
- $R_{min}$ is a scalar corresponding to the minimum allowable running backs on a roster
- $W_{max}$ is a scalar corresponding to the maximum allowable wide receivers on a roster
- $W_{min}$ is a scalar corresponding to the minimum allowable wide receivers on a roster
- $T_{max}$ is a scalar corresponding to the maximum allowable tight ends on a roster
- $T_{min}$ is a scalar corresponding to the minimum allowable tight ends on a roster
- $P_{total}$ is a scalar corresponding to the total allowable players on a roster

### Convex Objective Function:
- $\max_{} f(x)$

where
- $f(x) = \bar{Q} Q_{fv} + \bar{R} R_{fv} + \bar{W} W_{fv} + \bar{T} T_{fv}$
- $Q_{fv}$ is a vector in which each element corresponds to the projected fantasy value of the potential quarterback options
- $R_{fv}$ is a vector in which each element corresponds to the projected fantasy value of the potential running back options
- $W_{fv}$ is a vector in which each element corresponds to the projected fantasy value of the potential wide receiver options
- $T_{fv}$ is a vector in which each element corresponds to the projected fantasy value of the potential tight end options

## Data Sources
NFL player statistics should be provided for an entire season and stored in the `Player_Statistics/` directory.

There are many possible options online for NFL statistics. One potential source is from [Pro-Football Reference](https://www.pro-football-reference.com/). If you wish to use this data, please follow their provided [guidelines](https://www.sports-reference.com/data_use.html) and use at your own risk/discretion. 

## Tasklist
- Add 2pt conversion compensation in calculation
- Add injury compensation
- Add rookies and performance predictions
- Add compensation for draft order
- Recommend what player to draft next 
- Add a better method for removing drafted players from solver
- Add kickers
- Add compensation for team/players on that team (stealing ball time, providing ball time)