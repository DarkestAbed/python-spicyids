# spicy_ids/generate_random_strings.py

from random import sample
from string import ascii_lowercase, ascii_uppercase, digits
from typing import LiteralString

from utils import logger


def generate_random_string(length: int = 15) -> str:
    str_space: LiteralString = ascii_lowercase + ascii_uppercase + digits
    rnd_str: str = "".join(sample(population=str_space, k=length))
    logger.debug(f"{rnd_str = }")
    return rnd_str