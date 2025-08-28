from bs4 import BeautifulSoup
import pandas as pd

HTML = "assignmentScraper/assignments_scraper/Assignments_ MATH 214 FA 2025.htm"

#need to do custom parsing
def dt_parse(df):
    #string parsing stuff
    for i in range(0, len(df), 1):
        date_str = df.iloc[i, 1]
        date_str = date_str.split()
        print(date_str)
        #df.iloc[i, 0] = df.iloc[i, 0] + " " + date_str[2] + " " + date_str[3]
        #print(type(df.iloc[i, 0]))
    #Nov 9 at 12am
    
    #df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')
    #print(df)

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    assignments = pd.DataFrame(columns=['title', 'due_date'])
    elements = soup.find_all(class_="ig-info")
    for row in elements:
        title = row.find(class_='ig-title').get_text(strip=True)
        due_date = row.find('span',class_='screenreader-only').get_text(strip=True)
        assignments.loc[len(assignments)] = [title, due_date]
    dt_parse(assignments)
    #print(assignments)
    #assignments.to_csv('assignments.csv', index=False)
    

def parse():
    with open(HTML, 'r', encoding='utf-8') as file:
        html = file.read()
    get_content(html)

parse()
