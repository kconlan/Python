#Kevin Conlan Python 6651-01 Professor Nurmatova Search By Country Code


import urllib.request
import json

while True:
    myinput = input("Please enter the country code or select quit:")
    if( myin == "quit" ):                      
        print("Thanks for searching!")
        break
    try:
        url = "https://restcountries.eu/rest/v1/alpha/"+ myinput
        page = urllib.request.urlopen(url)
        content = page.read()                   
        content_string = content.decode("utf-8")
        json_data = json.loads(content_string) 
        print(json_data["name"], json_data["capital"])
    except urllib.error.HTTPError:             
        print("Sorry,cannot find this country code")
