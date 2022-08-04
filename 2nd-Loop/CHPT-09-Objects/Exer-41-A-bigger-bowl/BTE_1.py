'''
Write an Envelope class, with two attributes, weight (a float, measuring grams)
and was_sent (a Boolean, defaulting to False). There should be three methods:
(1) send, which sends the letter, and changes was_sent to True, but only after
the envelope has enough postage; (2) add_postage, which adds postage equal to its
argument; and (3) postage_needed, which indicates how much postage the envelope
needs total. The postage needed will be the weight of the envelope times 10.

Now write a BigEnvelope class that works just like Envelope except that the postage
is 15 times the weight, rather than 10.
'''

class NotEnoughPostageError(Exception):
    pass

class Envelope():

    postage_multiplier = 10

    def __init___(self, weight):
        self.weight = weight
        self.postage = 0
        self.was_sent = False

    def add_postage(self, amount):
        self.postage += amount
        
    def send(self):
        if self.postage >= self.weight * self.postage_multiplier:
            return self.was_sent = True
        raise NotEnoughPostageError('Not enough postage')



class BigEnvelope(Envelope):
    postage_multiplier = 15

