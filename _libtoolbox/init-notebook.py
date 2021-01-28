#!/bin/env python3

from ipywidgets import interactive_output
import ipywidgets as widgets

import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import root_scalar

import sys
sys.path.append(['_libtoolbox', '../_libtoolbox', '../../_libtoolbox'])
import gas