'''
Created on Mar 1, 2021

@author: rcurtis
'''

import logging
from util import trigger

def handle_comment(comment):
    logging.debug('Handling comment [%s]', comment.id)
    if trigger in comment.body.lower():
        logging.info('Comment contains %s', trigger)
        
    
def handle_submission(submission):
    logging.debug('Handling submission [%s]', submission.id)
    if submission.is_self and trigger in submission.selftext.lower():
        logging.info('Submission contains %s', trigger)
