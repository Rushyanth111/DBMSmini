"""Authrization Module

"""


def authorize(username, password) -> bool:
    print(username, password)
    return username == "root" and password == ""
