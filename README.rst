

`kvp.io <https://www.kvp.io>`_ is a micro-service designed to empower
automation, in any cloud, in any data-center, with ease.

kvp.io-python
-------------
The python library and cli for `kvp.io <https://www.kvp.io>`_.

Installation
------------
``pip install kvpio-python``

Tests
-----
Requires ``pytest`` and ``pytest-cov``.

``py.test --cov-report term --cov=kvpio``

API Documentation
-----------------
See `kvp.io-python <https://kvpio.github.io/kvp.io-python-docs>`_ for the API
docs.

CLI Documentation
-----------------
The cli is a simple utility suitable for use by itself or in an automation
pipeline.

An API key must be provided via one of the following:

- as an environment variable name ``KVPIO_APIKEY``
- as a single line in the file ``~/.kvpio``

**Usage:**

.. code:: bash

    kvpio --help
    Usage: kvpio [OPTIONS] COMMAND [ARGS]...

      kvpio v0.1.5

      usage:

        kvpio account

        kvpio bucket    list|get|set|del

        kvpio template  list|get|set|del

    Options:
      --api-key TEXT  the kvp.io api key to use
      --verbose       turn on detailed output
      --help          Show this message and exit.

    Commands:
      bucket    Interact with key/value pairs.
      account   Get account information.
      template  Interact with templates.

CLI Examples
------------

Here are a few examples to get you familiar with the cli.

Basic bucket usage:

.. code:: bash

    $ export KVPIO_APIKEY=<your api key here>
    $ kvpio bucket set foo bar
    $ kvpio bucket get foo
    bar

Bucket with nested data:

.. code:: bash

    $ kvpio bucket set foo '{"bar": {"baz": 123}}'
    $ kvpio bucket get foo/bar/baz
    123

Basic template usage:

.. code:: bash

    $ kvpio template set foo 'baz is equal to {{ foo.bar.baz }}'
    $ kvpio template get foo
    baz is equal to 123

Get account information:

.. code:: bash

    $ kvpio account
    {"id": "kvp.io", "email": "support@kvp.io", "reads": 87, "size": 0}
