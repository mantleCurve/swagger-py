About
-----

This is a Python 3 compatible fork of [Swagger.py](https://github.com/digium/swagger-py), a Python library for using
[Swagger](https://developers.helloreverb.com/swagger/) defined API's.


Usage
-----

Install the latest release from PyPI:

```bash
$ pip install git+https://github.com/mantleCurve/swagger-py
```

Or install from source using the `setup.py` script:

```bash
$ ./setup.py install
```

Requirements
-----------

- Python 3.6 or later
- httpretty>=1.1.4
- requests>=2.28.0
- websocket-client>=1.6.0

API
===

Swagger.py will dynamically build an object model from a Swagger-enabled
RESTful API.

Here is a simple example using the [Asterisk REST Interface](https://wiki.asterisk.org/wiki/display/AST/Asterisk+12+ARI):

```python
#!/usr/bin/env python3

import json

from swaggerpy.client import SwaggerClient
from swaggerpy.http_client import SynchronousHttpClient

http_client = SynchronousHttpClient()
http_client.set_basic_auth('localhost', 'hey', 'peekaboo')

ari = SwaggerClient(
    "http://localhost:8088/ari/api-docs/resources.json",
    http_client=http_client)

ws = ari.events.eventWebsocket(app='hello')

for msg_str in iter(lambda: ws.recv(), None):
    msg_json = json.loads(msg_str)
    if msg_json['type'] == 'StasisStart':
        channelId = msg_json['channel']['id']
        ari.channels.answer(channelId=channelId)
        ari.channels.play(channelId=channelId,
                          media='sound:hello-world')
        ari.channels.continueInDialplan(channelId=channelId)
```

swagger-codegen
===============

There are the beginnings of a Mustache-based code generator, but it's
not functional... yet.

Data model
==========

The data model presented by the `swagger_model` module is nearly
identical to the original Swagger API resource listing and API
declaration. This means that if you add extra custom metadata to your
docs (such as a `_author` or `_copyright` field), they will carry
forward into the object model. I recommend prefixing custom fields with
an underscore, to avoid collisions with future versions of Swagger.

There are a few meaningful differences:

**Resource listing**
- The `file` and `base_dir` fields have been added, referencing the
  original `.json` file.
- The objects in a `resource_listing`'s `api` array contains a
  field `api_declaration`, which is the processed result from the
  referenced API doc.

**API declaration**
- A `file` field has been added, referencing the original `.json`
  file.

Development
-----------

The code is documented using [Sphinx](http://sphinx-doc.org/), which
allows [IntelliJ IDEA](http://confluence.jetbrains.net/display/PYH/) to do a better job at inferring types for autocompletion.

To keep things isolated, I also recommend installing (and using)
[virtualenv](http://www.virtualenv.org/).

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

[Setuptools](http://pypi.python.org/pypi/setuptools) is used for
building. [Nose](http://nose.readthedocs.org/en/latest/) is used
for unit testing, with the [coverage](http://nedbatchelder.com/code/coverage/) plugin installed to
generated code coverage reports. Pass `--with-coverage` to generate
the code coverage report. HTML versions of the reports are put in
`cover/index.html`.

```bash
$ ./setup.py develop   # prep for development (install deps, launchers, etc.)
$ python3 -m unittest discover -s swaggerpy_test -p "*_test.py" -v  # run unit tests
$ ./setup.py bdist_egg # build distributable
```

License
-------

Copyright (c) 2013, Digium, Inc. All rights reserved.

Swagger.py is licensed with a [BSD 3-Clause License](http://opensource.org/licenses/BSD-3-Clause).
