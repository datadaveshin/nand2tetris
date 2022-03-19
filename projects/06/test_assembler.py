#!/usr/bin/env python3
"""Unit test specs for assembler.py"""
import os
import filecmp
import assembler as asmb


def test_truthy():
    """Test a truthy case"""
    assert 1 + 1 == 2

class TestAssembler:
    """Tests for the assembler"""

    def test_filename_given(self):
        assert (asmb.filename_given(['./assembler.py', 'add/Add.asm']) is True)
        assert (asmb.filename_given(['./assembler.py']) is False)

    def test_filename_valid(self):
        """Checks if file extension is asm"""
        assert (asmb.filename_valid("file.asm") is True)
        assert (asmb.filename_valid("file.name.asm") is True)
        assert (asmb.filename_valid("directory/file.name.asm") is True)
        assert (asmb.filename_valid("file.hack") is False)
        assert (asmb.filename_valid("file") is False)
        assert (asmb.filename_valid("asm") is False)
        assert (asmb.filename_valid("file.") is False)
        assert (asmb.filename_valid(".asm") is False)

    def test_main(self):
        os.system("assembler.py Add/add.asm")
        assert (filecmp.cmp("Add/add.hack", "my_Add.cmp") is True)
