import base64
import xml.dom.minidom
import zlib

from xml.parsers.expat import ExpatError


def repr_saml(saml_str, b64=False):
    """ Decode SAML from b64 and b64 deflated and
        return a pretty printed representation
    """
    try:
        msg = base64.b64decode(saml_str).decode() if b64 else saml_str
        dom = xml.dom.minidom.parseString(msg)
    except (UnicodeDecodeError, ExpatError):
        # in HTTP-REDIRECT the base64 must be inflated
        msg = base64.b64decode(saml_str)
        inflated = zlib.decompress(msg, 0)
        dom = xml.dom.minidom.parseString(inflated.decode())
    return dom.toprettyxml()


def encode_saml(saml_envelope, use_zlib=False):
    before_base64 = zlib.compress(saml_envelope.encode()) if use_zlib else saml_envelope.encode()
    return base64.b64encode(before_base64)

