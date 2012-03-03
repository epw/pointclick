#! /usr/bin/env python

# This module contains the actual logic to be used in the game.
# This is the main file to alter

# For most games, simple if..elif chains involving the "found" image
# are likely to be all that is necessary.

import os, getsession

def process (src, found, session, x, y):
    """This function figures out what image should be displayed next,
    due to a click on a displayed image.

    src - The filename of the image that was clicked
    found - The filename of the mask which matches the coordinates
    clicked
    session - The session ID of the user
    x - The X coordinate of the click
    y - The Y coordinate of the click

    It should return a string containing the relative path to the new
    image to load."""

    params = getsession.get (session)

    getsession.put (session, params)

    return "spherecube.png"

def process_special (src, data, session, x, y):
    """This function figures out what image should be displayed next,
    due to some other message being sent.

    src - The filename of the image that was clicked
    data - Arbitrary data (string)
    session - The session ID of the user
    x - The X coordinate of the click, if any
    y - The Y coordinate of the click, if any

    It should return a string containing the relative path to the new
    image to load."""

    params = getsession.get (session)

    getsession.put (session, params)

    return "spherecube%s.png" % data
