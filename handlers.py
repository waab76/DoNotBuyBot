'''
Created on Mar 1, 2021

@author: rcurtis
'''

import logging
from util import triggers

def handle_comment(comment):
    logging.debug('Handling comment [%s]', comment.id)
    matches = {trigger for trigger in triggers.keys() if trigger in comment.body.lower()}
    if len(matches) > 0:
        logging.info('Comment [%s] contains %s : [%s]', comment.id, matches, comment.body)
        
    
def handle_submission(submission):
    logging.debug('Handling submission [%s]', submission.id)
    matches = {trigger for trigger in triggers.keys() if trigger in submission.selftext.lower()}
    if len(matches) > 0:
        logging.info('Submission [%s] contains %s : [%s]', submission.id, matches, submission.selftext)
