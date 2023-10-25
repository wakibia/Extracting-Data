
"""Downloading Files
This file involves downloading files from websites.

Here we demonstrate using image download for the country flags.

This is done using `requests` and `BeautifulSoup`

"""

from bs4 import BeautifulSoup
import requests
import os

# create a directory to store your files if it doesn't exists

if not os.path.exists('downloaded_files'):
    os.makedirs('downloaded_files')

# where to download the files from
url = 'https://www.worldometers.info/geography/flags-of-the-world/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# container for the flags
flags_div = soup.find_all('div', {'class': "col-md-4"})
countries = []

for flag in flags_div:
    try:
        img_src = flag.find('img').get('src')
        img_url = 'https://www.worldometers.info'+img_src
        response = requests.get(img_url)
        country_name = flag.find('div', {'style': "font-weight:bold; padding-top:10px"}).text.strip()
        countries.append(country_name)
        new_name = country_name+'.'+(img_url.split('/')[-1].split('.')[-1].replace('gif', 'jpg'))
        new_filename = os.path.join('downloaded_files', new_name)

        if new_filename not in os.listdir('downloaded_files'):
            # save the flags to the directory
            with open(new_filename, 'wb') as file:
                file.write(response.content)
        else:
            print(f"{new_filename} already added")
    except Exception as e:
        print(f"This exception was found: {e}")

## total number of flags
print(f"Total Country Flags Found in the {url}: ", len(countries))

## total flags downloaded in the directory
all_downloads = os.listdir('downloaded_files')
print("Total Flags Downloaded: ", len(all_downloads))
