#To install this package with conda run:
#conda install -c anaconda requests
#import requests

# internet cycle or the request response cycle
# DNS lookup
# computer makes a request to a server
# server processes the request
# server issues a response

# response status code
#2xx - Success
#3xx - Redirect
# 4xx client error your fault
# 5xx server error not your fault


           # HTTP VERB
           #GET                                      #POST
# USEFUUL FOR RETRIEVING DATA                 WRITING DATA
 # DATA PASSED IN QUERY STRING               REQUEST BODY
# NO SIDE EFFECTS                               CAN HAVE
 # CAN BE CACHED AND BOOKMARKED               CANNOT

# APPLICATION PROGRAMMING INTERFACE
 # ALLOWS TO GET DATA FROM ANOTHER APPLICATION WITHOUT NEEDING HOW THE APPLICATION WORKS
 # CAN SEND DATA IN DIFFERENT FORMATS
# EX- GITHUB SPOTIFY GOOGLE





#
#API
#icanhazdadjoke.com can be used as an API for fetching a random joke, a specific joke, or searching for jokes in a variety of formats.
#
#Calling the API
#Authentication
#No authentication is required to use the icanhazdadjoke.com API. Enjoy :)
#
#API response format
#All API endpoints follow their respective browser URLs, but we adjust the response formatting to be more suited for an API based on the provided HTTP Accept header.
#
#Accepted Accept headers:
#
#text/html - HTML response (default response format)
#application/json - JSON response
#text/plain - Plain text response
#Note: Requests made via curl which do not set an Accept header will respond with text/plain by default.
#Fetch a random dad joke
#GET https://icanhazdadjoke.com/ fetch a random dad joke.


import requests
url = "http://www.google.com/dfsdf"
response = requests.get(url)# we use get as a client while writing account we are doing post work
#response.ok TRUE
# res.text 
# status code= 200 for ouyput recieved or 404 for error page not found we
print(f"your request to {url} came back w/ status code {response.status_code}")

print(response.text)# mix of html and json
# output=your request to http://www.google.com came back w/ status code 200
# long html never ending(very large)=<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="DGZs0/759HZ98rEDdy92RA==">(function(

# header to filter json 
import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})
# headers are dictionary
data = response.json()

print(data["joke"])# gives us the joke from dictionary keeps changing
print(f"status: {data['status']}")
#A horse walks into a bar. The bar tender says "Hey." The horse says "Sure."
#status: 200



########################################3with parameters
import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1} # we want 1 cat joke
)

data = response.json()
type(data)# dictionary  with key id,joke,status
# response.txt is a string therefore not used as a dictionary is better
print(data["results"])# gives a list of dictionary with id and joke two keyvalue pair
# output
#[{'id': 'iGJeVKmWDlb', 'joke': 'My cat was just sick on the carpet, I don’t think it’s feline well.'}]

############################################################################ case sensitivity doesnot matter
import requests
import pyfiglet
import termcolor
from random import choice

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="magenta")
print(header)

term = input("Let me tell you a joke! Give me a topic: ")
response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": term}
).json()
results = response_json["results"]
print(results)# to get the dictionary
total_jokes = response_json["total_jokes"]
print(total_jokes)# to get the no of jokes
if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {term}. Here's one:\n",
        choice(results)['joke']
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {term}. Here it is:\n",
        results[0]['joke']# one item gets printed
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")
#
#____            _       _       _          _____  ___   ___   ___  
#|  _ \  __ _  __| |     | | ___ | | _____  |___ / / _ \ / _ \ / _ \ 
#| | | |/ _` |/ _` |  _  | |/ _ \| |/ / _ \   |_ \| | | | | | | | | |
#| |_| | (_| | (_| | | |_| | (_) |   <  __/  ___) | |_| | |_| | |_| |
#|____/ \__,_|\__,_|  \___/ \___/|_|\_\___| |____/ \___/ \___/ \___/     
       
#Let me tell you a joke! Give me a topic: mom
#I've got one joke about mom. Here it is:
#I've been trying to come up with a dad joke about momentum . . . but I just can't seem to get it going.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    