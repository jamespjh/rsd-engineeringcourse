'''
Convert between different units
'''

import yaml
import os

class IncompatibleUnitsError(Exception):
    pass

# Import the unit definitions
def import_config():
    config_file = 'units.yaml'
    definitions = yaml.load(open(os.path.join(os.path.dirname(__file__),
        config_file)))
    return definitions

# Create a class for the defined units
# Operator overloading on __rmul__
class Unit(object):
    pass


class NumberUnit(object):
    pass





