import os
import re
import requests
from bs4 import BeautifulSoup

def clean_html(raw_html):
    '''Remove HTML tags'''
    clean_text = re.sub(re.compile('<.*?>') , '', raw_html)
    return clean_text

def main():
    '''Stage working directory for new Advent of Code day'''
    year = input('Enter year: ')
    if len(year) == 2:
        year = '20' + year
    day = input('Enter day: ')
    aoc_session = os.environ['AOC_COOKIE']
    url = 'https://adventofcode.com/' + year + '/day/' + day
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    challenge_text = clean_html(str(soup.article))
    challenge_input = requests.get(url + '/' + 'input', cookies={'session': aoc_session}, timeout=30)
    challenge_input.raise_for_status()
    if int(day) < 10:
        working_dir = '0' + day
        os.mkdir(working_dir)
    else:
        working_dir = day
        os.mkdir(working_dir)
    with open(working_dir + '/' + 'README.md', 'w', encoding='UTF8') as readme:
        readme.write(url + '\n\n' + challenge_text)
        readme.close()
    with open(working_dir + '/' + 'input.txt', 'w', encoding='UTF8') as input_file:
        input_file.write(challenge_input.text)
        input_file.close()

if __name__ == '__main__':
    main()
