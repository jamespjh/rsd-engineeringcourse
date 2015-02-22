from nose.tools import assert_raises, assert_equal, assert_true, assert_false
from nose import with_setup
from uclunit.convert import Unit, NumberUnit, IncompatibleUnitsError
import yaml

# First test suggested in the exercise
def test_5meters_equals_0005_kilometers():
    meters = Unit('meters', 'length', 1.)
    kilometers = Unit('kilometers', 'length', 1000.)
    assert(5*meters == 0.005*kilometers)

# Second test suggested in the exercise
def test_60seconds_equals_1minute():
    seconds = Unit('seconds', 'time', 1.)
    minutes = Unit('minutes', 'time', 60.)
    assert((60*seconds).to(minutes).value==1.0)

# Third test suggested in the exercise
def test_seconds_convert_to_minutes():
    seconds = Unit('seconds', 'time', 1.)
    minutes = Unit('minutes', 'time', 60.)   
    assert((60*seconds).to(minutes).unit==minutes) 

# Fourth test suggested in the exercise
def test_incompatible_unit_multiplication():
    meters = Unit('meters', 'length', 1.)
    seconds = Unit('seconds', 'time', 1.)
    with assert_raises(IncompatibleUnitsError):
        5*meters+2*seconds

# Additional test


