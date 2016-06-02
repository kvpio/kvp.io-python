

import pytest


@pytest.fixture
def valid_api_key():
    return 'abc123'

@pytest.fixture
def invalid_api_key():
    return 'foobar'

@pytest.fixture(params=[
    # tuple of (key, value, access key, expected value)
    ('foo', 'bar', 'foo', 'bar'),
    ('foo', {'bar': {'baz': 123}}, 'foo/bar/baz', 123)
])
def bucket_data(request):
    return request.param

@pytest.fixture(params=[
    # tuple of (key, value, bucket key, bucket value, rendered template)
    ('far', 'Test template: {{ foo }} should equal bar', 'foo', 'bar', 'Test template: bar should equal bar'),
    ('far', 'Test template: {{ foo.bar.baz }} should equal 123', 'foo', {'bar': {'baz': 123}}, 'Test template: 123 should equal 123')
])
def template_data(request):
    return request.param
