
`kvp.io <https://www.kvp.io>`_ is a micro-service designed to empower
automation, in any cloud, in any data-center, with ease.

kvp.io-python
-------------

The python (3.5) library and cli for `kvp.io <https://www.kvp.io>`_.

Installation
------------

``pip install kvpio-python``

Documentation
-------------

See `kvp.io-python <https://kvpio.github.io/kvp.io-python-docs>`_ for the API
docs.

kvpio CLI
---------

The cli is a simple utility suitable for use by itself or in an automation
pipeline.

An API key must be provided via one of the following:

- at the command line with the ``--api-key`` switch
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
