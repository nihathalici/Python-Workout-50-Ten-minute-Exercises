class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)
