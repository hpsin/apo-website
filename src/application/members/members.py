"""This module contains methods related to user profiles
and permissions.

It utilizes the methods found in the accounts package.

.. module:: application.members.members

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

import urllib, hashlib

from models import FamilyModel

def get_avatar_url(email, size=100, default='/static/img/avatar.png'):
    """
    This function takes a Gravatar email address
    and returns the gravatar image url

    :param email: The Gravatar email address
    :type email: unicode

    :param size: Size of the returned avatar image
    :type size: int

    :param default: Default avatar url
    :type default: unicode
    """

    gravatar_url = "http://www.gravatar.com/avatar/"
    gravatar_url += hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

    return gravatar_url

def get_family_names():
    """
    Returns the list of family names in the database
    """

    query = FamilyModel.all()

    count = query.count()

    results = query.fetch(count)

    names = []
    for family in results:
        names.append(family.name)

    names.sort()

    return names
    