import requests
from bs4 import BeautifulSoup

url = "https://www40.zippyshare.com/v/FJjX9P5J/file.html"
#the url is the zippyshare url

url_content = requests.get(url).content
soup = BeautifulSoup(url_content,'html.parser')

x = list(soup.find_all('script',type='text/javascript'))
xx = []
    
for i in x:
    xx.append(str(i))

for j in xx:
    if '51245' in j:
        thing = j
        break
    else:
        pass

thing_stripped = thing.strip()

ylist = thing_stripped.split('/')

url_initial = url.split('/')[2]

file_id = ylist[3]

unique_code = ylist[4].strip(" '\" ()+")
unique_code0 = eval(unique_code)

game_name = ylist[-2].strip('";\n}< ')

parsed_link = f'{url_initial}/d/{file_id}/{unique_code0}/{game_name}'
parsed_link2 = f'{url_initial}/d/{file_id}/{unique_code0}/script>'
# you can also use "script>" (without the quotes) instead of game name, it will download just as fine

print(ylist)

print()

print(url_initial)
print(file_id)
print(unique_code)
print(unique_code0)
print(game_name)

print()

print(parsed_link)
print(parsed_link2)