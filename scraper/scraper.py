from bs4 import BeautifulSoup
import requests

TEST_CITY = {
    "city" : "Oakland",
    "state" : "IL",
    "country" : "United States"
}

NUMBEO_URL = "https://www.numbeo.com/cost-of-living/in/"


def formatLocationURL(city, country='', state=''):
    return ('-').join(filter(None, city.split(' ') + state.split(' ') + country.split(' ')))

def loadPage(city_dict):
    
    numbeo_req = requests.get(NUMBEO_URL + formatLocationURL(city_dict["city"]))

    # TODO: add error handling for bad request

    bs_obj = BeautifulSoup(numbeo_req.content, 'html.parser')

    if ("Cannot find city id" in bs_obj):
        numbeo_req = requests.get(NUMBEO_URL + formatLocationURL(city_dict["city"], city_dict["country"], city_dict["state"]))
        bs_obj = BeautifulSoup(numbeo_req.content, 'html.parser')

        if ("Cannot find city id" in bs_obj):
            # TODO: error handling for nonexistent city
            pass

    return bs_obj


numbeo_bs = loadPage(TEST_CITY)

print(numbeo_bs.title.get_text())

