#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Unit test specs for hackparser.py"""
from hackparser import Parser


def test_truthy():
    """Test a truthy case"""
    assert 1 + 1 == 2

class TestParser:
    """Tests for the hackparser"""
    def test_remove_leading_trailing_white_space(self):
        parser = Parser("  hello  ")
        parser.remove_leading_trailing_white_space()
        assert parser.instruction == "hello"

        parser = Parser("  hello world ")
        parser.remove_leading_trailing_white_space()
        assert parser.instruction == "hello world"

    def test_instruction_is_command(self):
        parser = Parser("@R1")
        assert parser.instruction_is_command()

        parser = Parser("D=A+M")
        assert parser.instruction_is_command()

        parser = Parser("(LOOP)")
        assert parser.instruction_is_command()

        parser = Parser("(LOOP) // Comment")
        assert parser.instruction_is_command()

        parser = Parser("// Comment")
        assert not parser.instruction_is_command()

        parser = Parser("")
        assert not parser.instruction_is_command()

    def test_get_instruction(self):
        parser = Parser("@R1")
        parser.get_instruction()
        assert parser.instruction == "@R1"

        parser = Parser(" D=A+M ")
        parser.get_instruction()
        assert parser.instruction == "D=A+M"

        parser = Parser(" D=A+M // Comment")
        parser.get_instruction()
        assert parser.instruction == "D=A+M"

    def test_set_instruction_type(self):
        parser = Parser("@R1")
        parser.set_instruction_type()
        assert parser.instruction_type == "A_INSTRUCTION"

        parser = Parser("(LOOP)")
        parser.set_instruction_type()
        assert parser.instruction_type == "L_INSTRUCTION"

        parser = Parser("M=D+1")
        parser.set_instruction_type()
        assert parser.instruction_type == "C_INSTRUCTION"

        parser = Parser("D+1;JLT")
        parser.set_instruction_type()
        assert parser.instruction_type == "C_INSTRUCTION"

    def test_get_a_symbol(self):
        parser = Parser("@R1")
        assert parser.get_a_symbol() == "R1"

    def test_get_l_symbol(self):
        parser = Parser("(LOOP)")
        assert parser.get_l_symbol() == "LOOP"

    def test_get_dest(self):
        parser = Parser("M=D")
        assert parser.get_dest() == "M"

        parser = Parser("M=D+1")
        assert parser.get_dest() == "M"

        parser = Parser("M=D+1;JLT")
        assert parser.get_dest() == "M"

    def test_get_comp(self):
        parser = Parser("M=D")
        assert parser.get_comp() == "D"

        parser = Parser("M=D+1")
        assert parser.get_comp() == "D+1"

        parser = Parser("D;JLT")
        assert parser.get_comp() == "D"

        parser = Parser("D+1;JLT")
        assert parser.get_comp() == "D+1"

    def test_get_jump(self):
        parser = Parser("0;JEQ")
        assert parser.get_jump() == "JEQ"

        parser = Parser("D;JEQ")
        assert parser.get_jump() == "JEQ"

        parser = Parser("D;JLE")
        assert parser.get_jump() == "JLE"

        parser = Parser("D;JLE")
        assert parser.get_jump() == "JLE"
