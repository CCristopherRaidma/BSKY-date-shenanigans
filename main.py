
import json
from datetime import datetime, timezone
import requests

example = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
def main():
    
    handle = input("Handle: ")
    pw = input("Pass: ")

    rsp = requests.post(
        "https://bsky.social/xrpc/com.atproto.server.createSession",
        json={"identifier": handle, "password": pw})
    
    session = rsp.json()
    try:
        while True:
            PostText = input("Insert post text: ")
            DT = input("Insert date and time, EXAMPLE:" + example + " " + " : ")
            
            post = {
                "$type": "app.bsky.feed.post",
                "text": PostText,
                "createdAt": DT,
            }

            resp = requests.post(
                "https://bsky.social" + "/xrpc/com.atproto.repo.createRecord",
                headers={"Authorization": "Bearer " + session["accessJwt"]},
                json={
                    "repo": session["did"],
                    "collection": "app.bsky.feed.post",
                    "record": post,
                },
            )
            print(json.dumps(resp.json(), indent=2))
            resp.raise_for_status()
            
            
    except KeyboardInterrupt:
        print("KBDI")
        
        
if __name__ == "__main__":
    main()