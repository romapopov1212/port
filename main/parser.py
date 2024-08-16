import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def all_ctf():
    url = 'https://ctftime.org/event/list/'
    base_url = 'https://ctftime.org'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    current_year = datetime.now().year
    current_datetime = datetime.now()
    
    events = []
    for row in soup.select('tr'):
        columns = row.find_all('td')
        if columns:
            name_tag = columns[0].find('a')
            date_range = columns[1].text.strip().split(' — ')
            
            # Регулярное выражение для поиска даты и времени
            date_pattern = re.compile(r'(\d{2} \w{3})(?:, (\d{4}))?\.?, (\d{2}:\d{2} UTC)')
            
            start_date_match = date_pattern.match(date_range[0].strip())
            
            
            # Обработка дат
            if start_date_match:
                start_date_str = start_date_match.group(1)
                start_time_str = start_date_match.group(3)
                start_year_str = start_date_match.group(2) if start_date_match.group(2) else str(current_year)
                start_date = datetime.strptime(f'{start_date_str}, {start_year_str} {start_time_str}', '%d %b, %Y %H:%M UTC')
            else:
                start_date = None
            
           
            if start_date and start_date > current_datetime:  # Добавляем только мероприятия после текущей даты
                events.append({
                    'name': name_tag.text.strip(),
                    'link': base_url + name_tag.get('href'),
                    'start_date': start_date,
                    
                })
    
    # Сортируем мероприятия по дате начала и берем первые 5
    events = sorted(events, key=lambda x: x['start_date'])[:3]
    
    # Преобразуем дату в строку для удобного отображения
    for event in events:
        event['start_date'] = event['start_date'].strftime('%d %b, %Y %H:%M UTC')
    
    return events