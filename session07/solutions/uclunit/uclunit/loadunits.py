import os
import yaml
from uclunit.convert import Unit

# Import the unit definitions
def import_config():
    config_file = 'units.yaml'
    definitions = yaml.load(open(os.path.join(os.path.dirname(__file__),
        config_file)))
    return definitions

# import the unit definitions from a configuration file
definitions = import_config()

# load the units into the local namespace
for key, subkey in definitions.iteritems():
    a = {x: Unit(x,key,subkey[x]) for x in subkey.keys()}
    globals().update(a)

