
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        """Add one or more scoops to the bowl"""
            for one_scoop in new_scoops:
                if len(self.scoops) < self.max_scoops:
                    self.scoops.append(one_scoop)

    def __repr__(self):
            return '\n'.join(s.flavor for s in self.scoops)

class BigBowl(Bowl):
    max_scoops = 5

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4, s5)
print(bb)  # now prints 5 flavors
