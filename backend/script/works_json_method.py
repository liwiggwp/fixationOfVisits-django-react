import json

#РАСПИСАНИЕ

def parse_team(data, event):
  realizations = data["_embedded"]["lesson-realization-teams"]
  for realization in realizations:
    try:
      if (event["_links"]["lesson-realization-team"]["href"] == realization["_links"]["self"]["href"]):
        return realization["name"]
    except:
      pass
  return ""

def parse_subject(data, event):
  realizations = data["_embedded"]["course-unit-realizations"]
  for realization in realizations:
    try:
      if (event["_links"]["course-unit-realization"]["href"] == realization["_links"]["self"]["href"]):
        return realization["name"]
    except:
      pass
  return ""
def str_to_time(time_json):
    time_json.replace('T', ' ')
    second = time_json[11:16]
    return second

def parse_classes(data):
  id=0
  if (len(data) > 0):
    result = []
    events = data["_embedded"]["events"]
    if (len(events) > 0):
      for event in events:
        theme = event['name']
        starts_at = str_to_time(event['startsAtLocal'])
        ends_at = str_to_time(event['endsAtLocal'])
        subject = parse_subject(data, event)
        team = parse_team(data, event)
        eventId = event["id"]        
        result.append({
          'id':id,
          'modul': theme,
          'time': starts_at + " - " + ends_at,
          'subject': subject,
          'team': team,
          'eventId': eventId
        })
        id+=1
      return result

# with open('week_schedule.json', 'r', encoding='utf-8') as f:
#     json_week_schedule = json.load(f)
    
# list_week_schedule=parse_classes(json_week_schedule)




# СПИСКИ СТУДЕНТОВ И ПРЕПОДОВ

# вытащить списки из json
def list_student_teacher(token, eventId, id):
    
    with open("backend\\script\\file\\dis.json", 'r', encoding='utf-8') as f: #открыли файл с данными
        data_para = json.load(f) 
    realizations = data_para["_embedded"]["event-attendees"]
    per = data_para["_embedded"]["persons"]
    teach=[]
    stud=[]
    for i in range(len(realizations)):
        if realizations[i]['_links']['event-attendee-role']['href'] == '/TEACH':
            teach.append(realizations[i])
        else:
            stud.append(realizations[i])
    #Получить список ФИО преподавателей и студентов
    teacher_fullName=[]
    for t in teach:
        for p in per:
            if t['_links']['person']['href'] == ('/'+ p['id']):
                teacher_fullName.append(p['fullName'])
    student_fullName=[]
    for s in stud:
        for p in per:
            if s['_links']['person']['href'] == ('/'+ p['id']):
                student_fullName.append(p['fullName'])
    return teacher_fullName, student_fullName

# получить id пар (для получения списка команды и преподавателя)
def get_list_eventId(id,list_week):
    EventId=[]
    for i in range(len(list_week)):
        EventId.append(list_week[i]['eventId'])
    return EventId[id]
# получить id пар (для получения списка команды и преподавателя)
def get_list_eventId(id,list_week):
    EventId=[]
    for i in range(len(list_week)):
        EventId.append(list_week[i]['eventId'])
    return EventId[id]

# получить словари преподавателей и студентов
def get_list_teacher_student(temps):
    help_list_week_tea={}
    help_list_week_st={}
    tea = sorted(temps[0])
    for i in range(len(tea)):
        help_list_week_tea[str(i+1)] = tea[i]
    st= sorted(temps[1])
    for i in range(len(st)):
        help_list_week_st[str(i+1)] = st[i]
    return help_list_week_tea, help_list_week_st

#добавление в словарь для соединения списков с информацией пары
def add_week_dist_tea_st(token, list_week, id):
    temp = list_student_teacher(token, get_list_eventId(id, list_week),id)

    help_list_week=get_list_teacher_student(temp)
    list_week[id]['teacher'] = help_list_week[0]
    list_week[id]['student'] = help_list_week[1]
    return list_week

# ids=6
# json_student_teacher(token, get_list_eventId(ids, list_week_schedule),ids)

# end = add_week_dist_tea_st(token, list_week_schedule, ids)
# end[ids]

# with open("list_for_card.json", "w", encoding="UTF-8") as page:
#   json.dump(end, page, ensure_ascii=False)