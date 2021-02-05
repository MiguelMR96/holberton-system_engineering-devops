#!/usr/bin/python3
""" Function to extract data from
reddit API
"""
import json
import requests


def number_of_subscribers(subreddit):
    """Function to returns the number of subscribers
    of a given subireddit
    """

    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "User Agent"}
    response = requests.get(url + subreddit + "/about.json",
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
