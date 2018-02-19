import ConfigParser


class LPMConfigParser(ConfigParser.SafeConfigParser):
    """ Defines the custom extension from `ConfigParser.SafeConfigParser` used by `lpm`

    TODO: Export the current configuration as a YAML object
    """

    def find_config_parser(self):
        pass

