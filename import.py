import json
from pyyoutube import Api

def main():
    api = Api(access_token='ya29.a0AVvZVsrib0nIJeUU6M4gTW60oPaHZ02zwrzoauuar4DjPVCmL8wN58BIgjLyt1SczYdu8IaBc3fAYp7Ozf0C5rhn60m5oM2Xs9boR3nPKPApy43JNC-Y1CHyoc2s_qGagr4KPUcG5jHGxu6jQTwD5GZ5RM-6aCgYKATcSARASFQGbdwaIR0K5BPbDyoKq5cpYk6iwwg0163')
    channel_by_mine = api.get_channel_info(mine=True)

    print(channel_by_mine.items[0])
    # with open('vitaliy.gusak24@gmail.com.json', 'r') as f:
    #     data = json.load(f)
    #
    # # Output: {'name': 'Bob', 'languages': ['English', 'French']}
    # print(data)


if __name__ == '__main__':
    main()