'''
Created on Mar 1, 2021

@author: rcurtis
'''
import praw

bot_name="DNBBot"
user_agent="script:DNBBot:0.1 (by u/BourbonInExile)"
trigger = 'paa'.lower()

# Create the connection to Reddit.
# This assumes a properly formatted praw.ini file exists:
#   https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit(bot_name, user_agent=user_agent)

# Get a handle on our preferred subreddit
subreddit = reddit.subreddit("WetShaving+Wicked_Edge")
