# Created by lcg at 30.11.22
import math
from pathlib import Path
from typing import List


def assert_file_exists(path: str):
    """ Checks if file exists.

    :param path: file path
    :return: None
    :exception: FileNotFoundError
    """
    if not Path(path).is_file():
        raise FileNotFoundError(f'File {path} not found.')


def args2lists(length: int, *args) -> List[List]:
    """ Converts each parameter into a list of given length, parameter values
    are repeated if required.

    :param length: target lengths of created lists
    :param args: parameters to convert
    :return: list of converted parameters
    """
    args_lsts = []
    for arg in args:
        args_lsts.append(arg2list(length, arg))
    return args_lsts


def arg2list(length: int, arg) -> List:
    """ Converts parameter into a list of given length, parameter values
    are repeated if required.

    :param length: target length of list
    :param arg: parameter
    :return: list
    """
    if not isinstance(arg, list):
        arg = [arg]
    arg = arg*math.ceil(length/len(arg))
    return arg[:length]
