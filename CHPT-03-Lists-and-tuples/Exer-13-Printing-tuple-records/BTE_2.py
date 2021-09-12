'''
Define a list of tuples, in which each tuple contains the name,
length (in minutes), and director of the movies nominated for best picture
Oscar awards last year. Ask the user whether they want to sort the list
by title, length, or director’s name, and then present the list sorted
by the user’s choice of axis.
'''
import collections
from operator import itemgetter

MOVIES = [('The Father', 97, 'Florian Zeller'),
          ('Judas and the Black Messiah', 126, 'Shaka King'),
          ('Mank', 131,'David Fincher'),
          ('Minari', 115,'Lee Isaac Chung'),
          ('Nomadland', 108, 'Chloé Zhao')]

def list_of_movies_oscar(iter):
    
    opt = ('title','length','director')
    Movie = collections.namedtuple('movie',opt)
    movies = [Movie(m[0],m[1],m[-1]) for m in iter]
    
    choice = input(f'Which column to sort? {opt}: ').split(',')
    if all(map(lambda x: x.lower() in opt,choice)):
        
        s = ''
        for item in sorted(movies, key=itemgetter(*[opt.index(x.lower()) for x in choice])): 
            s += f'{item.title:27} {item.length:5} {item.director:5}\n'
        return s
    return 'Pick a correct choice!'

print(list_of_movies_oscar(MOVIES))
