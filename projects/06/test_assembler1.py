#!/usr/bin/env python3
"""Unit test specs for assembler1.py"""
import os
import filecmp
import assembler1 as asmb


def test_truthy():
    """Test a truthy case"""
    assert 1 + 1 == 2

class TestAssembler:
    """Tests for the assembler"""

    def test_filename_given(self):
        assert (asmb.filename_given(['./assembler.py', 'add/Add.asm']))
        assert (not asmb.filename_given(['./assembler.py']))

    def test_filename_valid(self):
        """Checks if file extension is asm"""
        assert (asmb.filename_valid("file.asm"))
        assert (asmb.filename_valid("file.name.asm"))
        assert (asmb.filename_valid("directory/file.name.asm"))
        assert (not asmb.filename_valid("file.hack"))
        assert (not asmb.filename_valid("file"))
        assert (not asmb.filename_valid("asm"))
        assert (not asmb.filename_valid("file."))
        assert (not asmb.filename_valid(".asm"))

    def test_main(self):
        os.system("./assembler.py add/Add.asm")
        assert (filecmp.cmp("add/Add.cmp", "add/Add.hack"))

        os.system("./assembler.py max/MaxL.asm")
        assert (filecmp.cmp("max/MaxL.cmp", "max/MaxL.hack"))

        os.system("./assembler.py rect/RectL.asm")
        assert (filecmp.cmp("rect/RectL.cmp", "rect/RectL.hack"))

        os.system("./assembler.py pong/PongL.asm")
        assert (filecmp.cmp("pong/PongL.cmp", "pong/PongL.hack"))
