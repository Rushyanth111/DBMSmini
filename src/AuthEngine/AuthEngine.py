"""Authrization Module

"""

import hashlib


def authorize(username, password) -> bool:
    return username == "root" and password == ""


def register(username, password) -> bool:
    pass


def __hash__(password):
    pass


def __compare_hash__(password):
    pass


def __obtain_hash__(username):
    pass
