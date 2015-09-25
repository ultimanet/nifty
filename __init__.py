## NIFTY (Numerical Information Field Theory) has been developed at the
## Max-Planck-Institute for Astrophysics.
##
## Copyright (C) 2013 Max-Planck-Society
##
## Author: Marco Selig
## Project homepage: <http://www.mpa-garching.mpg.de/ift/nifty/>
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import division

import matplotlib as mpl
mpl.use('Agg')

import dummys

from keepers import about,\
                  global_dependency_injector,\
                  global_configuration



from nifty_cmaps import ncmap
from nifty_core import space,\
                    point_space,\
                    field

from nifty_mpi_data import distributed_data_object, d2o_librarian
from nifty_random import random
from nifty_simple_math import *
from nifty_utilities import *

from nifty_paradict import space_paradict,\
                            point_space_paradict,\
                            nested_space_paradict
from operators import *

## optional submodule `rg`
try:
    from rg import rg_space,\
                    power_backward_conversion_rg,\
                    power_forward_conversion_rg
    from nifty_paradict import rg_space_paradict
except(ImportError):
    pass

## optional submodule `lm`
try:
    from lm import lm_space,\
                    power_backward_conversion_lm,\
                    power_forward_conversion_lm
    from nifty_paradict import lm_space_paradict

    try:
        from lm import gl_space
        from nifty_paradict import gl_space_paradict
    except(ImportError):
        pass

    try:
        from lm import hp_space
        from nifty_paradict import hp_space_paradict
    except(ImportError):
        pass

except(ImportError):
    pass

from demos import get_demo_dir
from pickling import _pickle_method, _unpickle_method

#import pyximport; pyximport.install(pyimport = True)

