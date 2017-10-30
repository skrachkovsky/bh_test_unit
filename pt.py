import pytest
import math

def setup():
    print('load test')

def teardown():
    print('finish test')


def setup_function(fn):
    print('load %s function' % str(fn))


def test_int():
    print('test int')
    assert int('1') == 1


def test_float():
    print('test float')
    assert float('1.1') == 1.1


@pytest.fixture()
def int_fixt(request):
    print('init fixt')
    def td():
        print('finiths fixt')
    request.addfinalizer(td)
    return [1, 2]

def test_int2(int_fixt):
    assert len(int_fixt) == 2
    assert isinstance(int_fixt[0], int)
    assert isinstance(int_fixt[1], int)


@pytest.yield_fixture(scope='function', params=[2])
def float_fixt():
    print('init fixt2')
    yield [2.0, 3.0]
    print('finish fixt2')


def test_float2(float_fixt):
    assert len(float_fixt) == 2
    assert isinstance(float_fixt[0], float)
    assert isinstance(float_fixt[1], float)


def interr():
    int('1.0')

def test_exception():
    with pytest.raises(ValueError):
        interr()