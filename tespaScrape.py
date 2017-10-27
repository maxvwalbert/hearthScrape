import requests
import re
from BeautifulSoup import BeautifulSoup, SoupStrainer

#NOTE TO FUTURE DEVELOPERS:
#These ranges will need to be updated as the tournament progresses
R1_range_start = 90844
R1_range_end = 91044

R2_range_start = 101777
R2_range_end = 101977

R3_range_start = 103278
R3_range_end = 103478

R4_range_start = 104435
R4_range_end = 104635

R5_range_start = 105630
R5_range_end = 105830

opponent_name = raw_input('Opponent team name: ')
print 'fetching your opponent\'s previous matches (this may take a minute)'
print '========================='

print 'round 1 match:'

for i in range(R1_range_start, R1_range_end):
    url = 'https://compete.tespa.org/tournament/83/match/' + str(i)
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    if soup(text=re.compile(opponent_name)) != []:
        print url
        break;

print 'round 2 match:'

for i in range(R2_range_start, R2_range_end):
    url = 'https://compete.tespa.org/tournament/83/match/' + str(i)
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    if soup(text=re.compile(opponent_name)) != []:
        print url
        break

print 'round 3 match:'

for i in range(R3_range_start, R3_range_end):
    url = 'https://compete.tespa.org/tournament/83/match/' + str(i)
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    if soup(text=re.compile(opponent_name)) != []:
        print url
        break

print 'round 4 match:'

for i in range(R4_range_start, R4_range_end):
    url = 'https://compete.tespa.org/tournament/83/match/' + str(i)
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    if soup(text=re.compile(opponent_name)) != []:
        print url
        break

print 'round 5 match:'

for i in range(R5_range_start, R5_range_end):
    url = 'https://compete.tespa.org/tournament/83/match/' + str(i)
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    if soup(text=re.compile(opponent_name)) != []:
        print url
        break