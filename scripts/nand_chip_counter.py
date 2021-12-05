#!/usr/bin/env python3
"""Nand Chip Consumption Calculator"""
import os
from queue import Queue

class Chip():
    """Creates a chip object that stores the chip name, parts, number of nand gates"""

    def __init__(self, path, parts):
        self.path = path
        self.name = path.split('/')[-1].split('.')[0]
        self.parts = parts
        self.num_nand_gates = 0

    def __str__(self):
        ret_str = f"Chip: {self.name}\n"
        for part, count in self.parts.items():
            ret_str += f"Part {part:9} count: {count:1}\n"
        ret_str += f"Number of Nand gates: {self.num_nand_gates}\n"
        return ret_str


def get_filenames():
    """Returns a list of chip names from .hdl files from project directory"""
    file_list = []
    for dirpath, _dirs, files in os.walk("../projects/"):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            if fname.split('.')[-1] == "hdl":
                file_list.append(fname)
    return file_list

def get_parts(fname : str):
    """Returns a dict that contains the parts within a chip .hdl file"""
    parts_dict = {}
    with open(fname, 'r', encoding="utf8") as lines:
        parts_start = False
        for line in lines:
            line = line.strip()
            if line == 'PARTS:':
                parts_start = True
            if line == '}':
                break
            if parts_start and line != 'PARTS:' and line != "}" and line != "":
                part = line.split("(")[0].split()[0]
                if part in parts_dict:
                    parts_dict[part] += 1
                elif part == "//":
                    pass
                else:
                    parts_dict[part] = 1
    return parts_dict

def calculate_nand_chips(chip, nand_gates_per_chip):
    """Returns the total number of nand chips a Chip object would consume"""
    total_nand_chips = 0
    for part_name, part_count in chip.parts.items():
        total_nand_chips += nand_gates_per_chip[part_name] * part_count
    return total_nand_chips

def main():
    """Outputs chip names, parts and number of nand gates used in projects directory"""
    nands_per_chip = {'Nand': 1, 'DFF': 2}
    filenames = get_filenames()
    uncompleted_chips = []
    completed_chips = []
    for name in filenames:
        parts = get_parts(name)
        chip = Chip(name, parts)
        if "//" in chip.parts:
            uncompleted_chips.append(chip)
        else:
            completed_chips.append(chip)

    frontier = Queue(maxsize = 50)
    for chip in completed_chips:
        frontier.put(chip)

    chips_with_nand_count = []
    while not frontier.empty():
        current_chip = frontier.get()
        all_parts_present = True
        for part in current_chip.parts:
            if part not in nands_per_chip:
                all_parts_present = False
        if all_parts_present:
            current_chip.num_nand_gates = calculate_nand_chips(current_chip, nands_per_chip)
            nands_per_chip[current_chip.name] = current_chip.num_nand_gates
            chips_with_nand_count.append(current_chip)
        else:
            frontier.put(current_chip)

    for chip in uncompleted_chips:
        print(chip)

    for chip in chips_with_nand_count:
        print(chip)

if __name__ == '__main__':
    main()
