import requests  # εισαγωγή της βιβλιοθήκης

url = input("Enter a URL:") #1

resp= requests.get(url) #2
print("HTTP Response Headers:")
for header,value in resp.headers.items(): #3
    print("\nHeader=", header, "\nValue=", value)

softw=resp.headers.get('Server') #a
if softw !=0:
    print("\nSoftware: ", softw)

count =0
cookies = resp.cookies
if cookies!=0: #b
    print("\nCookies:") 
    for cookie in cookies: #c
        count+=1 
        print("\n", count, " Name: " , cookie.name ,"  , Exp Date: ", cookie.expires)