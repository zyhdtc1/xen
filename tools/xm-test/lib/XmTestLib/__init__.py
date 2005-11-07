#
# Copyright (C) International Business Machines Corp., 2005
# Author: Dan Smith <danms@us.ibm.com>
#

from Console import *
from Test import *
from Xm import *
from XenDomain import *
from config import *

# Give this test a clean slate
destroyAllDomUs();

if os.environ.get("TEST_VERBOSE"):
    verbose = True
else:
    verbose = False


if verbose:
    timeStamp()
