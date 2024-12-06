%pip install jupyterlab-lsp colorama python-dotenv ipykernel

from __future__ import annotations
from dataclasses import asdict, dataclass, field
from enum import Enum, auto
from functools import cache, reduce
from itertools import permutations, combinations, count, cycle
from collections import Counter, deque, defaultdict
import heapq
import copy
import operator
import logging
import time
import os
import re
import ast
import unittest
import requests
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.markers import MarkerStyle
from matplotlib import path as pltpath
import numpy as np
import networkx as nx
import pandas as pd
from tqdm.notebook import tqdm
from dotenv import load_dotenv
from pathlib import Path
from getpass import getpass
from colorama import Fore, Back, Style
from IPython.display import display
from IPython.core.display import Markdown

##########################################################################
# SETUP LOGGING
#
# Create a new instance of "logger" in the client application
# Set to your preferred logging level
# And add the stream_handler from this module, if you want coloured output
##########################################################################

# logger for aoc_commons only
logger = logging.getLogger(__name__) # aoc_common.aoc_commons
logger.setLevel(logging.INFO)
stream_handler = None

class ColouredFormatter(logging.Formatter):
    """ Custom Formater which adds colour to output, based on logging level """

    level_mapping = {"DEBUG": (Fore.BLUE, "DBG"),
                     "INFO": (Fore.GREEN, "INF"),
                     "WARNING": (Fore.YELLOW, "WRN"),
                     "ERROR": (Fore.RED, "ERR"),
                     "CRITICAL": (Fore.MAGENTA, "CRT")
    }

    def __init__(self, *args, apply_colour=True, shorten_lvl=True, **kwargs) -> None:
        """ Args:
            apply_colour (bool, optional): Apply colouring to messages. Defaults to True.
            shorten_lvl (bool, optional): Shorten level names to 3 chars. Defaults to True.
        """
        super().__init__(*args, **kwargs)
        self._apply_colour = apply_colour
        self._shorten_lvl = shorten_lvl

    def format(self, record):
        if record.levelname in ColouredFormatter.level_mapping:
            new_rec = copy.copy(record)
            colour, new_level = ColouredFormatter.level_mapping[record.levelname]

            if self._shorten_lvl:
                new_rec.levelname = new_level

            if self._apply_colour:
                msg = colour + super().format(new_rec) + Fore.RESET
            else:
                msg = super().format(new_rec)

            return msg

            # If our logging message is not using one of these levels...
        return super().format(record)

        if not stream_handler:
            stream_handler = logging.StreamHandler()
            stream_fmt = ColouredFormatter(fmt='%(asctime)s.%(msecs)03d:%(name)s - %(levelname)s: %(message)s',
                                           datefmt='%H:%M:%S')
            stream_handler.setFormatter(stream_fmt)

        if not logger.handlers:
            # Add our ColouredFormatter as the default console logging
            logger.addHandler(stream_handler)

        def retrieve_console_logger(script_name):
            """ Create and return a new logger, named after the script
            So, in your calling code, add a line like this:
            logger = ac.retrieve_console_logger(locations.script_name)
            """
            a_logger = logging.getLogger(script_name)
            a_logger.addHandler(stream_handler)
            a_logger.propagate = False
            return a_logger

        def setup_file_logging(a_logger: logging.Logger, folder: str | Path = ""):
            """ Add a FileHandler to the specified logger. File name is based on the logger name.
            In calling code, we can add a line like this:
            td.setup_file_logging(logger, locations.output_dir)

            Args:
                a_logger (Logger): The existing logger
                folder (str): Where the log file will be created. Will be created if it doesn't exist
            """
            Path(folder).mkdir(parents=True, exist_ok=True)  # Create directory if it does not exist
            file_handler = logging.FileHandler(Path(folder, a_logger.name + ".log"), mode='w')
            file_fmt = logging.Formatter(fmt="%(asctime)s.%(msecs)03d:%(name)s:%(levelname)8s: %(message)s",
                                         datefmt='%H:%M:%S')
            file_handler.setFormatter(file_fmt)
            a_logger.addHandler(file_handler)


def top_and_tail(data, block_size=5, include_line_numbers=True, zero_indexed=False):
    """ Print a summary of a large amount of data

    Args:
        data (_type_): The data to present in summary form.
        block_size (int, optional): How many rows to include in the top, and in the tail.
        include_line_numbers (bool, optional): Prefix with line number. Defaults to True.
        zero_indexed (bool, optional): Lines start at 0? Defaults to False.
    """
    if isinstance(data, list):
        # Get the number of digits of the last item for proper alignment
        num_digits_last_item = len(str(len(data)))

        # Format the string with line number
        def format_with_line_number(idx, line):
            start = 0 if zero_indexed else 1
            if include_line_numbers:
                return f"{idx + start:>{num_digits_last_item}}: {line}"
            else:
                return line

        start = 0 if zero_indexed else 1
        if len(data) < 11:
            return "\n".join(format_with_line_number(i, line) for i, line in enumerate(data))
        else:
            top = [format_with_line_number(i, line) for i, line in enumerate(data[:block_size])]
            tail = [format_with_line_number(i, line) for i, line in enumerate(data[-block_size:], start=len(data)-block_size)]
            return "\n".join(top + ["..."] + tail)
    else:
        return data



