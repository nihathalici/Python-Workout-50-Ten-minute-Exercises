import random

def create_password_generator(chars):

    def create_password(length):
        output = []

        for i in range(length):
            output.append(random.choice(chars))

        return ''.join(output)

    return create_password

f = create_password_generator('abcdefghij!@#$%')

print(f(10))
