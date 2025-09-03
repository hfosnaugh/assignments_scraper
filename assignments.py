from bs4 import BeautifulSoup
import pandas as pd

HTML = "assignmentScraper/assignments_scraper/Assignments_ MATH 214 FA 2025.htm"

#need to do custom parsing
def dt_parse(df):
    monthlist = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    #string parsing stuff
    for i in range(0, len(df), 1):
        date_str = df.iloc[i, 1]
        date_str = date_str.split()
        #print(date_str)
        df.iloc[i, 0] = df.iloc[i, 0] + " due " + date_str[2] + " " + date_str[3]
        for month in monthlist:
            if date_str[0] in month:
                date_str[0] = monthlist[month]
        #reassigns date format
        year = "2025"
        if int(date_str[0]) < 7:
            year = "2026"
        df.iloc[i, 1] = date_str[0]+"/"+date_str[1]+"/"+year
        #print(df.iloc[i, 0]+" | "+df.iloc[i, 1])
    
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
    print(assignments)
    assignments.to_csv('assignmentScraper/assignments.csv', index=False)
    

def parse():
    with open(HTML, 'r', encoding='utf-8') as file:
        html = file.read()
    get_content(html)

parse()
