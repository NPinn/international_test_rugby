# Project Logic

- This document will be used to track the logic behind the decisions made for this project
- Version 0.1.0
------
## Logic Evolution
### Original Logic (2025-09-18)
- The original thought behind this process was to scrape all the matches and tournaments from the [List of Women's Test Matches Wikipedia page](https://en.wikipedia.org/wiki/List_of_women%27s_international_rugby_union_test_matches).
    - The initial scrape of this was successful, with all matches being scraped, as well as tournament names
    - However, recursively searching for Wikipedia page names based on the tournament names proved to require too much manual review, both in terms of confirming the correct page name had been identfied, as well as the correct matches from those pages/page sections

### Updated Match Extraction Logic (2025-10-07)
- Due to the non-systematic manner in which the Wikipedia scraping process worked, another avenue of extracting matches was searched for
- An API to pull all matches (including non-internationals) was found, and used as new source for this project
    - This also allowed for both Women's and Men's matches to be processed concurrently
------
## Scoring
- The Scoring Sysems used over the history of Rugby Union has changed over time. The details and implementation logic can be found in the latest [History of Scoring in Rugby Union](./history_of_scoring_in_rugby_union_latest.md) file.
### Updates to Scoring
- 2025-10-19:
    - Upon investigating the data in more detail, it was found that matches upto the [1889 Home Nations Championship](https://en.wikipedia.org/wiki/1889_Home_Nations_Championship) were using Scoring System 2, based on [Version 1](../legacy/docs/history_of_scoring_in_rugby_union_v1.md) of the Scoring Documentation File
- 2025-11-02:
    - With Further investigation, it was discovered that Scoring System 2 was used until the [1890 Home Nations Championship](https://en.wikipedia.org/wiki/1890_Home_Nations_Championship), with Scoring System 3 only applying for the [1891 Home Nations Championship](https://en.wikipedia.org/wiki/1891_Home_Nations_Championship), and Scoring System 4 applied for the [1892](https://en.wikipedia.org/wiki/1892_Home_Nations_Championship) and [1893](https://en.wikipedia.org/wiki/1893_Home_Nations_Championship) Home Nations Championships
------