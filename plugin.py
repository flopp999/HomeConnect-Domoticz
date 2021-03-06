# Home Connect Python Plugin
#
# Author: flopp999
#
"""
<plugin key="HomeConnect" name="Home Connect 0.14" author="flopp999" version="0.14" wikilink="https://github.com/flopp999/HomeConnect-Domoticz" externallink="https://github.com/flopp999/HomeConnect-Domoticz">
    <description>
        <h2>HomeConnect is reading data from https://api.home-connect.com</h2><br/>
        <h2>Support me with a coffee &<a href="https://www.buymeacoffee.com/flopp999">https://www.buymeacoffee.com/flopp999</a></h2><br/>
        <h2>or use my Tibber link &<a href="https://tibber.com/se/invite/8af85f51">https://tibber.com/se/invite/8af85f51</a></h2><br/>
        <h3>Features</h3>
        <ul style="list-style-type:square">
            <li>..</li>
        </ul>
        <h3>Devices</h3>
        <ul style="list-style-type:square">
            <li>xxxxxxxxxxxxxxxxx</li>
        </ul>
        <h3>How to get your Cliend ID, Client Secret and Redirect URI?</h3>
        <h4>&<a href="https://github.com/flopp999/HomeConnect-Domoticz#identifier-secret-and-callback-url">https://github.com/flopp999/HomeConnect-Domoticz#identifier-secret-and-callback-url</a></h4>
        <h3>How to get your Authorization Code?</h3>
        <h4>&<a href="https://github.com/flopp999/HomeConnect-Domoticz#access-code">https://github.com/flopp999/HomeConnect-Domoticz#access-code</a></h4>
        <h3>Configuration</h3>
    </description>
    <params>
        <param field="Mode5" label="Client ID" width="500px" required="true" default="Client ID"/>
        <param field="Mode2" label="Client Secret" width="500px" required="true" default="Client Secret"/>
        <param field="Address" label="Redirect URI" width="650px" required="true" default="Redirect URI"/>
        <param field="Mode1" label="Authorization Code" width="350px" required="true" default="Authorization Code"/>
        <param field="Mode6" label="Debug to file (HomeConnect.log)" width="70px">
            <options>
                <option label="Yes" value="Yes" />
                <option label="No" value="No" default="true" />
            </options>
        </param>
    </params>
</plugin>
"""

import Domoticz

Package = True

try:
    import requests, json, os, logging
except ImportError as e:
    Package = False

try:
    from logging.handlers import RotatingFileHandler
except ImportError as e:
    Package = False

try:
    from datetime import datetime
except ImportError as e:
    Package = False

dir = os.path.dirname(os.path.realpath(__file__))
logger = logging.getLogger("HomeConnect")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(dir+'/HomeConnect.log', maxBytes=50000, backupCount=5)
logger.addHandler(handler)

class BasePlugin:
    enabled = False

    def __init__(self):

        return

    def onStart(self):
#        Domoticz.Debugging(128)
        self.GetAccessToken = Domoticz.Connection(Name="Get AccessToken", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")
        self.RefreshAccessToken = Domoticz.Connection(Name="Refresh AccessToken", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")
        self.GetOperationState = Domoticz.Connection(Name="Get OperationState", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")
        self.KeepAlive = Domoticz.Connection(Name="KeepAlive", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")
#        self.KeepAliveListen = Domoticz.Connection(Name="KeepAlive", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")
#        self.KeepAliveListen.Listen()
        WriteDebug("onStart")
        self.loop = 0
        self.Count = 5
        self.ClientID = Parameters["Mode5"]
        self.ClientSecret = Parameters["Mode2"]
        self.RedirectURI = Parameters["Address"]
        self.AuthorizationCode = Parameters["Mode1"]
        self.RefreshToken = ""
        self.AccessToken = ""
        self.Status = ""
        self.GetData = True
        self.DeviceName = ""
        self.DevicehaId = ""
        if len(self.ClientID) < 64:
            Domoticz.Log("Client ID too short")
            WriteDebug("Client ID too short")

        if len(self.ClientSecret) < 64:
            Domoticz.Log("Client Secret too short")
            WriteDebug("Client Secret too short")

        if len(self.RedirectURI) < 8:
            Domoticz.Log("Redirect URI too short")
            WriteDebug("Redirect URI too short")

        if len(self.AuthorizationCode) < 124:
            Domoticz.Log("Authorization Code too short")
            WriteDebug("Authorization Code too short")

        self.RefreshToken = CheckFile("RefreshToken")


#        Domoticz.Log(self.RefreshToken)

#        if self.RefreshToken == False:
#            Domoticz.Log("RefreshToken too short")
#            WriteDebug("RefreshToken too short")
#            self.GetAccessToken.Connect()
#        else:
#            self.RefreshAccessToken.Connect()

        if os.path.isfile(dir+'/HomeConnect.zip'):
            if 'HomeConnect' not in Images:
                Domoticz.Image('HomeConnect.zip').Create()
            self.ImageID = Images["HomeConnect"].ID




#        self.KeepAlive.Connect()

#        self.RefreshAccessToken.Connect()

#        GetAppliances(_plugin.AccessToken)
#        self.GetToken = Domoticz.Connection(Name="Get Token", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")
#        self.GetToken.Connect()
#        self.GetData = Domoticz.Connection(Name="Get Data", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")

#        Domoticz.Log(str(Data))
#        Status = int(Data["Status"])
#        Data = Data['Data'].decode('UTF-8')
#        WriteDebug("Status = "+str(Status))
#        Data = json.loads(Data)


#        Tokens = GetTokens(self.ClientID,self.ClientSecret,self.AuthorizationCode,self.RedirectURI)
#        self.Status = Tokens.status_code
#        Data = Token.json()
#        Data = json.loads(Tokens.content)
#        Domoticz.Log(str(Data["error"]))



#        if (self.Status == 200):

#            self.AccessToken = Data["access_token"]
#            Domoticz.Log("first token"+str(self.token))
#            Domoticz.Log("innan refresh"+str(self.refreshtoken))
#            self.RefreshToken = Data["refresh_token"]
#            Domoticz.Log("first refresh"+str(self.refreshtoken))

#                with open(dir+'/HomeConnect.ini') as jsonfile:
#                    data = json.load(jsonfile)
#                data["Config"][0]["Access"] = Data["access_token"]
#                with open(dir+'/HomeConnect.ini', 'w') as outfile:
#                    json.dump(data, outfile, indent=4)
#                self.GetToken.Disconnect()
#                self.GetData.Connect()


#        else:
#            Domoticz.Error(str("Status "+str(self.Status)))
#            Domoticz.Error(str(Data))
#            if _plugin.GetToken.Connected():
#                _plugin.GetToken.Disconnect()
    def onConnect(self, Connection, Status, Description):

        if Connection.Name == ("Get AccessToken"):
            Domoticz.Log("Get AccessToken")
            data = "grant_type=authorization_code"
            data += "&client_id="+self.ClientID
            data += "&client_secret="+self.ClientSecret
            data += "&redirect_uri="+self.RedirectURI
            data += "&code="+self.AuthorizationCode
#            Domoticz.Log(str(data))
            headers = { 'Host': 'api.home-connect.com', 'Content-Type': 'application/x-www-form-urlencoded' }
            Connection.Send({'Verb':'POST', 'URL': '/security/oauth/token', 'Headers': headers, 'Data': data})

        if Connection.Name == ("Refresh AccessToken"):
            Domoticz.Log(str(self.RefreshToken))
            Domoticz.Log("refresh start")
            data = "grant_type=refresh_token"
            data += "&refresh_token="+self.RefreshToken
            data += "&client_secret="+self.ClientSecret
#            Domoticz.Log(str(data))
            headers = { 'Host': 'api.home-connect.com', 'Content-Type': 'application/x-www-form-urlencoded' }
            Connection.Send({'Verb':'POST', 'URL': '/security/oauth/token', 'Headers': headers, 'Data': data})

        if Connection.Name == ("Get OperationState"):
            headers = { 'Host': 'api.home-connect.com', 'Authorization': 'Bearer '+self.AccessToken }
            Connection.Send({'Verb':'GET', 'URL': 'api/homeappliances/'+self.DevicehaId+'/status/BSH.Common.Status.OperationState', 'Headers': headers})
            Domoticz.Log("Get OperationState Done")

        if Connection.Name == ("KeepAlive"):
            Domoticz.Log("KeepAlive")
            headers = { 'Host': 'api.home-connect.com', 'Accept': 'text/event-stream', 'Authorization': 'Bearer '+self.AccessToken }
#            Domoticz.Log(str(headers))

            Connection.Send({'Verb':'GET', 'URL': '/api/homeappliances/56/events', 'Headers': headers})
            Domoticz.Log("KeepAlive Done")

    def onMessage(self, Connection, Data):
        Domoticz.Log(str(Data))
        Status = int(Data["Status"])
#        Data = Data['Data'].decode('UTF-8')
        Data = json.loads(Data["Data"])
        WriteDebug("Status = "+str(Status))

        if Status == 200:
            if Connection.Name == ("Get AccessToken"):
                Domoticz.Log("Get AccessToken Onmess")
                Domoticz.Log("AccessToken old")

                Domoticz.Log(str(self.AccessToken))

                self.AccessToken = Data["access_token"]
                Domoticz.Log("AccessToken new")
                Domoticz.Log(str(self.AccessToken))

                self.RefreshToken = Data["refresh_token"]
                Domoticz.Log(str(self.RefreshToken))

                WriteFile("RefreshToken",self.RefreshToken)
                self.GetAccessToken.Disconnect()
                Domoticz.Log("Get Refresh Done")

            elif Connection.Name == ("Refresh AccessToken"):

                self.AccessToken = Data["access_token"]
                Domoticz.Log(str(self.AccessToken))

                self.RefreshToken = Data["refresh_token"]
                Domoticz.Log(str(self.RefreshToken))

                WriteFile("RefreshToken",self.RefreshToken)
                self.RefreshAccessToken.Disconnect()

#                self.KeepAlive.Connect()


            elif Connection.Name == ("Get OperationState"):
                self.AccessToken = Data["access_token"]
                self.RefreshToken = Data["refresh_token"]
#                WriteFile("RefreshToken",self.RefreshToken)

            elif Connection.Name == ("KeepAlive"):
                Domoticz.Log(str(Data))

#        elif Status == 400 and Data["error_description"] == "invalid authorization_code":
#            self.RefreshToken = CheckFile("RefreshToken")
#            self.GetAccessToken.Disconnect()
#            self.RefreshAccessToken.Connect()

        else:
            if self.GetAccessToken.Connected():
                self.GetAccessToken.Disconnect()
            if self.RefreshAccessToken.Connected():
                self.RefreshAccessToken.Disconnect()

            Domoticz.Error(str("Status "+str(Status)))
            Domoticz.Error(str(Data))
            if Data["error_description"] == "invalid authorization_code":
                Domoticz.Error("Please create new Authorization Code, click below link")
                Domoticz.Error("https://api.home-connect.com/security/oauth/authorize?response_type=code&client_id="+self.ClientID+"&scope=IdentifyAppliance%20Monitor&redirect_uri="+self.RedirectURI)
#                self.RefreshAccessToken.Connect()

#            if _plugin.GetToken.Connected():
#               _plugin.GetToken.Disconnect()
#            if _plugin.GetData.Connected():
#               _plugin.GetData.Disconnect()

    def onHeartbeat(self):
        Domoticz.Log("heart")
        WriteDebug("onHeartbeat")
        HourNow = (datetime.now().hour)
        MinuteNow = (datetime.now().minute)

        self.Count += 1
        if self.Count == 7 and _plugin.GetData == True:  # check every minute
            self.RefreshAccessToken.Connect()

#            Domoticz.Log("getd")
#            self.GetAccessToken.Connect()
#            GetAppliances(_plugin.AccessToken)


            self.Count = 0
#        if self.Count == 4:  # check every minute

#            GetOperationState(_plugin.AccessToken, _plugin.DevicehaId, _plugin.DeviceName)
#        if HourNow == 0 and MinuteNow == 0 and self.GetData is False:
#            _plugin.GetData = True

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def GetAccessToken(RefreshToken):
    GetToken.Connect()

def UpdateDevice(Unit, nValue, sValue, Name, Brand, VIB, Type, eNumber, haId):
    if (Unit in Devices):
        if (Devices[Unit].nValue != nValue) or (Devices[Unit].sValue != sValue):
            Devices[Unit].Update(nValue, str(sValue))
    if (Unit not in Devices):
        if sValue == "-32768":
            return
        elif Unit == 1:
            Domoticz.Device(Name=Name+" Connected", Unit=Unit, TypeName="Text", Used=1, Image=(_plugin.ImageID), Description="Brand="+str(Brand)+"\ntype="+str(VIB)+"\neNumber="+str(eNumber)+"\nhaId="+str(haId)).Create()
        elif Unit == 2:
            Domoticz.Device(Name=Name+" State", Unit=Unit, TypeName="Text", Used=1, Image=(_plugin.ImageID)).Create()


def GetAppliances(Token):
    Domoticz.Log("GetAppl")


    headers = { "Authorization": "Bearer "+Token }
    Appliances = requests.get("https://api.home-connect.com/api/homeappliances", headers=headers)
    #Domoticz.Log(str(Appliances.content))
    Domoticz.Log(str(Appliances.status_code))

    _plugin.Status = int(Appliances.status_code)
    Appliances = Appliances.json()
    if _plugin.Status != 200:
        CheckStatus(_plugin.Status, Appliances)
    else:
        for each in Appliances["data"]["homeappliances"]:
#            Domoticz.Log(str(each))
            name = each["name"]
            brand = each["brand"]
            vib = each["vib"]
            connected = each["connected"]
            type = each["type"]
            enumber = each["enumber"]
            haId = each["haId"]
            Domoticz.Log(str(name))
            UpdateDevice(1, 0, connected, name, brand, vib, type, enumber, haId)
            GetOperationState(_plugin.AccessToken, haId, name)
            _plugin.DeviceName = name
            _plugin.DevicehaId = haId
#            _plugin.GetOperationState.Connect()



def GetTokens(ClientID, ClientSecret, Code, URL):

    data={"grant_type":"authorization_code","client_id":ClientID,"client_secret":ClientSecret,"code":Code,"redirect_uri":URL}
    headers = { 'Content-Type': 'application/x-www-form-urlencoded'}
    Tokens=requests.post("https://api.home-connect.com/security/oauth/token", data=data, headers=headers)
    Domoticz.Log("Message="+str(Token.json()))
    Domoticz.Log("Status="+str(Token.status_code))

    return Tokens

def GetOperationState(Token, haIds, Names):
#    Domoticz.Log(str(Token))
    #Domoticz.Log(str(haIds))
    #Domoticz.Log(str(Names))

    headers = { "Authorization": "Bearer "+Token }
    OperationState=requests.get("https://api.home-connect.com/api/homeappliances/"+haIds+"/status/BSH.Common.Status.OperationState", headers=headers)
    Domoticz.Log(str(OperationState.status_code))
    Domoticz.Log(str(OperationState.json()))
    OperationState = OperationState.json()
    OperationState = OperationState["data"]["value"]
    OperationState = OperationState.split(".")
    OperationState = OperationState[-1]
    UpdateDevice(2, 0, str(OperationState), Names, 0, 0, 0, 0, 0)
    Domoticz.Log(str(OperationState))

def GetNewAccessCode(RefreshToken, ClientSecret):

    data={"grant_type":"refresh_token","refresh_token":RefreshToken,"client_secret":ClientSecret}
    headers = { 'Content-Type': 'application/x-www-form-urlencoded'}
    NewAccessCode=requests.post("https://api.home-connect.com/security/oauth/token", data=data, headers=headers)
#    Domoticz.Log("Message="+str(NewToken.json()))
#    Domoticz.Log("Status="+str(NewToken.status_code))
    Data = json.loads(NewAccessCode.content)
    _plugin.AccessToken = Data["access_token"]
    _plugin.RefreshToken = Data["refresh_token"]
#    Domoticz.Log("ny token"+str(_plugin.token))
    Domoticz.Log("ny refresh "+str(_plugin.RefreshToken))

    return NewAcessCode

def CheckStatus(Status, Data):
    Domoticz.Error("Status Code = "+str(Status))
    Domoticz.Error("Error: "+str(Data["error"]["key"])+", "+str(Data["error"]["description"]))
    _plugin.GetData = False

def CheckInternet():
    WriteDebug("Entered CheckInternet")
    try:
        WriteDebug("Ping")
        requests.get(url='https://api.home-connect.com/', timeout=2)
        WriteDebug("Internet is OK")
        return True
    except:
        if _plugin.GetRefresh.Connected():
            _plugin.GetRefresh.Disconnect()
        if _plugin.GetToken.Connected():
            _plugin.GetToken.Disconnect()
        if _plugin.GetData.Connected():
            _plugin.GetData.Disconnect()
        WriteDebug("Internet is not available")
        return False

def WriteDebug(text):
    if Parameters["Mode6"] == "Yes":
        timenow = (datetime.now())
        logger.info(str(timenow)+" "+text)

def CreateFile():
    if not os.path.isfile(dir+'/HomeConnect.ini'):
        data = {}
        data["Config"] = []
        data["Config"].append({
            "Refresh": "",
            })
        with open(dir+'/HomeConnect.ini', 'w') as outfile:
            json.dump(data, outfile, indent=4)

def CheckFile(Parameter):
    if os.path.isfile(dir+'/HomeConnect.ini'):
        with open(dir+'/HomeConnect.ini') as jsonfile:
            data = json.load(jsonfile)
            data = data["Config"][0][Parameter]
            if data == "":
                _plugin.AllSettings = False
            else:
                return data

def WriteFile(Parameter,text):
    CreateFile()
    with open(dir+'/HomeConnect.ini') as jsonfile:
        data = json.load(jsonfile)
    data["Config"][0][Parameter] = text
    with open(dir+'/HomeConnect.ini', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data):
    _plugin.onMessage(Connection, Data)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

    # Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return
