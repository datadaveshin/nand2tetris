#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Unit test specs for codetranslator.py"""
from codetranslator1 import Code

def test_truthy():
    """Test a truthy case"""
    assert 1 + 1 == 2

class TestDecimalToBinaryMethods():
    """Tests for the code translator"""
    def test_decimal2binary(self):
        code = Code("pass")
        assert code.decimal2binary("0") == "0"
        assert code.decimal2binary("1") == "1"
        assert code.decimal2binary("2") == "10"
        assert code.decimal2binary("3") == "11"
        assert code.decimal2binary("3141") == "110001000101"

    def test_pad_binary(self):
        code = Code("pass")
        assert code.pad_binary("") == "0000000000000000"
        assert code.pad_binary("0") == "0000000000000000"
        assert code.pad_binary("1") == "0000000000000001"
        assert code.pad_binary("10") == "0000000000000010"
        assert code.pad_binary("111111111111111") == "0111111111111111"
        assert code.pad_binary("1111111111111111") == "1111111111111111"

class TestCodeTranslators():
    def test_translate_a_instruction(self):
        code = Code("1")
        assert code.translate_a_or_l_instruction() == "0000000000000001"
        code = Code("4")
        assert code.translate_a_or_l_instruction() == "0000000000000100"
        code = Code("3141")
        assert code.translate_a_or_l_instruction() == "0000110001000101"
        code = Code("24576")
        assert code.translate_a_or_l_instruction() == "0110000000000000"
        code = Code("32767")
        assert code.translate_a_or_l_instruction() == "0111111111111111"

    def test_translate_dest(self):
        code = Code("null")
        assert code.translate_dest() == "000"
        code = Code("M")
        assert code.translate_dest() == "001"
        code = Code("D")
        assert code.translate_dest() == "010"
        code = Code("DM")
        assert code.translate_dest() == "011"
        code = Code("MD")
        assert code.translate_dest() == "011"
        code = Code("A")
        assert code.translate_dest() == "100"
        code = Code("AM")
        assert code.translate_dest() == "101"
        code = Code("MA")
        assert code.translate_dest() == "101"
        code = Code("AD")
        assert code.translate_dest() == "110"
        code = Code("DA")
        assert code.translate_dest() == "110"
        code = Code("ADM")
        assert code.translate_dest() == "111"
        code = Code("AMD")
        assert code.translate_dest() == "111"
        code = Code("DAM")
        assert code.translate_dest() == "111"
        code = Code("DMA")
        assert code.translate_dest() == "111"
        code = Code("MAD")
        assert code.translate_dest() == "111"
        code = Code("MDA")
        assert code.translate_dest() == "111"

    def test_translate_jump(self):
        code = Code("null")
        assert code.translate_jump() == "000"
        code = Code("JGT")
        assert code.translate_jump() == "001"
        code = Code("JEQ")
        assert code.translate_jump() == "010"
        code = Code("JLT")
        assert code.translate_jump() == "100"
        code = Code("JNE")
        assert code.translate_jump() == "101"
        code = Code("JLE")
        assert code.translate_jump() == "110"
        code = Code("JMP")
        assert code.translate_jump() == "111"

    def test_translate_comp(self):
        code = Code("0")
        assert code.translate_comp() == "0101010"
        code = Code("1")
        assert code.translate_comp() == "0111111"
        code = Code("-1")
        assert code.translate_comp() == "0111010"
        code = Code("D")
        assert code.translate_comp() == "0001100"
        code = Code("A")
        assert code.translate_comp() == "0110000"
        code = Code("M")
        assert code.translate_comp() == "1110000"
        code = Code("!D")
        assert code.translate_comp() == "0001101"
        code = Code("!A")
        assert code.translate_comp() == "0110001"
        code = Code("!M")
        assert code.translate_comp() == "1110001"
        code = Code("D+1")
        assert code.translate_comp() == "0011111"
        code = Code("1+D")
        assert code.translate_comp() == "0011111"
        code = Code("A+1")
        assert code.translate_comp() == "0110111"
        code = Code("1+A")
        assert code.translate_comp() == "0110111"
        code = Code("M+1")
        assert code.translate_comp() == "1110111"
        code = Code("1+M")
        assert code.translate_comp() == "1110111"
        code = Code("D-1")
        assert code.translate_comp() == "0001110"
        code = Code("A-1")
        assert code.translate_comp() == "0110010"
        code = Code("M-1")
        assert code.translate_comp() == "1110010"
        code = Code("D+A")
        assert code.translate_comp() == "0000010"
        code = Code("A+D")
        assert code.translate_comp() == "0000010"
        code = Code("D+M")
        assert code.translate_comp() == "1000010"
        code = Code("M+D")
        assert code.translate_comp() == "1000010"
        code = Code("D-A")
        assert code.translate_comp() == "0010011"
        code = Code("D-M")
        assert code.translate_comp() == "1010011"
        code = Code("A-D")
        assert code.translate_comp() == "0000111"
        code = Code("M-D")
        assert code.translate_comp() == "1000111"
        code = Code("D&A")
        assert code.translate_comp() == "0000000"
        code = Code("A&D")
        assert code.translate_comp() == "0000000"
        code = Code("D&M")
        assert code.translate_comp() == "1000000"
        code = Code("M&D")
        assert code.translate_comp() == "1000000"
        code = Code("D|A")
        assert code.translate_comp() == "0010101"
        code = Code("A|D")
        assert code.translate_comp() == "0010101"
        code = Code("D|M")
        assert code.translate_comp() == "1010101"
        code = Code("M|D")
        assert code.translate_comp() == "1010101"

    def test_concatenate_c_instruction(self):
        # comp = Code()
        dest = Code("D")
        jump = Code("JLE")
