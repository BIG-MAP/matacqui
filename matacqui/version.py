# pylint: disable=invalid-name

author_info = (('Eibar Flores', 'eibfl@dtu.dk'),)
version_info = (0, 1, 0)

__author__ = ", ".join("{} <{}>".format(*info) for info in author_info)
__version__ = ".".join(map(str, version_info))

__all__ = ('__version__',)
