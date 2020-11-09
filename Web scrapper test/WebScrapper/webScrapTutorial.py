import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta

hackathons = []

url = "https://devpost.com/hackathons?utf8=%E2%9C%93&search=blockchain&challenge_type=all&sort_by=Submission+Deadline"
result = requests.get(
    url
)
src = result.content
soup = BeautifulSoup(src, 'lxml')

featured_challenges = soup.find_all('a', attrs={'data-role' : 'featured_challenge'})

# print(featured_challenges)

for featured_challenge in featured_challenges:
    try:
        timeObj = featured_challenge.find('time', attrs={'class': 'value timeago'})
        time = timeObj.text
        time_left = datetime.strptime(
            time[:-4], "%b %d, %Y %I:%M %p")
        now = datetime.now()
        if now > time_left - timedelta(days=50):
            hackathons.append(featured_challenge.attrs['href']) 
    except:
        continue
    
for hackathon in hackathons:
    print(hackathon)

