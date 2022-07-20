import requests
import json
from time import sleep
import works_json_method as works


def json_student_teacher(token, eventId, id):
        cookies = {
                '_ym_uid': '164503288520620731',
                '_ym_d': '1645032885',
                'tc01': '07f636ded531c2a3b69d89a89d61420c',
                '_ym_isad': '1',
        }

        headers = {
                'authority': 'utmn.modeus.org',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer ' + token,
                'referer': 'https://utmn.modeus.org/schedule-calendar/my?timeZone=%22Asia%2FTyumen%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222022-04-04%22%7D&selectedEvent=%7B%22eventId%22:%22' + eventId + '%22%7D&grid=%22Grid.05%22',
                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                'x-app-page-url': 'https://utmn.modeus.org/schedule-calendar/my?timeZone=%22Asia%2FTyumen%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222022-04-04%22%7D&selectedEvent=%7B%22eventId%22:%22' + eventId + '%22%7D&grid=%22Grid.05%22',
        }

        params = {
                'authAction': '',
        }

        response = requests.get('https://utmn.modeus.org/schedule-calendar-v2/api/calendar/events/' + eventId + '/team', params=params, cookies=cookies, headers=headers)
        j = response.json()
        with open("backend\\script\\file\\dis.json", "w", encoding="UTF-8") as page:
                json.dump(j, page, ensure_ascii=False)
        sleep(30)

tfile = "backend\\script\\file\\token.txt"

tokens = open(tfile, "r").read()

with open('backend\\script\\file\\week_schedule.json', 'r', encoding='utf-8') as f:
    json_week_schedule = json.load(f)
    
list_week_schedule=works.parse_classes(json_week_schedule)


for ids in range(len(list_week_schedule)):
        json_student_teacher(tokens, works.get_list_eventId(ids,list_week_schedule),ids)

        end = works.add_week_dist_tea_st(tokens, list_week_schedule, ids)
        end[ids]

        with open(r"C:\Users\liwiggwp\Documents\6 semestr\fixationOfVisits-django-react\frontend\src\store\list_for_card.json", "w", encoding="UTF-8") as page:
                json.dump(end, page, ensure_ascii=False)