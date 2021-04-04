# Home Connect Python Plugin
#
# Author: flopp999
#
"""
<plugin key="Home Connect" name="Home Connect 0.1" author="flopp999" version="0.1" wikilink="https://github.com/flopp999/" externallink="https://www.ink.com/">
    <description>
        <h2>Siemens is used to read data from https://api.home-connect.com</h2><br/>
        <h2>Support me with a coffee &<a href="https://www.buymeacoffee.com/flopp999">https://www.buymeacoffee.com/flopp999</a></h2><br/>
        <h3>Features</h3>
        <ul style="list-style-type:square">
            <li>..</li>
        </ul>
        <h3>Devices</h3>
        <ul style="list-style-type:square">
            <li>xxxxxxxxxxxxxxxxx</li>
        </ul>
        <h3>How to get your Identifier, Secret and URL?</h3>
        <h4>&<a href="https://github.com/flopp999/link-Domoticz#identifier-secret-and-callback-url">https://github.com/flopp999/NIBEUplink-Domoticz#identifier-secret-and-callback-url</a></h4>
        <h3>How to get your Access Code?</h3>
        <h4>&<a href="https://github.com/flopp999/link-Domoticz#access-code">https://github.com/flopp999/NIBEUplink-Domoticz#access-code</a></h4>
        <h3>How to get your System ID?</h3>
        <h4>&<a href="https://github.com/flopp999/link-Domoticz#system-id">https://github.com/flopp999/NIBEUplink-Domoticz#system-id</a></h4>
        <h3>Configuration</h3>
    </description>
    <params>
        <param field="Username" label="Siemens Client ID" width="320px" required="true" default="Client ID"/>
        <param field="Mode2" label="Siemens Client Secret" width="350px" required="true" default="Client Secret"/>
        <param field="Address" label="Siemens Redirect URI" width="950px" required="true" default="Redirect URI"/>
        <param field="Mode1" label="Siemens Authorization Code" width="350px" required="true" default="Authorization Code"/>
        <param field="Mode3" label="Siemens Refresh Token" width="350px" default="Copy Refresh Token from Log to here" required="true"/>
        <param field="Mode6" label="Debug to file (Nibe.log)" width="70px">
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
        self.AccessToken = ''
        self.loop = 0
        self.Count = 5
        return

    def onStart(self):
        WriteDebug("onStart")
        self.ClientID = Parameters["Username"]
        self.RedirectURI = Parameters["Address"]
        self.AuthorizationCode = Parameters["Mode1"]
        self.ClientSecret = Parameters["Mode2"]
        self.RefreshToken = Parameters["Mode3"]
        self.Status = ""
        self.GetData = True
        self.haId = ""
        self.DevicesName = []
        self.DeviceshaId = []
#        if len(self.Ident) < 32:
#            Domoticz.Log("Identifier too short")
#            WriteDebug("Identifier too short")
#            self.Ident = CheckFile("Ident")
#        else:
#            WriteFile("Ident",self.Ident)

#        if len(self.URL) < 26:
#            Domoticz.Log("URL too short")
#            WriteDebug("URL too short")
#            self.URL = CheckFile("URL")
#        else:
#            WriteFile("URL",self.URL)

#        if len(self.Access) < 370:
#            Domoticz.Log("Access Code too short")
#            WriteDebug("Access Code too short")
#            self.Access = CheckFile("Access")
#        else:
#            WriteFile("Access",self.Access)

#        if len(self.Secret) < 44:
#            Domoticz.Log("Secret too short")
#            WriteDebug("Secret too short")
#            self.Secret = CheckFile("Secret")
#        else:
#            WriteFile("Secret",self.Secret)

        if len(self.RefreshToken) < 125:
            Domoticz.Log("Refresh too short")
            WriteDebug("Refresh too short")
            self.RefreshToken = ""
#        else:
#            WriteFile("Refresh",self.Refresh)

#        if len(self.SystemID) < 4:
#            Domoticz.Log("System ID too short")
#            WriteDebug("System ID too short")
#            self.SystemID = CheckFile("SystemID")
#        else:
#            WriteFile("SystemID",self.SystemID)

#        if 'NIBEUplink' not in Images:
#            Domoticz.Image('NIBEUplink.zip').Create()

#        self.ImageID = Images["NIBEUplink"].ID
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

#                with open(dir+'/NIBEUplink.ini') as jsonfile:
#                    data = json.load(jsonfile)
#                data["Config"][0]["Access"] = Data["access_token"]
#                with open(dir+'/NIBEUplink.ini', 'w') as outfile:
#                    json.dump(data, outfile, indent=4)
#                self.GetToken.Disconnect()
#                self.GetData.Connect()


#        else:
#            Domoticz.Error(str("Status "+str(self.Status)))
#            Domoticz.Error(str(Data))
#            if _plugin.GetToken.Connected():
#                _plugin.GetToken.Disconnect()

    def onHeartbeat(self):
        WriteDebug("onHeartbeat")
        HourNow = (datetime.now().hour)
        MinuteNow = (datetime.now().minute)

        self.Count += 1
        if self.Count == 6 and _plugin.GetData == True:  # check every minute
# and _plugin.Status == 200:
            a = GetAppliances(_plugin.AccessToken)
            self.Count = 0
            GetOperationState(_plugin.AccessToken, _plugin.DeviceshaId, _plugin.DevicesName)
        if HourNow == 0 and MinuteNow == 0 and self.GetData is False:
            _plugin.GetData = True
#            if not _plugin.GetDataCurrent.Connected() and not _plugin.GetDataCurrent.Connecting():
#                WriteDebug("onHeartbeatGetDataCurrent")
#                _plugin.GetDataCurrent.Connect()
#        Domoticz.Log(str(self.refreshtoken))

#        GetData =
#        if self.Status == 200:
#            NewToken = getnewtoken(_plugin.refreshtoken,_plugin.Secret)
#        Domoticz.Log(str(getappliance(self.Token)))


global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def UpdateDevice(Unit, nValue, sValue, Name, Brand, VIB, Type, eNumber, haId):
    if (Unit in Devices):
        if (Devices[Unit].nValue != nValue) or (Devices[Unit].sValue != sValue):
            Devices[Unit].Update(nValue, str(sValue))
    if (Unit not in Devices):
        if sValue == "-32768":
            return
        elif Unit == 1:
            Domoticz.Device(Name=Name+" Connected", Unit=Unit, TypeName="Text", Used=1, Description="Brand="+str(Brand)+"\ntype="+str(VIB)+"\neNumber="+str(eNumber)+"\nhaId="+str(haId)).Create()
        elif Unit == 2:
            Domoticz.Device(Name=Name+" State", Unit=Unit, TypeName="Text", Used=1).Create()


def GetAppliances(Token):

    headers = { "Authorization": "Bearer "+Token }
    Appliances = requests.get("https://api.home-connect.com/api/homeappliances", headers=headers)
    Domoticz.Log(str(Appliances.content))
    Domoticz.Log(str(Appliances.status_code))

    _plugin.Status = int(Appliances.status_code)
    Appliances = Appliances.json()
    if _plugin.Status != 200:
        _plugin.Status = Appliances["error"]["key"]
        CheckStatus(_plugin.Status, Appliances)
    else:
        for each in Appliances["data"]["homeappliances"]:
            Domoticz.Log(str(each))
        name = each["name"]
        brand = each["brand"]
        vib = each["vib"]
        connected = each["connected"]
        type = each["type"]
        enumber = each["enumber"]
        haId = each["haId"]
        Domoticz.Log(str(name))
        UpdateDevice(1, 0, connected, name, brand, vib, type, enumber, haId)
        _plugin.DevicesName.append(name)
        _plugin.DeviceshaId.append(haId)


#    return Token

def GetTokens(ClientID, ClientSecret, Code, URL):

    data={"grant_type":"authorization_code","client_id":ClientID,"client_secret":ClientSecret,"code":Code,"redirect_uri":URL}
    headers = { 'Content-Type': 'application/x-www-form-urlencoded'}
    Tokens=requests.post("https://api.home-connect.com/security/oauth/token", data=data, headers=headers)
#    Domoticz.Log("Message="+str(Token.json()))
#    Domoticz.Log("Status="+str(Token.status_code))

    return Tokens

def GetOperationState(Token, haIds, Names):
    Domoticz.Log(str(Token))
    Domoticz.Log(str(haIds))
    Domoticz.Log(str(Names))

#    data={"grant_type":"authorization_code","client_id":ClientID,"client_secret":ClientSecret,"code":Code,"redirect_uri":URL}
    headers = { "Authorization": "Bearer "+Token }
    for Name, haId in zip(Names, haIds):
        OperationState=requests.get("https://api.home-connect.com/api/homeappliances/"+haId+"/status/BSH.Common.Status.OperationState", headers=headers)
        Domoticz.Log(str(OperationState.status_code))
        Domoticz.Log(str(OperationState.json()))
        OperationState = OperationState.json()
        OperationState = OperationState["data"]["value"]
        OperationState = OperationState.split(".")
        OperationState = OperationState[-1]
        UpdateDevice(2, 0, OperationState, Name, 0, 0, 0, 0, 0)
        Domoticz.Log(str(OperationState))



#####           curl -X GET "https://simulator.home-connect.com/api/homeappliances/010090386487001856/status/OperationState" -H "accept: application/vnd.bsh.sdk.v1+json" -H "Accept-Language: en-GB"

#    Domoticz.Log("Message="+str(Token.json()))
#    Domoticz.Log("Status="+str(Token.status_code))

#    return Tokens

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

def CreateFile():
    if not os.path.isfile(dir+'/HomeConnect.ini'):
        data = {}
        data["Config"] = []
        data["Config"].append({
             "Access": "",
             "Charge": "",
             "Ident": "",
             "Refresh": "",
             "Secret": "",
             "SystemID": "",
             "URL": ""
             })
        with open(dir+'/HomeConnect.ini', 'w') as outfile:
            json.dump(data, outfile, indent=4)

def CheckStatus(Status, Data):

    if Status != "200":
        Domoticz.Error("Status = "+str(Status))
        Domoticz.Error("Error: "+str(Data["error"]["description"]))
        _plugin.GetData = False

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
    with open(dir+'/NIBEUplink.ini') as jsonfile:
        data = json.load(jsonfile)
    data["Config"][0][Parameter] = text
    with open(dir+'/NIBEUplink.ini', 'w') as outfile:
        json.dump(data, outfile, indent=4)

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
