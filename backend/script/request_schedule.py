from lib2to3.pgen2 import token
import requests
import json
from time import sleep

tfile = "backend\\script\\file\\token.txt"

def json_schedule(token):
    cookies = {
    '_ym_uid': '164503288520620731',
    '_ym_d': '1645032885',
    '_ym_isad': '1',
    'tc01': '29bf94755cc7e30bf6e8e70954e6cc2d',
    }

    headers = {
        'authority': 'utmn.modeus.org',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer '+ token,
        'origin': 'https://utmn.modeus.org',
        'referer': 'https://utmn.modeus.org/schedule-calendar/my?timeZone=%22Asia%2FTyumen%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222022-04-11%22%7D&grid=%22Grid.05%22',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-app-page-url': 'https://utmn.modeus.org/schedule-calendar/my?timeZone=%22Asia%2FTyumen%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222022-04-04%22%7D&grid=%22Grid.05%22',
    }

    json_data = {
        'size': 500,
        'timeMin': '2022-04-06T00:00:00Z',
        'timeMax': '2022-04-07T00:00:00Z',
        'attendeePersonId': [
            'ac82739d-696b-4ab6-bb3f-0a6c061508a1',
        ],
    }

    response = requests.post('https://utmn.modeus.org/schedule-calendar-v2/api/calendar/events/search?tz=Asia/Tyumen&authAction=', cookies=cookies, headers=headers, json=json_data)

    j = response.json()
    with open("backend\\script\\file\\week_schedule.json", "w", encoding="UTF-8") as page:
        print(json.dump(j, page, ensure_ascii=False))
    sleep(30)

# def run():    
#     tokens = open(tfile, "r").read()
#     json_schedule(tokens)
tokens = open(tfile, "r").read()
json_schedule(tokens)