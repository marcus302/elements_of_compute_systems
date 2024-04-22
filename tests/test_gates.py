from gates import *


def test_nandg():
    assert nandg(True, False) == True
    assert nandg(False, True) == True
    assert nandg(False, False) == True
    assert nandg(True, True) == False


def test_notg():
    assert notg(True) == False
    assert notg(False) == True


def test_andg():
    assert andg(True, True) == True
    assert andg(True, False) == False
    assert andg(False, True) == False
    assert andg(False, False) == False


def test_org():
    assert org(True, False) == True
    assert org(False, True) == True
    assert org(True, True) == True
    assert org(False, False) == False


def test_xorg():
    assert xorg(True, False) == True
    assert xorg(False, True) == True
    assert xorg(True, True) == False
    assert xorg(False, False) == False


def test_multiplexor():
    assert multiplexor(True, False, False) == True
    assert multiplexor(True, True, False) == True
    assert multiplexor(True, False, True) == False


def test_demultiplexor():
    assert demultiplexor(True, False) == (True, False)
    assert demultiplexor(False, False) == (False, False)
    assert demultiplexor(True, True) == (False, True)
    assert demultiplexor(False, True) == (False, False)


def test_half_adder():
    assert half_adder(True, True) == (False, True)
    assert half_adder(True, False) == (True, False)
    assert half_adder(False, False) == (False, False)


def test_full_adder():
    assert full_adder(False, False, False) == (False, False)
    assert full_adder(False, False, True) == (True, False)
    assert full_adder(False, True, False) == (True, False)
    assert full_adder(False, True, True) == (False, True)
    assert full_adder(True, False, False) == (True, False)
    assert full_adder(True, False, True) == (False, True)
    assert full_adder(True, True, False) == (False, True)
    assert full_adder(True, True, True) == (True, True)


def test_data_flip_flop():
    dff = DLatch()

    dff(True, False) == True
    dff(False, False) == True
    dff(False, True) == False
    dff(True, False) == False
