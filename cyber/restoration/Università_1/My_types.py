from typing import Self
from enum import *

# Specialised domain 18..31
# - immutable

class Voto(int):
	def __new__(cls, v:int|Self)->Self:
		if v < 18 or v > 30:
			raise ValueError(f"Value v == {v} must be between 18 and 30")
		return int.__new__(cls, v)