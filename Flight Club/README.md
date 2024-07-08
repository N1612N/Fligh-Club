### Program Final Output
```
                               ._                             
                              |* ;                            
            `*-.              |"":                            
             \  \             |""                             
              .  \            |   :                           
              `   \           |                               
               \   \          |    ;               +.         
                .   \         |                   *._`-.      
                `    \        |     :          .-*'  `. `.    
                _\    \.__..--**--...L_   _.-*'      .'`*'    
               /  `*-._\   -.       .-*"*+._       .'         
              :        ``*-._*.     \      _J.   .'           
          .-*'`*-.       ;     `.    \    /   `.'             
      .-*'  _.-*'.     .-'       `-.  `-.:   _.'`-.           
   +*' _.-*'      `..-'             `*-. `**'      `-.        
    `*'          .-'      ._            `*-._         `.      
              .-'         `.`-.____..+-**""'         .*"`.    
         ._.-'          _.-*'':$$$;._$              /     `.  
      .-'  `.      _.-*' `*-.__T$P   `"**--..__    :        `.
.'..-'       \_.-*'                            `"**--..___.-*'
`. `.    _.-*'                                                
  `. `:*'                                                     
    `. `.                                                     
      `*

___________.__  .__       .__     __    _________ .__       ___.    
\_   _____/|  | |__| ____ |  |___/  |_  \_   ___ \|  |  __ _\_ |__  
 |    __)  |  | |  |/ ___\|  |  \   __\ /    \  \/|  | |  |  \ __  \ 
 |     \   |  |_|  / /_/  >   Y  \  |   \     \___|  |_|  |  / \_\  |
 \___  /   |____/__\___  /|___|  /__|    \______  /____/____/|___  /
     \/           /_____/      \/               \/               \/ 

[#] Fetching User Database
[#] Data Fetched Successfully
[#] Amadues API Authentication in Progress
[#] Access Token Retrieved: QUr5zGJ3r76bfjFHGreDactEd
[#] Authentication Successful
[#] Validating IATA Codes
[#] IATA Codes Validation Successful
[#] Fetching User Database
[#] Fetching User Database...
[#] Fetching Customer Emails
[#] No Tickets Available for Paris
[+] Tickets Available for Frankfurt
[+] Sending Email to redacted@gmail.com !
[+] Sending Email to redacted@nothing.com !
[+] Sending Email to redacted@something.com !
[+] Sending Email to redacted@gmail.com !
[+] SMS has been queued to 91redacted
[#] No Tickets Available for Tokyo
[#] No Tickets Available for Istanbul
[#] No Tickets Available for Dublin

Process finished with exit code 0
```

---

#### Program Requirements
```
This program to run successfully requires API Keys and Communication mediums.

APIs Used for this program:

Google Sheet Data Management - https://sheety.co/

Amadeus Flight Search API (Free Signup, Credit Card not required) - https://developers.amadeus.com/

Twilio Messaging (SMS or WhatsApp) API - https://www.twilio.com/docs/messaging/quickstart/python

Google mail address with apppassword key to send customer mails. (2FA Enabled)

A mobile number to send messages to for testing.

Configure the .env file in the home directory with your API keys and communication mediums like EMail Address and Mobile Number.
```
