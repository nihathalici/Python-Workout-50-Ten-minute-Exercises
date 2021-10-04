import random

def create_p_gen(chars):

    def create_p(length):
        output = []

        for i in range(length):
            output.append(random.choice(chars))

        return ''.join(output)

    return create_p

f = create_p_gen('abcdefghij!@#$%')

print(f(10))
