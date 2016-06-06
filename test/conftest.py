

import pytest
from kvpio import api_base


def pytest_addoption(parser):
    parser.addoption(
        '--local',
        action='store_true',
        default=False,
        help='use localhost for testing rather than api.kvp.io'
    )


def pytest_generate_tests(metafunc):
    if 'api_base' in metafunc.fixturenames:
        local = metafunc.config.option.local
        localhost = 'http://localhost:8000'
        metafunc.parametrize('api_base', [localhost if local else api_base])


@pytest.fixture
def valid_api_key():
    return 'steelhive'

@pytest.fixture
def invalid_api_key():
    return 'foobar'

@pytest.fixture(params=[
    # tuple of
    # (key, value,
    #  access key, expected value)
    ('foo', 'bar',
     'foo', 'bar'),

    ('foo', {'bar': {'baz': 123}},
     'foo/bar/baz', 123),

    ('foo', [1, {'10': 'Ten', '20': [46], '2': 'two'}, 3],
     'foo/1', 1),

    ('foo', [1, {'10': 'Ten', '20': [46], '2': 'two'}, 3],
     'foo/1', 1),

    ('foo', [1, {'10': 'Ten', '20': [46], '2': 'two'}, 3],
     'foo/2/10', 'Ten'),

    ('foo', [1, {'10': 'Ten', '20': [46], '2': 'two'}, 3],
     'foo/2/20/1', 46)
])
def bucket_data(request):
    return request.param

@pytest.fixture(params=[
    # tuple of
    # (key, value,
    #  bucket key, bucket value,
    #  resulting template)
    ('far', 'Test template: {{ foo }} should equal bar',
     'foo', 'bar',
     'Test template: bar should equal bar'),

    ('far', 'Test template: {{ foo.bar.baz }} should equal 123',
     'foo', {'bar': {'baz': 123}},
     'Test template: 123 should equal 123'),

    ('far', 'What is {{ foo[1]["20"][0] }} and {{ foo[1]["2"] }} about anyway...',
     'foo', [1, {'10': 'Ten', '20': [46], '2': 'two'}, 3],
     'What is 46 and two about anyway...')
])
def template_data(request):
    return request.param
