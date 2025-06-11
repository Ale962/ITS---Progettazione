from typing import Self

class IntGZ(int):
	def __new__(cls, v:int|float|Self)->Self:
		if v <= 0:
			raise ValueError(f"Value v == {v} must be >= 0")
		return int.__new__(cls, v)