#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Unit test specs for codetranslator.py"""
from codetranslator import Code

def test_truthy():
    """Test a truthy case"""
    assert 1 + 1 == 2

class TestCodetranslator():
    """Tests for the code translator"""
    def test_decimal2binary(self):
        c = Code("pass")
        assert (c.decimal2binary("0") == "0")
        assert (c.decimal2binary("1") == "1")
        assert (c.decimal2binary("2") == "10")
        assert (c.decimal2binary("3") == "11")
        assert (c.decimal2binary("3141") == "110001000101")

    def test_pad_binary(self):
        c = Code("pass")
        assert (c.pad_binary("1", 1) == "1")
        assert (c.pad_binary("1", 2) == "01")
        assert (c.pad_binary("1", 4) == "0001")
        assert (c.pad_binary("10", 4) == "0010")
        assert (c.pad_binary("11", 4) == "0011")
        assert (c.pad_binary("10", 8) == "00000010")
        assert (c.pad_binary("11", 8) == "00000011")

    def test_translate_a_instruction(self):
        c = Code("1")
        assert (c.translate_a_or_l_instruction() == "0000000000000001")
        c = Code("4")
        assert (c.translate_a_or_l_instruction() == "0000000000000100")
        c = Code("3141")
        assert (c.translate_a_or_l_instruction() == "0000110001000101")
        c = Code("24576")
        assert (c.translate_a_or_l_instruction() == "0110000000000000")
        c = Code("32767")
        assert (c.translate_a_or_l_instruction() == "0111111111111111")

    def test_translate_dest(self):
        c = Code("null")
        assert (c.translate_dest() == "000")
        c = Code("M")
        assert (c.translate_dest() == "001")
        c = Code("D")
        assert (c.translate_dest() == "010")
        c = Code("DM")
        assert (c.translate_dest() == "011")
        c = Code("MD")
        assert (c.translate_dest() == "011")
        c = Code("A")
        assert (c.translate_dest() == "100")
        c = Code("AM")
        assert (c.translate_dest() == "101")
        c = Code("MA")
        assert (c.translate_dest() == "101")
        c = Code("AD")
        assert (c.translate_dest() == "110")
        c = Code("DA")
        assert (c.translate_dest() == "110")
        c = Code("ADM")
        assert (c.translate_dest() == "111")
        c = Code("AMD")
        assert (c.translate_dest() == "111")
        c = Code("DAM")
        assert (c.translate_dest() == "111")
        c = Code("DMA")
        assert (c.translate_dest() == "111")
        c = Code("MAD")
        assert (c.translate_dest() == "111")
        c = Code("MDA")
        assert (c.translate_dest() == "111")

    def test_translate_jump(self):
        c = Code("null")
        assert (c.translate_jump() == "000")
        c = Code("JGT")
        assert (c.translate_jump() == "001")
        c = Code("JEQ")
        assert (c.translate_jump() == "010")
        c = Code("JLT")
        assert (c.translate_jump() == "100")
        c = Code("JNE")
        assert (c.translate_jump() == "101")
        c = Code("JLE")
        assert (c.translate_jump() == "110")
        c = Code("JMP")
        assert (c.translate_jump() == "111")

    def test_translate_comp(self):
        c = Code("0")
        assert (c.translate_comp() == "0101010")
        c = Code("1")
        assert (c.translate_comp() == "0111111")
        c = Code("-1")
        assert (c.translate_comp() == "0111010")
        c = Code("D")
        assert (c.translate_comp() == "0001100")
        c = Code("A")
        assert (c.translate_comp() == "0110000")
        c = Code("M")
        assert (c.translate_comp() == "1110000")
        c = Code("!D")
        assert (c.translate_comp() == "0001101")
        c = Code("!A")
        assert (c.translate_comp() == "0110001")
        c = Code("!M")
        assert (c.translate_comp() == "1110001")
        c = Code("D+1")
        assert (c.translate_comp() == "0011111")
        c = Code("1+D")
        assert (c.translate_comp() == "0011111")
        c = Code("A+1")
        assert (c.translate_comp() == "0110111")
        c = Code("1+A")
        assert (c.translate_comp() == "0110111")
        c = Code("M+1")
        assert (c.translate_comp() == "1110111")
        c = Code("1+M")
        assert (c.translate_comp() == "1110111")
        c = Code("D-1")
        assert (c.translate_comp() == "0001110")
        c = Code("A-1")
        assert (c.translate_comp() == "0110010")
        c = Code("M-1")
        assert (c.translate_comp() == "1110010")
        c = Code("D+A")
        assert (c.translate_comp() == "0000010")
        c = Code("A+D")
        assert (c.translate_comp() == "0000010")
        c = Code("D+M")
        assert (c.translate_comp() == "1000010")
        c = Code("M+D")
        assert (c.translate_comp() == "1000010")
        c = Code("D-A")
        assert (c.translate_comp() == "0010011")
        c = Code("D-M")
        assert (c.translate_comp() == "1010011")
        c = Code("A-D")
        assert (c.translate_comp() == "0000111")
        c = Code("M-D")
        assert (c.translate_comp() == "1000111")
        c = Code("D&A")
        assert (c.translate_comp() == "0000000")
        c = Code("A&D")
        assert (c.translate_comp() == "0000000")
        c = Code("D&M")
        assert (c.translate_comp() == "1000000")
        c = Code("M&D")
        assert (c.translate_comp() == "1000000")
        c = Code("D|A")
        assert (c.translate_comp() == "0010101")
        c = Code("A|D")
        assert (c.translate_comp() == "0010101")
        c = Code("D|M")
        assert (c.translate_comp() == "1010101")
        c = Code("M|D")
        assert (c.translate_comp() == "1010101")
