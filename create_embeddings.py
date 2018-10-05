#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 3 08:14:14 2018

@author: omontenegro
"""

import numpy as np
import os

file_path = "data/SBW-vectors-300-min5.txt"

vectors = {}
with open(file_path, 'rb') as f:
    for line in f:
        line_split = line.strip().split(" ")
        vec = np.array(line_split[1:], dtype=float)
        word = line_split[0]

        for char in word:
            if ord(char) < 128:
                if char in vectors:
                    vectors[char] = (vectors[char][0] + vec,
                                     vectors[char][1] + 1)
                else:
                    vectors[char] = (vec, 1)

base_name = "data/" + os.path.splitext(os.path.basename(file_path))[0] + '-char.txt'

with open(base_name, 'wb') as f2:
    for word in vectors:
        avg_vector = np.round(
            (vectors[word][0] / vectors[word][1]), 6).tolist()

        f2.write(word + " " + " ".join(str(x) for x in avg_vector) + "\n")