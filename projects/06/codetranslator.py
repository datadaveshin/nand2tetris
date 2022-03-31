#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Translates symbolic code to binary code"""
from tables import DEST_TABLE, JUMP_TABLE, COMP_TABLE

class Code():
    """docstring for Code Translator."""

    def __init__(self, instruction):
        self.instruction = instruction
        self.dest = DEST_TABLE
        self.jump = JUMP_TABLE
        self.comp = COMP_TABLE

    def decimal2binary(self, dec, binary=""):
        decimal = int(dec)
        modulo = decimal % 2
        quotient = decimal // 2
        binary = str(modulo) + binary
        if quotient >= 1:
            return self.decimal2binary(quotient, binary)
        return(binary)

    def pad_binary(self, binary, digits):
        return (digits - len(binary)) * "0" + binary

    def translate_a_or_l_instruction(self):
        return self.pad_binary(self.decimal2binary(self.instruction), 16)

    def translate_dest(self):
        return self.dest[self.instruction]

    def translate_comp(self):
        return self.comp[self.instruction]

    def translate_jump(self):
        return self.jump[self.instruction]
