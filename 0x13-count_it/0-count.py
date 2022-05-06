#!/usr/bin/python3
"""  prints a sorted count of given keywords """
import requests


def count_words(subreddit, word_list, counter={}, after=""):
    """ queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords """
    if len(counter) <= 0:
        for item in word_list:
            counter[item] = 0
    if after is None:
        word_list = [[key, value] for key, value in counter.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for i in word_list:
            if i[1]:
                print("{}: {}".format(i[0].lower(), i[1]))
        return None
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    parameters = {'limit': 100, 'after': after}
    head = {'user-agent': 'my-app/0.0.1'}
    call = requests.get(
        url,
        headers=head,
        params=parameters,
        allow_redirects=False,
    )
    if call.status_code == 200:
        after = call.json().get('data').get('after')
        children = call.json().get('data').get('children')
        for child in children:
            title = child.get('data').get('title')
            lower = [j.lower() for j in title.split(' ')]
            for word in word_list:
                counter[word] += lower.count(word.lower())
    else:
        return None
    count_words(subreddit, word_list, counter, after)