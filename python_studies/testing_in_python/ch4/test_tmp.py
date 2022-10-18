'''
The package pytest provides some builtin fixtures, being 'tmp_path_factory' one
of them.
'''
def test_tmp_path_factory(tmp_path_factory):
    path = tmp_path_factory.mktemp("sub") # mktemp() returns a 'Path' object
    file = path / "file.txt"
    file.write_text("Hello")
    assert file.read_text() == "Hello"


