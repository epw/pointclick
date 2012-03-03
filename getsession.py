#! /usr/bin/env python

"""Handle simple sessions stored as pickle objects in a directory, indexed
by arbituary IDs (usually timestamps)"""

import pickle, os

session_path = "sessions/"
EXN = ".pkl"

def get (session):
    """Return object stored with session, or empty dict if none found."""

    if os.path.exists (session_path + session + EXN):
        with open (session_path + session + EXN) as f:
            return pickle.load (f)
    return {}

def put (session, obj):
    """Store object with session ID, overwriting previous if any."""

    with open (session_path + session + EXN, "w") as f:
        pickle.dump (obj, f)
