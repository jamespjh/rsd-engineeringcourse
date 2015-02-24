print('\n> Importing the library...\n')

from nose.tools import assert_raises
from uclunit.convert import Unit, NumberUnit, IncompatibleUnitsError
from uclunit.loadunits import *

# import the unit definitions from a configuration file
definitions = import_config()

# load the units into the local namespace
for key, subkey in definitions.iteritems():
    a = {x: Unit(x,key,subkey[x]) for x in subkey.keys()}
    locals().update(a)

# check the example assertions
print('\n> Checking the assertions provided in the exercise...\n')
assert(5*meters == 0.005*kilometers)
assert((60*seconds).to(minutes).value==1)
assert((60*seconds).to(minutes).unit==minutes)
with assert_raises(IncompatibleUnitsError):
    5*meters+2*seconds

# check the example assertions
print('\n> If you are reading this, the tests passed.\n')

