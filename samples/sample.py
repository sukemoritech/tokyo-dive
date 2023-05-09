# Python Sample Code

import math
from typing import List


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)

    @classmethod
    def create_circle(cls, radius: float) -> "Circle":
        return cls(radius)

    @staticmethod
    def list_areas(circles: List["Circle"]) -> List[float]:
        return [circle.area() for circle in circles]


def main() -> None:
    circle = Circle(5)
    print(f"Circle Area: {circle.area()}")

    circles = [Circle.create_circle(i) for i in range(1, 4)]
    areas = Circle.list_areas(circles)
    print(f"Areas of circles: {areas}")


if __name__ == "__main__":
    main()
