from http.client import HTTPConnection as Ht
from requests import get
from json import loads


class IATAGetter(object):
    dummy_city = "Анадырь"
    link = "https://www.travelpayouts.com/widgets_suggest_params?q="
    link_ip = "http://www.travelpayouts.com/whereami?locale=ru&callback=useriata&ip="

    def __init__(self, city):
        self.city = city

    @staticmethod
    def _get_my_ip():
        conn = Ht("ifconfig.me")
        conn.request("GET", "/ip")
        s = conn.getresponse().read().split(b".")
        return [int(i) for i in s]

    @property
    def get_iata_by_name(self):
        l = f"{self.link}Из {self.city} в {self.dummy_city}"
        response = get(l)
        print(response.text)
        ret = loads(response.text)
        return ret["origin"]["iata"]

    @property
    def get_iata_by_ip(self):
        ip = self._get_my_ip()
        ip_str = ".".join([str(i) for i in ip])
        l = f"{self.link_ip}{ip_str}"
        response = get(l)
        return response.text


def main():
    g = IATAGetter("Иркутск")
    print(g.get_iata_by_name)
    print(g.get_iata_by_ip)


if __name__ == '__main__':
    main()
