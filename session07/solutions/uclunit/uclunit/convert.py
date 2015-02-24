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

# Class for the base units
# Operator overloading on __rmul__
class Unit(object):
    def __init__(self, unit, unit_type, rel_value):
        self.unit = unit
        self.unit_type = unit_type
        self.rel_value = rel_value
    def __repr__(self):
        return 'Unit(' + self.unit + ')'
    def __str__(self):
        return 'Unit(' + self.unit + ')'
    def __rmul__(self, other):
        return NumberUnit(self, other)

# Class for a number combined with a Unit
class NumberUnit(object):
    def __init__(self, unit, numval):
        self.unit = unit
        self.unit_type = unit.unit_type
        self.rel_value = unit.rel_value
        self.value = numval
    def __repr__(self):
        return 'NumberUnit(' + str(self.value) + '*' \
            + self.unit.unit + ')'
    def __str__(self):
        return 'NumberUnit(' + str(self.value) + '*' \
            + self.unit.unit + ')'
    def __eq__(self, other):
        if type(other) == NumberUnit:
            unit_type_match = self.unit_type == other.unit_type
            value_match = self.value * self.rel_value == \
                other.value * other.rel_value
            return unit_type_match and value_match
        else:
            raise IncompatibleUnitsError('Incompatible units')
    def __add__(self, other):
        if self.unit_type != other.unit_type:
            raise IncompatibleUnitsError('Incompatible units')
        else:
            convertor = float(self.rel_value) / other.rel_value
            new_value = (self.value + other.value) * convertor
            return NumberUnit(self.unit,new_value)
    def to(self,other):
        if self.unit_type != other.unit_type:
            raise IncompatibleUnitsError('Incompatible units')
        else: 
            convertor = float(self.rel_value) / other.rel_value
            new_value = self.value * convertor
            return NumberUnit(other,new_value)

