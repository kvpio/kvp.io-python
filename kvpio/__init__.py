# -*- coding: utf-8 -*-
"""
kvpio
-----
The core python bindings for [kvp.io](https://www.kvp.io)

Accessing account information:

    #!python
    import kvpio
    kvpio.api_key = '123abc'
    account = kvpio.Account().get()

Writing to your bucker:

    #!python
    data = {
        'foo': 123,
        'bar': True,
        'baz': {
            'boo': 321,
            'far': False,
            'faz': [1, 2, 3]
        }
    }
    bucket = kvpio.Bucket()
    bucket.set('my_key', data)

Reading from your bucket:

    #!python
    data = bucket.get('my_key/baz/faz')

- `copyright` (c) 2016 by Steelhive, LLC
- `license` MIT, see LICENSE for more details

"""

import os
import json
import requests
import logging


log = logging.getLogger(__name__)
api_key = None
api_ver = 'v1'
api_base = 'https://api.kvp.io'
http_methods = [
    'get',
    'post',
    'delete'
]

class Endpoint(object):
    """
    Represents an API endpoint from the client-side's perspective. This
    class should not need to be instantiated manually. It is essentially a
    convenience wrapper for the [requests](http://docs.python-requests.org)
    library.

    params:

    * `name` name of the api endpoint to access, e.g., 'bucket'
    """

    name = None

    def __init__(self, name):
        self.name = name

    @property
    def auth(self):
        return (api_key, '')

    @property
    def url(self):
        return '/'.join([api_base, api_ver, self.name])

    def request(self, method, key=None, params=None, json=None):
        """
        A simple request wrapper. Used by get, post, etc. methods.

        params:

        * `method` a supported HTTP verb
        * `key` a key path appended to an endpoint url
        * `params` the url parameters to pass to the endpoint
        * `json` a JSON encodable value to pass to the endpoint

        returns:

        * `tuple`: a tuple of the form (int, str) where the first element is
            the response code and the second is a JSON decodable value or an
            empty string
        """
        if method not in http_methods:
            raise Exception('Unsupported method attempted: {}'.format(method))
        response = getattr(requests, method)(
            '{}/{}'.format(self.url, path),
            params=params,
            json=json,
            auth=self.auth
        )
        return (response.status_code, response.text)


class Account(Endpoint):
    """Provides access to account information."""

    def __init__(self):
        super(Account, self).__init__('account')

    def get(self):
        """Requests the current account information as a JSON string, e.g.,
        ```
            {
                'id': 'Account Name',
                'email': 'you@domain.tld',
                'reads': 154,
                'size': 140762
            }
        ```

        returns:

        * `tuple` status code, JSON encoded string representation of the account
        """
        return self.request('get')


class Bucket(Endpoint):
    """Provides access to bucket (key/value pair) storage."""

    def __init__(self):
        super(Bucket, self).__init__('bucket')

    def list(self):
        """Retrieves the current list of keys.

        returns:

        * `tuple` status code, JSON encoded list of keys
        """
        return self.request('get')

    def get(self, key):
        """Retrieves either the value stored at the key.

        params:

        - `key` the key or key path under which a value is stored

        returns:

        - `tuple` status code, JSON encoded string of the value
        """
        return self.request('get', key)

    def set(self, key, data):
        """Assigns a value to the key path.

        params:

        - `key` the key or key path under which a value is stored
        - `data` JSON encodable value to assign to store under key

        returns:

        - `tuple` status code, empty string
        """
        return self.request('post', key, json=data)

    def delete(self, key):
        """Deletes a key, it's value, and all values beneath it.

        params:

        - `key` the key or key path under which a value is stored

        returns:

        - `tuple` status code, empty string
        """
        return self.request('delete', key)


class Templates(Endpoint):
    """Provides access to templates storage."""

    def __init__(self):
        super(Templates, self).__init__('templates')

    def list(self):
        """Retrieves the current list of templates.

        returns:

        - `tuple` status code, JSON encoded list of templates
        """
        return self.request('get')

    def get(self, key, data=None, raw=False):
        """Retrieves the template stored at key.

        The template is rendered with data pulled from the account's bucket
        using the `Jinja2 <http://jinja.pocoo.org>`_ engine.

        If `raw` is `True, returns the template un-rendered.

        If `data` is provided, it is used to override bucket values.

        params:

        - `key` the key or key path under which the template is stored
        - `data` JSON encodable value used to override bucket data
        - `raw` whether or not to render the template

        :returns

        - `tuple` status code, the rendered, or un-rendered, template document
        """
        return self.request('get', key, params={'raw': raw}, json=data)

    def set(self, key, template):
        """Stores the template document under key.

        params:

        - `key` the key under which the template will be stored
        - `template` the template document, optionally written with Jinja2

        returns:
        - `tuple` status code, empty string
        """
        return self.request('post', key, json=json)

    def delete(self, key):
        """Deletes a key and it's template document.

        params:

        - `key` the key under which the template is stored

        returns:

        - `tuple` status code, empty string
        """
        return self.delete('delete', key)
