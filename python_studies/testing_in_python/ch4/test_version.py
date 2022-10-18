'''
Sometimes, the method or function that must be tested is supposed to output something
to stdout or stderr. In situations like this, it's possible to use the builtin
fixture 'capsys' as a way to read the output.
'''
import cards
def test_version_v2(capsys):
    cards.cli.version() # prints to the stdout
    output = capsys.readouterr().out.rstrip() # readouterr returns a namedtuple
    assert output == cards.__version__ # cards.__version__ is a string 
