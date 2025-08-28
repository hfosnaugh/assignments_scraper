from bs4 import BeautifulSoup
import pandas as pd

HTML = "assignmentScraper/assignments_scraper/Assignments_ MATH 214 FA 2025.htm"

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    assignments = pd.DataFrame(columns=['title', 'due_date'])
    elements = soup.find_all(class_="ig-info")
    for row in elements:
        title = row.find(class_='ig-title').get_text(strip=True)
        due_date = row.find('span',class_='screenreader-only').get_text(strip=True)
        assignments.loc[len(assignments)] = [title, due_date]
    print(assignments)
    

def parse():
    with open(HTML, 'r', encoding='utf-8') as file:
        html = file.read()
    get_content(html)

parse()