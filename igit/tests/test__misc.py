from hypothesis import given
from hypothesis.strategies import text

from igit.tests.common import letters
from igit.util.misc import unquote


# *** unquote
def isnt_quoted(val) -> bool:
    try:
        if val[0] == '"':
            return val[-1] != '"'
        if val[0] == "'":
            return val[-1] != "'"
    except IndexError:
        return True


@given(text(letters).filter(isnt_quoted))
def test__unquote__sanity(txt):
    actual = unquote(txt)
    assert actual == txt


@given(text(letters))
def test__unquote__quoted(txt):
    single_quoted = f"'{txt}'"
    actual = unquote(single_quoted)
    assert actual == txt
    
    double_quoted = f'"{txt}"'
    actual = unquote(double_quoted)
    assert actual == txt


@given(text(letters).filter(lambda s: not s.endswith('"')))
def test__unquote__left_dbl_quote(txt):
    onequote = f'"{txt}'
    actual = unquote(onequote)
    assert actual == onequote


@given(text(letters).filter(lambda s: not s.endswith("'")))
def test__unquote__left_single_quote(txt):
    onequote = f"'{txt}"
    actual = unquote(onequote)
    assert actual == onequote


@given(text(letters).filter(lambda s: not s.startswith('"')))
def test__unquote__right_dbl_quote(txt):
    onequote = f'{txt}"'
    actual = unquote(onequote)
    assert actual == onequote


@given(text(letters).filter(lambda s: not s.startswith("'")))
def test__unquote__right_single_quote(txt):
    onequote = f"{txt}'"
    actual = unquote(onequote)
    assert actual == onequote
