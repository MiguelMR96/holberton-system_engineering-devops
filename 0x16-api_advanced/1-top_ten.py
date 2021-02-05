#!/usr/bin/python3
"""Function that queries the Reddit API
"""

import json
import requests


def top_ten(subreddit):
    """Function to prints the titles of the first 10 hot posts of a
    subreddit
    """

    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "User Agent"}
    response = requests.get(url + subreddit + "/hot.json?limit=10",
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")
