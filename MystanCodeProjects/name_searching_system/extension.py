"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():

    # web crawling
    for year in ['2010s', '2000s', '1990s']:
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find_all('tbody')

        # initial number
        males = 0
        females = 0

        for item in items:
            data = item.text
            data = data.split()

            # remove names(str)
            for ele in data:
                if ele.isalpha():
                    data.remove(ele)

            # remove ranks
            for rank in data:
                if rank.isdigit():
                    data.remove(rank)

            for i in range(len(data)):
                # when to stop
                if data[i] == 'Source:':
                    break

                # even => males' names' nums
                if i % 2 == 0:
                    males += int(data[i].replace(',', ''))

                # odd => females' names' nums
                else:
                    females += int(data[i].replace(',', ''))
        print('---------------------------')
        print(year)
        print('Male Number:', males)
        print('Female Number:', females)


if __name__ == '__main__':
    main()
