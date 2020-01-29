#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Atbash is a simple substitution cipher originally for the Hebrew alphabet,
#  but possible with any known alphabet.
#  ```
#   Original:   abcdefghijklmnopqrstuvwxyz
#   Substitute: ZYXWVUTSRQPONMLKJIHGFEDCBA
#  ```
#
#  So you would substitute "a" in your input text with "Z" in your output text,
#  "b" with "Y", "c" with "X" and so forth.
#
#  A few English words also 'Atbash' into other English words: "irk"="rip",
#  "low"="old", "hob"="sly", "hold"="slow", "holy"="slob", "horn"="slim",
#  "glow"="told", "grog"="tilt" and "zoo"="all". Some other English words
#  Atbash into their own reverses, e.g., "wizard" = "draziw."
#
#  (https://en.wikipedia.org/wiki/Atbash)

original = 'abcdefghijklmnopqrstuvwxyz '
substitute = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '.lower()
mapping = {}
for k, v in zip(original, substitute):
    mapping[k] = v


def encode(s):
    """ Encodes the string """
    return "".join([mapping[l] for l in s])


def decode(s):
    """ Since the cypher is symmetric, use the same mapping to decode """
    return "".join([mapping[l] for l in s])
