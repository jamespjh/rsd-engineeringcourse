'''
Convert between different units
'''

# Define our custom error 
class IncompatibleUnitsError(Exception):
    pass

# Base unit
class Unit(object):
    def __init__(self, unit, unit_type, rel_value):
        self.unit = unit
        self.unit_type = unit_type
        self.rel_value = rel_value
    # Define magic functions to give person-friendly description
    def __repr__(self):
        return 'Unit(' + self.unit + ')'
    def __str__(self):
        return 'Unit(' + self.unit + ')'
    # Create NumberUnit when Unit is multiplied by numerical value
    def __rmul__(self, other):
        return NumberUnit(self, other)

# Number combined with a base unit
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
    # Define how the equality operator is used for NumberUnits
    def __eq__(self, other):
        if type(other) == NumberUnit:
            unit_type_match = self.unit_type == other.unit_type
            value_match = self.value * self.rel_value == \
                other.value * other.rel_value
            return unit_type_match and value_match
        else:
            raise IncompatibleUnitsError('Incompatible units')
    # Define how NumberUnits are summed
    def __add__(self, other):
        if self.unit_type != other.unit_type:
            raise IncompatibleUnitsError('Incompatible units')
        else:
            convertor = float(other.rel_value) / self.rel_value
            new_value = self.value + (other.value * convertor)
            return NumberUnit(self.unit,new_value)
    # Define how NumberUnits are subtracted
    def __sub__(self, other):
        if self.unit_type != other.unit_type:
            raise IncompatibleUnitsError('Incompatible units')
        else:
            convertor = float(other.rel_value) / self.rel_value
            new_value = self.value - (other.value * convertor)
            return NumberUnit(self.unit,new_value)
    # Create a method for converting between units
    def to(self,other):
        if self.unit_type != other.unit_type:
            raise IncompatibleUnitsError('Incompatible units')
        else: 
            convertor = float(self.rel_value) / other.rel_value
            new_value = self.value * convertor
            return NumberUnit(other,new_value)

