import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path

insta_url='https://www.instagram.com'
inta_username= input('enter username of instagram : ')

response = requests.get(f"{insta_url}/{inta_username}/")

#if the response is ok, find profile photo link

if response.ok:
    html = response.text

    bs_html = bs(html, features="lxml")
    bs_html = bs_html.text
    index = bs_html.find('profile_pic_url_hd')+21

    remaining_text = bs_html[index:]
    remaining_text_index = remaining_text.find('request_by_viewer')-3
    string_url =remaining_text[:remaining_text_index]
    print(string_url, "\n \n downloading..........")

#Now, create a loop and download photo
while True:
    filename = 'pic' +str(random.randint(1, 100000))+ 'jpg'
    file_exist =os.path.isfile(filename)

    if not file_exist:
        with open(filename, 'wb+')as handle:
            response = request.get(string_url, stream = True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                    handle.write(block)
    else:
        continue
    break
print("\n                downloading completed ..............")




