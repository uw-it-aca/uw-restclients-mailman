# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

"""
Interface for interacting with the mailman uwnetid resource
"""

import json
from commonconf import settings
from uw_mailman import get_resource


URL = "/{key}/admin/v1.0/uwnetid/available/?uwnetid={uwnetid}"
MAILMAN_ADMIN_URL = "https://mailman.u.washington.edu/mailman/admin/{}"


def _get_url_path(list_name):
    """
    Live Dao requires RESTCLIENTS_MAILMAN_KEY in the settings.py
    """
    access_key = getattr(settings,
                         "RESTCLIENTS_MAILMAN_KEY",
                         "__mock_key__")
    return URL.format(key=access_key, uwnetid=list_name)


def exists(list_name):
    """
    Return True if the corresponding mailman list is avaliable
    for the given list name string
    @param list_name: a non_empty string
    """
    return _process_json(get_resource(_get_url_path(list_name)))


def _process_json(response_body):
    """
    Returns True the list already exists
    """
    data = json.loads(response_body)
    return "Available" in data and data["Available"] == "False"


def get_admin_url(list_name):
    return MAILMAN_ADMIN_URL.format(list_name)
