import requests
import re
from BeautifulSoup import BeautifulSoup, SoupStrainer

#NOTE TO FUTURE DEVELOPERS:
#These ranges will need to be updated as the tournament progresses
range_start = 90934#90744
range_end = 90954#105730

opponent_name = raw_input('Opponent team name: ')
print 'fetching your opponent\'s previous matches (this may take a minute)'
print '========================='

for i in range(range_start, range_end):
    url = 'https://compete.tespa.org/tournament/83/match/' + str(i)
    response = requests.get(url)
    html = response.content

    product = SoupStrainer('div',{'id': 'player1Container', 'id': 'player2Container'})

    soup = BeautifulSoup(html, parseOnlyThese=product)
    if soup(text=re.compile(opponent_name)) != []:
        print url