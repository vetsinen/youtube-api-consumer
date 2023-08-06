import json
from pyyoutube import Api, Client, PyYouTubeException
import pyyoutube.models as mds
import pyyoutube.resources.playlists as pls
from authy import get_token_from_google

def get_valid_client():
    with open('actoc.txt', 'r') as file:
        actoc = file.read()

    client = (Client(access_token=actoc))
    try:
        resp = client.channels.list(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
    except(PyYouTubeException):
        actoc = get_token_from_google()
        client = (Client(access_token=actoc))
        resp = client.channels.list(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
        with open('actoc.txt', 'w') as file:
            file.write(actoc)

    return client

def inser_playlist():
    pass


def main():
    # api = Api(access_token='ya29.a0AVvZVsrib0nIJeUU6M4gTW60oPaHZ02zwrzoauuar4DjPVCmL8wN58BIgjLyt1SczYdu8IaBc3fAYp7Ozf0C5rhn60m5oM2Xs9boR3nPKPApy43JNC-Y1CHyoc2s_qGagr4KPUcG5jHGxu6jQTwD5GZ5RM-6aCgYKATcSARASFQGbdwaIR0K5BPbDyoKq5cpYk6iwwg0163')
    client = get_valid_client()
    insert = client.playlists.insert({"title":"playlist title","description":"pl descr"})
    # "defaultLanguage": "en-US"
    # resp = client.channels.list(channel_id="UCEFrhn7UqDRjYc4q_5sLW5A")

    # with open('vitaliy.gusak24@gmail.com.json', 'r') as f:
    #     data = json.load(f)
    #
    # # Output: {'name': 'Bob', 'languages': ['English', 'French']}
    # print(data)


if __name__ == '__main__':
    main()