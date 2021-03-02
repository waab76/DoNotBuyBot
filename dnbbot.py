'''
Created on Mar 1, 2021

@author: rcurtis
'''

import logging
import sys
import threading

from prawcore import ServerError
from praw.models.reddit import comment
from praw.models.reddit import submission

from handlers import handle_comment, handle_submission
from util import subreddit

logging.basicConfig(filename='DNBBot.log', level=logging.INFO, 
                    format='%(asctime)s :: %(levelname)s :: %(threadName)s :: %(module)s:%(funcName)s :: %(message)s ', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def monitor_submissions():
    logging.info('Monitoring submissions')
    while True:
        submission_stream = subreddit.stream.submissions()
        try:
            for submission in submission_stream:
                handle_submission(submission)
        except ServerError:
            logging.error('Reddit server is down: %s', sys.exc_info()[0], exc_info=True)
        except:
            logging.error('Caught exception: %s', sys.exc_info()[0], exc_info=True)

def monitor_comments():
    logging.info('Monitoring comments')
    while True:
        comment_stream = subreddit.stream.comments()
        try:
            for comment in comment_stream:
                handle_comment(comment)
        except ServerError:
            logging.error('Reddit server is down: %s', sys.exc_info()[0], exc_info=True)
        except:
            logging.error('Caught exception: %s', sys.exc_info()[0], exc_info=True)
        

if __name__ == '__main__':
    logging.info('Starting child threads')
    threading.Thread(target=monitor_submissions, name='submissions').start()
    threading.Thread(target=monitor_comments, name='comments').start()