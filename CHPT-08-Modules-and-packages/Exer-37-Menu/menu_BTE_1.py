
'''
Write a version of menu.py that can be imported (as in the exercise), but that
when you invoke the file as a stand-alone program from the command line, tests
the function. If you aren’t familiar with testing software such as pytest, you
can just run the program and check the output.
'''


import subprocess
import sys
from io import StringIO

def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()

        print('Not a valid option')

def test_good_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('a\n'))

    def a():
        return 'called a'

    returned_value = menu(a=a)

    assert 'called a' in returned_value


def test_bad_then_good_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('q\na\n'))

    def a():
        return 'called a'

    returned_value = menu(a=a)
    captured_stdout, captured_stderr = capsys.readouterr()

    assert 'Not a valid option' in captured_stdout
    assert 'called a' in returned_value

if __name__ == '__main__':
    program_name = sys.argv[0]

    subprocess.run(f'pytest -vv {program_name}', shell= True)

