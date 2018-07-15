import requests
from bs4 import BeautifulSoup
from person.person import Harvard_Person
from random import random

class Directory_API:
    def get_student(email=None, first_name=None, last_name=None, phone=None):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.directory.harvard.edu',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache',
            'Postman-Token': '3dfh5a1f-7q5e-e66r-f9d7-a5ay66189e93'
        }

        payload = ''
        if email != None:
            payload += 'email='+email+'&'
        if first_name != None:
            payload += 'firstName='+first_name+'&'
        if last_name != None:
            payload += 'lastName='+last_name+'&'
        if phone != None:
            payload += 'officePhone='+phone+'&'
        if payload == '':
            return None
        payload = 'org.apache.struts.taglib.html.TOKEN=6e2a03f2877b4ad9a25dc7393a780d36&' + payload + 'command_btn=Search'

        r = requests.post('https://www.directory.harvard.edu/submitSearch.do', headers=headers, data=payload)

        return Directory_API.parse_directory_response(r)

    def parse_directory_response(r):
        if r.status_code != 200:
            return None

        soup = BeautifulSoup(r.content, 'html.parser')

        try:
            trs = soup.find('table').find('form').find_all('tr')

            name = trs[0].find_all('td')[1].text
            department = trs[1].find_all('td')[1].text
            email = trs[2].find_all('td')[1].text
            phone = trs[3].find_all('td')[1].text
            residence = trs[4].find_all('td')[1].text
            unit = trs[5].find_all('td')[1].text
            mail = trs[6].find_all('td')[1].text
            name = name.split(' ')

            return Harvard_Person(name[2], name[-1], department, phone, residence, unit, mail)
        except:
            pass

        try:
            trs = soup.find('table').find('table').find('table').find('tbody').find_all('tr')
            persons = []

            for tr in trs:
                a = tr.find('a')
                print('no')
                if a == None:
                    break

                href = a.attrs['href']
                r = requests.get('https://www.directory.harvard.edu' + href)
                persons.append(Directory_API.parse_directory_response(r))

            return persons

        except:
            return None
