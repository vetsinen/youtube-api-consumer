from pyyoutube import Api

def get_token_from_google():
    api = Api(client_id="1029429236539-4del4jm1mes0csfpf92lvb5pb8fo2kit.apps.googleusercontent.com",
              client_secret="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")
    print (api.get_authorization_url()[0])
    #('https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=id&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=scope&state=PyYouTube&access_type=offline&prompt=select_account', 'PyYouTube')
    # user to do
    # copy the response url
    str = input('enter url')
    return (api.generate_access_token(authorization_response=str).access_token)
    # AccessToken(access_token='token', expires_in=3599, token_type='Bearer')

if __name__ == '__main__':
    actoc = (get_token_from_google())
    with open('actoc.txt', 'w') as file:
        file.write(actoc)


# a = AccessToken(access_token='ya29.a0AVvZVsrib0nIJeUU6M4gTW60oPaHZ02zwrzoauuar4DjPVCmL8wN58BIgjLyt1SczYdu8IaBc3fAYp7Ozf0C5rhn60m5oM2Xs9boR3nPKPApy43JNC-Y1CHyoc2s_qGagr4KPUcG5jHGxu6jQTwD5GZ5RM-6aCgYKATcSARASFQGbdwaIR0K5BPbDyoKq5cpYk6iwwg0163', expires_in=3599, token_type='Bearer')
