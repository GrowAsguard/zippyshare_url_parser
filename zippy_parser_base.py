import requests
from bs4 import BeautifulSoup

url = "https://www9.zippyshare.com/v/m90twnE2/file.html"
#the url is the zippyshare url

url_content = requests.get(url).content
soup = BeautifulSoup(url_content,'html.parser')

x = list(soup.find_all('script',type='text/javascript'))
xx = []
    
for i in x:
    xx.append(str(i))

for j in xx:
    if 'var a' and 'var b' in j:
        thing = j
        break
    else:
        pass

line_list = []

for l in j.splitlines():
    line_list.append(l)

a = eval(line_list[1].strip('varb= ;'))
b = eval(line_list[2].strip('varb= ;'))

url_initial = url.split('/')[2]

file_code = url.split('/')[4]

unique_code = (a//3) + (a%b)

file_name0 = line_list[-3]
file_name1 = file_name0.split('/')[-1]
file_name2 = file_name1.strip('";')

final_url = f'https://{url_initial}/d/{file_code}/{unique_code}/{file_name2}'

print(final_url)