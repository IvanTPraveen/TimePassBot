import requests
desc = []
def hans(message: str) -> str:
    if message == "hr":
        return "hello"
    
    if message == "ho":
        return "bye"
    
    if message == "help":
        return "help me ahhhh im trapped in my basement"
    
    if message[0] == "!":
        message = message[1:]
        print(message)
        import requests

        url = "https://youtube138.p.rapidapi.com/video/details/"

        querystring = {"id":message,"hl":"en","gl":"US"}

        headers = {
	        "X-RapidAPI-Key": "",
	        "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()
        cards = data["title"]
        desc.append(cards)
        return desc[-1]

    return "didn't understand a single thing you are telling me"