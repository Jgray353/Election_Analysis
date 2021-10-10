# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate won. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10, Visual Studio Code, 1.61.0

## Summary of candidate results
The analysis of the election shows that:
- There were 369711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85213 votes.
    - Diana DeGette received 73.8% of the vote and 272892 votes. 
    - Raymon Anthony Doane received 3.1% of the vote and 11606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272892 votes.

## Challenge Overview
With the votes counted and a winner determined, the challenge task was to go a step further and complete the following tasks.
1. Get voter turnout for each county.
2.  Getperentage of votes from each county out of the total count
3.  Get the county with the highest voter turnout.

## Sumnmary of county results
- The 369711 votes cast in the election are from 3 counties.
   - The counties were:
    - Jefferson
    - Denver
    - Arapahoe
- The county results were:
    - Jefferson county accounted for 38855 votes, which was 10.5% of the total votes cast.
    - Denver county accounted for 38855 votes, which was 82.8% of the total votes cast.
    - Denver county accounted for 24801 votes, which was 6.7% of the total votes cast.
- The county with the highest voter turnout was:     
    - Denver county, which accounted for 24801 votes, which was 6.7% of the total votes cast.

## ChallengeSummary
This code, with minor modification, can be used for just about any election. In the code, things like 'county' can be modified if it's for measuring results by city, state, zip code, etc. You can declare a new value and then edit accordingly throughout the code to ensure it's properly referenced. And of course you likely will have to edit in a new variable for the file name at the top of the code. And you can edit in something else for 'candidate name', like if you're calulcating results for a government propostion or measure. This code is very versatile for election results with little modification. 


