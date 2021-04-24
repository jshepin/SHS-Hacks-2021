import requests, json

class Car:

    def __init__(self, data: dict):
        self.make            = data['attributes']['make']
        self.model           = data['attributes']['model']
        self.year            = data['attributes']['year']
        self.trim            = data['attributes']['trim']
        self.style           = data['attributes']['style']
        self.type            = data['attributes']['type']
        self.fuel_type       = data['attributes']['fuel_type']

        self.horsepower      = data['attributes']['make'] #NOT AVALIBLE
        self.torque          = data['attributes']['make'] #NOT AVALIBLE
        self.acceleration    = data['attributes']['make'] #NOT AVALIBLE

        fuel_capacity_raw    = data['attributes']['fuel_capacity']
        self.fuel_capacity   = {
            'capacity' : float(fuel_capacity_raw[0]),
            'units'    : str(fuel_capacity_raw[1])
        }
        city_mileage_raw     = data['attributes']['city_mileage'].split(' ', 1)
        self.city_mileage    = {
            'mileage' : float(city_mileage_raw[0]),
            'units'   : str(city_mileage_raw[1])
        }
        highway_mileage_raw  = data['attributes']['highway_mileage'].split(' ', 1)
        self.highway_mileage = {
            'mileage' : float(highway_mileage_raw[0]),
            'units'   : str(highway_mileage_raw[1])
        }
        self.mpg           = {
            'mpg' : data['attributes']['make'],
            'electric' : False
        }

    def __str__(self):
         return F'''
Make: {self.make}
Model: {self.model}
Year: {self.year}
Trim: {self.trim}
Style: {self.style}
Type: {self.type}
Fuel Capacity: {self.fuel_capacity['capacity']}
City Mileage: {self.city_mileage['mileage']}
Highway Mileage: {self.highway_mileage['mileage']}
'''


def fetch_carxse(vin: str):
    url = 'https://storage.googleapis.com/car-switch/respoonse.json'
    #url =  F'https://api.carsxe.com/specs?key=rnldxnjyx_s9pe9t3ov_kyb2nnr21&vin={vin}
    r = requests.get(url)#, headers=headers)
    return json.loads(r.text)

def fetch_carqueryapi(make: str, model: str, year: str):
<<<<<<< HEAD
    url = F'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make={make}&model={model}&year={year}'
    #url = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make=Lexus&year=2006'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return json.loads(r.text[2:-2])

if __name__ == '__main__':
    json_str = fetch_carxse('JTJZK1BA1D2009651')
    car = Car(json_str)
    print(car)
    a = fetch_carqueryapi(car.make, car.model + car.trim, car.year)
    print(a)
=======
    #url = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make=' + make + '&model=' + model + '&year=' + year
    url = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make=' + make + '&year=' + year
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    for entry in json.loads(r.text[2:-2])['Trims']:
        if entry['model_name'] + ' ' + entry['model_trim'] == model:
            return entry
    return null


def getImageURL(make: str, model:str):
    url = "https://storage.googleapis.com/car-switch/image_response.json"
    # url = "http://api.carsxe.com/images?key=rnldxnjyx_s9pe9t3ov_kyb2nnr21&make=%s&model=%s" % (make,model)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data["images"][0]["link"]

# getImageURL("chevy","bolt")


if __name__ == '__main__':
    fetch_carqueryapi('Lexus','ES330','2005')
>>>>>>> 046d49a425b8871b2e40ee50c301d0b8840f1c32
    """
    json_str = fetch_carxse('JTJZK1BA1D2009651')
    car = Car(json_str)
    print(car)
    """
