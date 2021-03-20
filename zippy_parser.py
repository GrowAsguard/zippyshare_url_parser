import sys
import requests
from bs4 import BeautifulSoup

import tkinter
from tkinter import filedialog
root=tkinter.Tk()
root.withdraw()

def zippy_parser(url):

    url_content = requests.get(url).content
    soup = BeautifulSoup(url_content,'html.parser')

    x = list(soup.find_all('script',type='text/javascript'))
    xx= []

    for i in x:
        xx.append(str(i))
    
    for j in xx:
        if '51245' in j:
            reqd_tag = j
            break
        else:
            pass

    all_tag = reqd_tag.strip()
    ylist = all_tag.split('/')

    file_id = ylist[3]

    un_uncode = eval(ylist[4].strip(" '\" ()+"))

    game_name = ylist[-2].strip('";\n}< ')

    url_initial = url.split('/')[2]

    final_url = f'{url_initial}/d/{file_id}/{un_uncode}/{game_name}'

    print(final_url)
    return final_url

print('Press any key to select the txt file with the zippyshare links')
input()

file_path_open = filedialog.askopenfilename(
    initialdir='./',
    title='Please select the txt file with the ZippyShare links',
    filetypes=(('Text file','*.txt'),)
)

opened_file = open(file_path_open,'r')

file_path_closed = filedialog.asksaveasfilename(
    initialdir='./',
    title='Save file',
    filetypes=(('Text file','*.txt'),)
)

closed_file = open(file_path_closed+'.txt','a')

for line in opened_file:
    url = line.strip()
    res = zippy_parser(url)
    closed_file.write(res+'\n')

opened_file.close()
closed_file.close()

print('Press any key to exit')
input()
sys.exit()