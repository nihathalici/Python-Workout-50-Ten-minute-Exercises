
"""
URL-encode characters—In URLs, we often replace special and nonprintable
characters with a % followed by the character’s ASCII value in hexadecimal. For
example, if a URL is to include a space character (ASCII 32, aka 0x20), we
replace it with %20. Given a string, URL-encode any character that isn’t a letter
or number. For the purposes of this exercise, we’ll assume that all characters
are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It
might help to know about the ord (http://mng.bz/EdnJ) and hex (http://mng
.bz/nPxg) functions. 
"""
import string

def url_change(url):
    valid_char = string.ascii_lowercase + ':/.' + '0123456789'
    replace_symbol = '%'

    return ''.join([replace_symbol + str(hex(ord(ch))[2:]) if not ch.lower() in valid_char else ch for ch in url])

url = 'file://Python_Workout_50_Essential_Exercises_by_Reuven_M_Lerner.pdf'

print(url, '\n', url_change(url))
