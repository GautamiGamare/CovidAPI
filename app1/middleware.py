import requests
import json
from proj1.settings import covid19_path
class Covid19Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Im Constructor")
        data_loading()

    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        print("Im Call")
        return response

def data_loading():
    res = requests.get("https://api.covid19india.org/state_district_wise.json")
    # print(res.status_codes)
    dict_data = json.loads(res.text)
    json.dump(dict_data, open(covid19_path, "w"))
    print("data loaded")
