"""
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
"""


from csv import DictReader
from math import sqrt

from typing import List, Optional


class Dinosaur:
    def __init__(
        self,
        name: str,
        leg_length: float,
        stance: Optional[str] = None,
        stride_length: float = 0,
    ):
        self.name = name
        self.leg_length = leg_length
        self.stance = stance
        self.stride_length = stride_length
        self.speed = ((self.stride_length / self.leg_length) - 1) * sqrt(
            self.leg_length * 9.8
        )

    def __str__(self):
        return f"Dinosaur(name: {self.name}, leg_length: {self.leg_length}, stride_length: {self.stride_length}, stance: {self.stance})"


def parse_dinosaurs(
    files: List[str] = ["dataset1.csv", "dataset2.csv"]
) -> List[Dinosaur]:
    dinos: List[Dinosaur] = list()

    with open(files[0], "r") as reader1:
        r = DictReader(reader1)
        for row in r:
            dinos.append(
                Dinosaur(name=row["NAME"], leg_length=float(row["LEG_LENGTH"]))
            )

    with open(files[1], "r") as reader2:
        r = DictReader(reader2)
        for row in r:
            for d in dinos:
                if d.name == row["NAME"]:
                    d.stride_length = float(row["STRIDE_LENGTH"])
                    d.stance = row["STANCE"]

    return dinos


if __name__ == "__main__":
    dinos = parse_dinosaurs()
    dinos.sort(key=lambda dino: dino.speed)

    for i in dinos:
        if i.stance == "bipedal":
            print(i.name)
