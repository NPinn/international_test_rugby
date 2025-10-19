<h1><p align="center">International Test Rugby Union Data Project</p></h1>

- Author: [Nathan Pinnock](https://www.linkedin.com/in/nathan-pinnock)
- Version 0.1.3
------
## Project Purpose
- This is a Data Science/Analytics Project looking to build a database of all Rugby Tests played throughout history
- From this; a historical version of world rankings can be calculated alongside replicating World Rugby rankings, as well as head-to-heads and each Nation's/Teams Perfomance
- Tournament Perofmances can also be tracked
------
## Project Logic
- The Logic for this project, as well as any changes in logic over time, can be found in the [Project Logic](./docs/project_logic.md) file
------
## Tasks:
1. _Scrape all rugby matches from the appropraite API (**Complete**)_
    1. _Extract only international matches, using nation team Ids (**Complete**)_
2. Structure Results
    1. This will include properly populating historical scores, especially 19th Century matches
    - Details on scoring are detailed in the [History of Scoring in Rugby Union](./docs/history_of_scoring_in_rugby_union.md) file
3. Set up a database for these results
    - Potentiall using [DuckDB](https://duckdb.org/)?
4. Systematically populate this database with new matches
5. Build Analytics based on these results
    - These analytics will include (but aren't limited to):
    1. World Rankings
        1. Replicate Current World Rankings
        2. Produce Historical Rankings dating back to first International Match
        - Will need to consult World Rugby for how rankings are (and have been) done
    2. Team Performances & Head-To-Heads
    3. Tournament Performances
    4. [Scorigami](https://nflscorigami.com), but Rugby?
    5. All of the above, but using all of the different scoring systems used over time
------
