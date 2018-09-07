# FME
FME related Python snippets

## Helper functions

### Convert bytestring to hex string

```python
def bytearray2str(byte_array):
    """
    Converts an FME byte array into a hex encoded
    string (e.g. used by Oracle RAW fields)
    """
    return ''.join('{:02x}'.format(x) for x in byte_array or '').upper()
```

### Force string to unicode

```python
from locale import getdefaultlocale

def str2unicode(text, encoding=None):
    """
    Converts text to unicode, if necessary.
    Encoding defaults to locale encoding.
    """
    if isinstance(text, unicode):
        return text
    else:
        return text.decode(encoding or getdefaultlocale()[1])
```
