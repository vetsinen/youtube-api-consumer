from pyyoutube import Api
api = Api(client_id="client key", client_secret="client secret")
# Get authorization url
print (api.get_authorization_url())
#('https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=id&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=scope&state=PyYouTube&access_type=offline&prompt=select_account', 'PyYouTube')
# user to do
# copy the response url
#>>> api.generate_access_token(authorization_response="link for response")
# AccessToken(access_token='token', expires_in=3599, token_type='Bearer')