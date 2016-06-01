
kvp.io is a micro-service designed to empower automation, in any cloud, in
any data-center, with ease.

kvp.io client
-------------

A simple convenience utility for interacting with `kvp.io <https://www.kvp.io>`_.

See `kvp.io/docs <https://www.kvp.io/docs>`_ for detailed documentation.

.. code:: bash

    kvpio --help
    Usage: kvpio [OPTIONS] COMMAND [ARGS]...

      kvpio v0.1.0

      usage:

        kvpio customer

        kvpio bucket    list|get|set|del

        kvpio template  list|get|set|del

    Options:
      --api-key TEXT  the kvp.io api key to use
      --verbose       turn on detailed output
      --help          Show this message and exit.

    Commands:
      bucket    Interact with key/value pairs.
      customer  Get account information.
      template  Interact with templates.
