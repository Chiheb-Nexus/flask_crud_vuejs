#
# Project config
#


class BaseConfig(object):
    DEBUG = True


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    DEBUG = False


CURRENT_CONFIG = DevConfig
