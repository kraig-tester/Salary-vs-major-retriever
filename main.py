"""Program receives current data from payscale.com on major and their corresponding salaries.
For proper use, user should insert number of pages on the website into variable num_of_pages 
"""
import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.payscale.com/college-salar-report/majors-that-pay-you-back/bachelors"
URL_PAGE = "/page/"
FILE_NAME = "updated_salaries_list.csv"

num_of_pages = 34
contents = "Rank,Major,Degree Type,Early Career Pay,Mid-Career Pay,High Meaning\n"


def cls():
    '''Clears screen to properly display current progress
    '''
    os.system('cls' if os.name=='nt' else 'clear')


def clear_string(str):
    '''Extracts extra symbols from a string like, which are unnecessary
    for our purposes
    '''
    new_str = str.strip()
    new_str = str.replace('$', '')
    new_str = new_str.replace('%', '')
    new_str = new_str.replace(',','')
    return new_str


for page in range(1,num_of_pages+1):
    cls()
    print(f"Current page: {str(page)}")
    if page != 1:
        response = requests.get(URL + URL_PAGE + str(page))
    else:
        response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all(name="tr", class_="data-table__row")

    for row in range(len(rows)):
        values = rows[row].find_all(class_ = "data-table__value")
        new_row = ""
        for count in range(len(values)):
            new_row += f"{clear_string(values[count].getText())}"
            if count != len(values)-1:
                new_row+=','
        new_row+='\n'
        contents+=new_row

cls()
print(f'Creating file with results: "{FILE_NAME}"')

with open(FILE_NAME, mode="w", encoding="utf8") as file:
    file.write(contents)