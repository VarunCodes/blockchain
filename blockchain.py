"""
import hashlib
import json
from time import time
"""

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        #creates new block and add it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        #adds new transaction to the list of transactions

        """
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> Index of block

        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        #hashes a block
        pass

    @property
    def last_block(self):
        #returns the last block in the chain
        pass
