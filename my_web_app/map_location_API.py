import folium

from build_map import build
from get_location import get_loc
import requests


def get_json_from_API_IP(user_name):
    return requests.get(f"https://api.twitter.com/2/users/by/username/{user_name}", headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAI7vZAEAAAAAWxLmcJ3L6Qn49oId3kUP5CZijmk'
                         '%3DLDuIqIpBahgDanLhSxqwl7A2ueKRfXsFK4ll4zCgatORTveens'}).json()['data']['id']


def get_json_from_API_friends(ID):
    return requests.get(f"https://api.twitter.com/2/users/{ID}/following?user.fields=location",
                        headers={'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAI7vZAEAAAAAWxLmcJ3L6Qn49oId3kUP5CZijmk%3'
                                                  'DLDuIqIpBahgDanLhSxqwl7A2ueKRfXsFK4ll4zCgatORTveens'}).json()


def Main(users_name, count):
    API_json = get_json_from_API_friends(get_json_from_API_IP(users_name))
    print(API_json)
    data = API_json['data']
    kol = 0
    finding_location = []
    for user in data:
        if kol == count:
            break
        if "location" in user:
            finding_location.append((user["location"], user["username"]))
            kol += 1
    return build(get_loc(finding_location))


if __name__ == "__main__":
    Main('')
