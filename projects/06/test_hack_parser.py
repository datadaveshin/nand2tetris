#!/usr/bin/env python3
"""Unit test specs for hackparser.py"""
import os
import filecmp
from hackparser import Parser


def test_truthy():
    """Test a truthy case"""
    assert 1 + 1 == 2

class TestParser:
    """Tests for the hackparser"""
    def test_remove_leading_trailing_white_space(self):
        p = Parser("  hello  ")
        p.remove_leading_trailing_white_space()
        assert (p.instruction == "hello")

        p = Parser("  hello world ")
        p.remove_leading_trailing_white_space()
        assert (p.instruction == "hello world")

    def test_instruction_is_command(self):
        p = Parser("@R1")
        assert (p.instruction_is_command() is True)

        p = Parser("D=A+M")
        assert (p.instruction_is_command() is True)

        p = Parser("(LOOP)")
        assert (p.instruction_is_command() is True)

        p = Parser("(LOOP) // Comment")
        assert (p.instruction_is_command() is True)

        p = Parser("// Comment")
        assert (p.instruction_is_command() is False)

        p = Parser("")
        assert (p.instruction_is_command() is False)

    def test_get_instruction(self):
        p = Parser("@R1")
        p.get_instruction()
        assert (p.instruction == "@R1")

        p = Parser(" D=A+M ")
        p.get_instruction()
        assert (p.instruction == "D=A+M")

        p = Parser(" D=A+M // Comment")
        p.get_instruction()
        assert (p.instruction == "D=A+M")

    def test_get_a_symbol(self):
        p = Parser("@R1")
        assert (p.get_a_symbol() == "R1")

    def test_get_l_symbol(self):
        p = Parser("(LOOP)")
        assert (p.get_l_symbol() == "LOOP")

    def test_get_dest(self):
        p = Parser("M=D")
        assert (p.get_dest() == "M")

        p = Parser("M=D+1")
        assert (p.get_dest() == "M")

        p = Parser("M=D+1;JLT")
        assert (p.get_dest() == "M")

    def test_get_comp(self):
        p = Parser("M=D")
        assert (p.get_comp() == "D")

        p = Parser("M=D+1")
        assert (p.get_comp() == "D+1")

        p = Parser("D;JLT")
        assert (p.get_comp() == "D")

        p = Parser("D+1;JLT")
        assert (p.get_comp() == "D+1")
