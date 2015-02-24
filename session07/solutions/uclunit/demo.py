print('\n> Importing the library...\n')

from nose.tools import assert_raises
from uclunit.convert import Unit, NumberUnit, IncompatibleUnitsError
from uclunit.loadunits import *

# check the example assertions
print('\n> Checking the assertions provided in the exercise...\n')
assert(5*meters == 0.005*kilometers)
assert((60*seconds).to(minutes).value==1)
assert((60*seconds).to(minutes).unit==minutes)
with assert_raises(IncompatibleUnitsError):
    5*meters+2*seconds

# check the example assertions
print('\n> If you are reading this, the tests passed.\n')

