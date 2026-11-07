"""Sample app for the ground-truth tests. It pins vulnerable dependency
versions ON PURPOSE. Never install or deploy it.

Imports every vulnerable package but never calls the vulnerable function. It
also defines local functions named like the vulnerable ones: matching must be
by module, not by bare name.
"""
import json

import yaml
from yaml import safe_load
from PIL import Image
from cryptography.fernet import Fernet


# Local look-alikes. These are not the library functions.
def load(path):
    with open(path) as f:
        return json.load(f)


def serialize_key_and_certificates(*parts):
    return b"".join(parts)


def read_config(text):
    return yaml.safe_load(text), safe_load(text)


def thumbnail(path):
    image = Image.open(path)
    image.thumbnail((64, 64))
    return image


def new_token():
    return Fernet(Fernet.generate_key())
