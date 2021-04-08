Support me with a coffee https://www.buymeacoffee.com/flopp999 or use my Tibber link https://tibber.com/se/invite/8af85f51  
Please use my Tibber invite code, then we both get SEK 500, to use in Tibber shop. https://tibber.com/se/invite/8af85f51
---
Create a folder with name "HomeConnect" in "domoticz/plugins"  
Put plugin.py, requirements.txt in that folder
Run "pip3 install -r requirements.txt" to install all packages that this plugin needs  

or

Run in domoticz/plugins "sudo git clone h<span>ttps://gith<span>ub.com/flopp999/HomeConnect-Domoticz HomeConnect"  
Run "cd HomeConnect"  
Run "pip3 install -r requirements.txt" to install all packages that this plugin needs

---
You need to have some information to be able to use this plugin: 

[Client ID](https://github.com/flopp999/HomeConnect-Domoticz/blob/main/README.md#Client-ID,-Client-Secret-and-Redirect-URi)  
[Client Secret](https://github.com/flopp999/HomeConnect-Domoticz/blob/main/README.md#Identifier,-Secret-and-URL)  
[Redirect RUi](https://github.com/flopp999/HomeConnect-Domoticz/blob/main/README.md#Identifier,-Secret-and-Callback-URL)  
[Authorization Code](https://github.com/flopp999/HomeConnect-Domoticz/blob/main/README.md#System-ID)  
[Refresh Token](https://github.com/flopp999/HomeConnect-Domoticz/blob/main/README.md#Charge-from-your-electricity-company)  
[Access code](https://github.com/flopp999/HomeConnect-Domoticz/blob/main/README.md#Access-code)

# Client ID, Client Secret and Redirect URi  
Login to [Home Connect](https://developer.home-connect.com/applications/)  
Register new application https://developer.home-connect.com/applications/add  
*Application ID can be anything, OAuth Flow shall be "Authorization Code Grant Flow", Home Connect User... can be empty, Redirect URi can be any address, as long as it exists*  
Copy Client ID, Client Secret and Redirect URi, paste to HomeConnect hardware in Domoticz  
Create an Authorization code by replace {client_id} and {redirect_uri} with details you got during registration of new application
https://api.home-connect.com/security/oauth/authorize?response_type=code&client_id={client_id}&scope=IdentifyAppliance%20Monitor&redirect_uri={redirect_uri}

# Access code
You need to create an Access code before first use  
Click on the link below, you will get an error, that is OK  
https://api.nibeuplink.com/oauth/authorize?client_id=yyyyyy&scope=READSYSTEM&state=x&redirect_uri=https://api.nibeuplink.com/&response_type=code  
Once you clicked it, in the address bar change yyyyyy to your Identifier, NOT YOUR SYSTEM ID!!!  
Then it will ask you to login and accept.  
When this is done the address bar will look something like below  
"h<span>ttps://a<span>pi.nib<span>euplink.com/?code=ndfhj3u38ufhswhnerjqa5zEyN-RmBgkTCc&state=x"  
Copy everything after "...code=" and before "&state...", the code above is just an example, normally the code is ~380 characters
Above example have access code "ndfhj3u38ufhswhnerjqa5zEyN-RmBgkTCc"


Support me with a coffee https://www.buymeacoffee.com/flopp999 or use my Tibber link https://tibber.com/se/invite/8af85f51
