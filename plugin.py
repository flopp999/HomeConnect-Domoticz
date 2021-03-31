# Siemens Python Plugin
#
# Author: flopp999
#
"""
<plugin key="Siemens" name="Siemens 0.1" author="flopp999" version="0.1" wikilink="https://github.com/flopp999/" externallink="https://www.ink.com/">
    <description>
        <h2>Siemens is used to read data from api.siemens.com</h2><br/>
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
        <param field="Address" label="Siemens Callback URL" width="950px" required="true" default="URL"/>
        <param field="Mode1" label="Siemens Access Code" width="350px" required="true" default="Access Code"/>
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
import siemens
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
logger = logging.getLogger("Siemens")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(dir+'/Siemens.log', maxBytes=50000, backupCount=5)
logger.addHandler(handler)

class BasePlugin:
    enabled = False

    def __init__(self):
        self.token = ''
        self.loop = 0
        self.Count = 5
        return

    def onStart(self):
        WriteDebug("onStart")
        self.Ident = Parameters["Username"]
        self.URL = Parameters["Address"]
        self.Access = Parameters["Mode1"]
        self.Secret = Parameters["Mode2"]
        self.Refresh = Parameters["Mode3"]
        self.SystemID = Parameters["Mode4"]
        self.Charge = Parameters["Mode5"]
        self.AllSettings = True
        self.Categories = []

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

#        if len(self.Refresh) < 270:
#            Domoticz.Log("Refresh too short")
#            WriteDebug("Refresh too short")
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
        v = siemens.gettoken(self.Ident,self.Secret,self.Access,self.URL)
        Domoticz.Log(str(v))
        self.GetToken = Domoticz.Connection(Name="Get Token", Transport="TCP/IP", Protocol="HTTPS", Address="api.home-connect.com", Port="443")
        self.GetToken.Connect()

    def onConnect(self, Connection, Status, Description):
        if CheckInternet() == True:
#        if CheckInternet() == True and self.AllSettings == True:
            if (Status == 0):
                if Connection.Name == ("Get Token"):
                    Domoticz.Log("token")
                    WriteDebug("Get Token")
#                    if len(self.Refresh) > 50:
#                        self.reftoken = self.Refresh
#                    data = "grant_type=authorization_code"
#                    data += "&client_id="+self.Ident
#                    data += "&client_secret="+self.Secret
#                    data += "&code="+self.Access
#                    data += "&redirect_uri="+self.URL
                    data="grant_type=authorization_code&client_id=1B2349B9FA66DC4F2B0561673667D40E5E03267E0F015E40CF4B15C33F871BB6&client_secret=6E218B9A3E676A3B8EEBF0D20439225E9164D39B5D505CE15AE3A5E5F9D2B8C1&code=eyJ4LXJlZyI6IkVVIiwieC1lbnYiOiJQUkQiLCJ0b2tlbiI6ImE3OGM2NTFiLTE3YzUtNDZjOS05ZmY2LWU4ZGQ3MjQ0NDE2YyIsImNsdHkiOiJwcml2YXRlIn0=&redirect_uri=https://test.se"
#                    headers="a"
#          headers = { 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'api.home-connect.com', 'Authorization':''}
                    Domoticz.Log(str(data))
#                    Domoticz.Log(str(headers))
                    WriteDebug("innan token send")
#                    Connection.Send({'Verb': 'POST','URL': 'api.home-connect.com/security/oauth/token', 'Headers': headers, 'Data': data, 'Host': 'api.home-connect.com'})
                    Connection.Send({'Verb': 'POST','URL': 'http://api.home-connect.com/security/oauth/token', 'Data': data})


    def onMessage(self, Connection, Data):
        Domoticz.Log(str(Data))
        Status = int(Data["Status"])
        Data = Data['Data'].decode('UTF-8')
        WriteDebug("Status = "+str(Status))
#        Data = json.loads(Data)

        if (Status == 200):

            if Connection.Name == ("Get Token"):
                self.token = Data["access_token"]
                with open(dir+'/NIBEUplink.ini') as jsonfile:
                    data = json.load(jsonfile)
                data["Config"][0]["Access"] = Data["access_token"]
                with open(dir+'/NIBEUplink.ini', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                self.GetToken.Disconnect()
#                self.GetData.Connect()


        else:
            Domoticz.Error(str("Status "+str(Status)))
            Domoticz.Error(str(Data))
            if _plugin.GetToken.Connected():
                _plugin.GetToken.Disconnect()



    def onHeartbeat(self):
        Domoticz.Log("h")

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def UpdateDevice(ID, nValue, sValue, Unit, Name, PID, Design):
    if PID == 44896:
        ID = 61
    if PID == 44897:
        ID = 62
    if PID == 44908:
        ID = 63
    if PID == 10069:
        ID = 64
    if (ID in Devices):
        if (Devices[ID].nValue != nValue) or (Devices[ID].sValue != sValue):
            Devices[ID].Update(nValue, str(sValue))
    if (ID not in Devices):
        if sValue == "-32768":
            return
        elif Unit == "l/m":
            Domoticz.Device(Name=Name, Unit=ID, TypeName="Waterflow", Used=1, Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
        elif Unit == "°C" or ID == 56 and ID !=24:
            Domoticz.Device(Name=Name, Unit=ID, TypeName="Temperature", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
        elif Unit == "A":
            if ID == 15:
                Domoticz.Device(Name=Name+" 1", Unit=ID, TypeName="Current (Single)", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
            if ID == 16:
                Domoticz.Device(Name=Name+" 2", Unit=ID, TypeName="Current (Single)", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
            if ID == 17:
                Domoticz.Device(Name=Name+" 3", Unit=ID, TypeName="Current (Single)", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
            if ID == 53:
                Domoticz.Device(Name=Name, Unit=ID, TypeName="Current (Single)", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
        elif Name == "compressor starts":
            Domoticz.Device(Name=Name, Unit=ID, TypeName="Custom", Options={"Custom": "0;times"}, Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
        elif Name == "blocked":
            if ID == 21:
                Domoticz.Device(Name="compressor "+Name, Unit=ID, TypeName="Custom", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
            if ID == 51:
                Domoticz.Device(Name="addition "+Name, Unit=ID, TypeName="Custom", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
        elif ID == 24:
            Domoticz.Device(Name="compressor "+Name, Unit=ID, TypeName="Temperature", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
        elif ID == 41 or ID == 81:
            Domoticz.Device(Name=Name, Unit=ID, TypeName="Custom", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()
        elif ID == 61:
            Domoticz.Device(Name="comfort mode "+Name, Unit=ID, TypeName="Custom", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
        elif ID == 62:
            Domoticz.Device(Name="comfort mode "+Name, Unit=ID, TypeName="Custom", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
        elif ID == 63:
            Domoticz.Device(Name="smart price adaption "+Name, Unit=ID, TypeName="Custom", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
        elif ID == 71:
            Domoticz.Device(Name=Name, Unit=ID, TypeName="Text", Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
        elif ID == 72 or ID == 73:
            Domoticz.Device(Name=Name, Unit=ID, TypeName="Text", Used=1, Image=(_plugin.ImageID)).Create()
        elif ID == 74:
            Domoticz.Device(Name="software "+Name, Unit=ID, TypeName="Text", Used=1, Image=(_plugin.ImageID)).Create()
        else:
            if Design == "":
                Domoticz.Device(Name=Name, Unit=ID, TypeName="Custom", Options={"Custom": "0;"+Unit}, Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)).Create()
            else:
                Domoticz.Device(Name=Name, Unit=ID, TypeName="Custom", Options={"Custom": "0;"+Unit}, Used=1, Image=(_plugin.ImageID), Description="ParameterID="+str(PID)+"\nDesignation="+str(Design)).Create()

def CreateFile():
    if not os.path.isfile(dir+'/NIBEUplink.ini'):
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
        with open(dir+'/NIBEUplink.ini', 'w') as outfile:
            json.dump(data, outfile, indent=4)

def CheckFile(Parameter):
    if os.path.isfile(dir+'/NIBEUplink.ini'):
        with open(dir+'/NIBEUplink.ini') as jsonfile:
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
        requests.get(url='https://api.nibeuplink.com/', timeout=2)
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
