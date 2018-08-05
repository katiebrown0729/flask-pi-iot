'''Code to get config info from a yaml file at a given url. Made by Katie & David, still married... unbelievably'''

import yaml
import requests

class YAMLConfig():
    def get_config_from_url(self,url):
        response = requests.get(url)
        if (response.status_code ==200):
            d = yaml.load(response.text)
        print(d)
        return d

if __name__ == '__main__':
    YConfig = YAMLConfig()  # type: YAMLConfig
    YConfig.get_config_from_url("https://github.com/katiebrown0729/flask-pi-iot/blob/master/pi_client/config/config.yml")
