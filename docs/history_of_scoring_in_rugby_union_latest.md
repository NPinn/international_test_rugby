# The History of Scoring in Rugby Union
-----
## Updated: 2025-10-19
## Version: 2.0.1
-----
- The history of scoring in Rugby Union is a fascinating subject, and has seen numerous changes since the inception of rugby
    - For instance, the first 14 years of international rugby saw matches decided by the number of goals scored, rather than the number of points scored
- The table highlighted in this [Wikipedia Page](https://en.wikipedia.org/wiki/History_of_rugby_union#Scoring) page will act as the guide for changes in scoring
    - This data is sourced from [Rugby Football History](https://www.rugbyfootballhistory.com/), specifically their page on [Scoring Through the Ages](https://www.rugbyfootballhistory.com/scoring.htm)
- Upon Investigating the data, it was found that matches up to 1889 were using Scoring System 2
- [Previous Version of this file](history_of_scoring_in_rugby_union_v1.md)
-----
## Scoring over Time
| Date | Try | Conversion | Penalty | Dropped Goal | Goal From Mark | Scoring System | Notes | Date Range |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 1871 - 1875 | No Score | 1 Goal | 1 Goal | 1 Goal | N/A | 1 | Matches decided by a majority of Goals. A Try was required to score a conversion-goal | `matchDate <= 1875-12-31` |
| 1876 - 1889 | 1 Try | 1 Goal | 1 Goal | 1 Goal | N/A | 2 | Like above, but if number of Goals were equal, the number of Tries was used as a tie-breaker | `matchDate` between `1876-01-01` & `1889-12-31` |
| 1890 - 1891 | 1 Point | 2 Points | 3 Points | 3 Points | N/A | 3 | All Tests played in 1891 were played as a part of the [1891 Home Nations Championship](https://en.wikipedia.org/wiki/1891_Home_Nations_Championship#Scoring_system), which used Scoring System 3 | `matchDate` between `1890-01-01` & `1891-12-31` |
| 1891 - 1894 | 2 Points | 3 Points | 3 Points | 4 Points | 4 Points | 4 | | `matchDate` between `1892-01-01` & `1893-12-31` |
| 1894 - 1904 | 3 Points | 2 Points | 3 Points | 4 Points | 4 Points | 5 | All Tests played in 1894 were played as a part of the [1894 Home Nations Championship](https://en.wikipedia.org/wiki/1894_Home_Nations_Championship#Scoring_system), which used Scoring System 5 | `matchDate` between `1894-01-01` & `1904-12-31` |
| 1905 - 1947 | 3 Points | 2 Points | 3 Points | 4 Points | 3 Points | 6 | | `matchDate` between `1905-01-01` & `1947-12-31` |
| 1948 - 1970 | 3 Points | 2 Points | 3 Points | 3 Points | 3 Points | 7 | | `matchDate` between `1948-01-01` & `1970-12-31` |
| 1971 - 1977 | 4 Points | 2 Points | 3 Points | 3 Points | 3 Points | 8 | The last [_Goal From Mark_](https://en.wikipedia.org/wiki/Goal_from_mark) was scored by Romania against France on 1971-12-11. This means that, for practical purposes, 1971 is the only year that meets Scoring System 8 | `matchDate` between `1970-01-01` & `1971-12-31` |
| 1977 - 1991 | 4 Points | 2 Points | 3 Points | 3 Points | N/A | 9 | As the only diference between Scoring System 9 and Scoring System 8 is the fact that the [_Goal From Mark_](https://en.wikipedia.org/wiki/Goal_from_mark) was replaced by the Free Kick Law in 1977, and the last Goal From Mark was kicked in 1971, this scoring system can be applied to all matches from 1972 to 1991 | `matchDate` between `1972-01-01` & `1991-12-31` |
| 1992 - Present | 5 Points | 2 Points | 3 Points | 3 Points | N/A | 10 | | `matchDate >= 1992-01-01` |

-----
