import requests

def gettoken(ClientID, ClientSecret, Code, URL):

#ClientID="1B2349B9FA66DC4F2B0561673667D40E5E03267E0F015E40CF4B15C33F871BB6"
#ClientSecret="6E218B9A3E676A3B8EEBF0D20439225E9164D39B5D505CE15AE3A5E5F9D2B8C1"
#Code="eyJ4LXJlZyI6IkVVIiwieC1lbnYiOiJQUkQiLCJ0b2tlbiI6ImRhNjRlZTk2LWE1OTAtNDY5MC1hNDk2LTQxNmY2MGY1ZjRlOSIsImNsdHkiOiJwcml2YXRlIn0="
#URL="https://test.se"


    params={"grant_type":"authorization_code","client_id":ClientID,"client_secret":ClientSecret,"code":Code,"redirect_uri":URL}
    headers = { 'Content-Type': 'application/x-www-form-urlencoded', 'host':'asdf.com'}
    r=requests.post("https://api.home-connect.com/security/oauth/token", data=params, headers=headers)
#    Domoticz.Log(str(r.content)
    return r.content
