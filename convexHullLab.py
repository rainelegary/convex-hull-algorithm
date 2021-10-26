from dataclasses import dataclass

@dataclass
class HullSettings:
	dimensions: int = 3
	numPoints: int = 1000

