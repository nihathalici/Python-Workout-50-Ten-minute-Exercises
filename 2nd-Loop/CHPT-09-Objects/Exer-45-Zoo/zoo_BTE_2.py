
'''
As things currently stand, we’re treating our Zoo class almost as if it’s
a singleton object—that is, a class that has only one instance. What a sad
world that would be, with only one zoo! Let’s assume, then, that we have two
instances of Zoo, representing two different zoos, and that we would like
to transfer an animal from one to the other. Implement a Zoo.transfer_animal
method that takes a target_zoo and a subclass of Animal as arguments.
The first animal of the specified type is removed from the zoo on which
we’ve called the method and inserted into the first cage in the target zoo.
'''
