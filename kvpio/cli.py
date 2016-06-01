

import os
import click
import kvpio


VERBOSE = False


@click.group()
@click.option('--api-key', help='the kvp.io api key to use')
@click.option('--verbose', help='turn on detailed output', is_flag=True)
def cli(api_key, verbose):
    """
    kvpio v0.1.5

    usage:

        kvpio account

        kvpio bucket    list|get|set|del

        kvpio template  list|get|set|del
    """
    global VERBOSE

    if not api_key:
        api_key = os.environ.get('KVPIO_APIKEY', None)
    if not api_key:
        if os.path.exists('~/.kvpio'):
            with open('~/.kvpio', 'r') as f:
                api_key = f.read()
    if not api_key:
        print(
            '\n' +
            'WARNING: No api key was provided. This means only READ \n' +
            'operations will be permitted on PUBLIC endpoints. You can \n' +
            'set an API key via the following:\n' +
            '    with the command line option --api-key\n'+
            '    as an environment variable named KVPIO_APIKEY\n' +
            '    as a single line in the file ~/.kvpio\n'
        )
    kvpio.api_key = api_key
    VERBOSE = verbose

#
# bucket commands
#
@cli.command('account')
def account():
    """
    Get account information.
    """
    if not kvpio.api_key:
        click.echo('Please provide an API key.')
    click.echo(
        kvpio.Account().get()
    )

#
# bucket commands
#
@cli.group('bucket')
def bucket():
    """
    Interact with key/value pairs.
    """

@bucket.command('list')
def bucket_list():
    """
    Retrieve a list of keys.
    """
    click.echo(
        kvpio.Bucket().list()
    )

@bucket.command('get')
@click.argument('key')
def bucket_get(key):
    """
    Retrieve the value stored at KEY.

    KEY may be a single word or a path of the form path/to/key to access
    nested values.
    """
    click.echo(
        kvpio.Bucket().get(key)
    )

@bucket.command('set')
@click.argument('key')
@click.argument('value')
def bucket_set(key, value):
    """
    Set KEY to the specified VALUE.

    KEY may be a single word or a path of the form path/to/key to set
    nested values.
    """
    try:
        value = json.loads(value)
    except:
        pass
    kvpio.Bucket().set(key, value)

@bucket.command('del')
@click.argument('key')
def bucket_del(key):
    """
    delete KEY and it's value

    KEY may be a single word or a path of the form path/to/key to delete.
    KEY and all keys and values nested below it will be deleted.
    """
    kvpio.Bucket().delete(key)

#
# template comands
#
@cli.group('template')
def template():
    """
    Interact with templates.
    """

@template.command('list')
def template_list():
    """
    Retrieve a list templates.
    """
    click.echo(
        kvpio.Templates().list()
    )

@template.command('get')
@click.argument('name')
@click.option('--values', help='A dictionary, as a JSON string.')
@click.option('--raw', is_flag=True, help='Return the template un-rendered.')
def template_get(name, values, raw):
    """
    Retrieve and render the template at NAME

    Values for the template are retrieved from your bucket based on variable
    names found in template.

    If the --values option specifics a valid JSON dictionary, it's values
    will override those found in the bucket. This is useful for rendering
    templates with non-persistent, one-time values.

    If the --raw flag is specified, the original, unrendered template is
    returned.
    """
    try:
        values = json.loads(values)
    except:
        values = {}

    if raw:
        click.echo(
            kvpio.Templates().get(name, raw=raw)
        )
    else:
        click.echo(
            kvpio.Templates().get(name, data=values)
        )

@template.command('set')
@click.argument('name')
@click.argument('value')
def template_set(name, value):
    """
    Set NAME to the specified template VALUE.

    VALUE must be a string utilizing the Jinja2 template language.
    """
    kvpio.Templates().set(name, value)

@template.command('del')
@click.argument('name')
def template_del(name):
    """
    Delete NAME and it's template.
    """
    kvpio.Templates().delete(name)
