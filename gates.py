def nandg(a: bool, b: bool):
    """
    A | B | Output
    --------------
    1 | 1 |   0
    1 | 0 |   1
    0 | 1 |   1
    0 | 0 |   1
    """
    return not (a and b)


def notg(a: bool):
    """
    A | Output
    ----------
    1 |   0
    0 |   1
    """
    return nandg(a, a)


def andg(a: bool, b: bool):
    """
    A | B | Output
    --------------
    1 | 1 |   1
    1 | 0 |   0
    0 | 1 |   0
    0 | 0 |   0
    """
    return notg(nandg(a, b))


def org(a: bool, b: bool):
    """
    A | B | Output
    --------------
    1 | 1 |   1
    1 | 0 |   1
    0 | 1 |   1
    0 | 0 |   0
    """
    return nandg(notg(a), notg(b))


def norg(a: bool, b: bool):
    return notg(org(a, b))


def xorg(a: bool, b: bool):
    """
    A | B | Output
    --------------
    1 | 1 |   0
    1 | 0 |   1
    0 | 1 |   1
    0 | 0 |   0
    """
    return andg(org(a, b), notg(andg(a, b)))


def multiplexor(a: bool, b: bool, sel: bool):
    """
    Sel | Output
    --------------
    0   |   A
    1   |   B
    """
    return org(andg(a, notg(sel)), andg(b, sel))


def demultiplexor(ins: bool, sel: bool) -> tuple[bool, bool]:
    """
    Sel | A   | B
    ---------------
    0   | ins | 0
    1   | 0   | ins
    """
    return andg(ins, notg(sel)), andg(ins, sel)


def half_adder(a: bool, b: bool) -> tuple[bool, bool]:
    """
    A | B | Sum | Carry
    ---------------
    0 | 0 | 0   | 0
    1 | 0 | 1   | 0
    0 | 1 | 1   | 0
    1 | 1 | 0   | 1
    """
    return xorg(a, b), andg(a, b)


def full_adder(a: bool, b: bool, c: bool) -> tuple[bool, bool]:
    """
    A | B | C | Sum | Carry
    -----------------------
    0 | 0 | 0 |  0  |  0
    0 | 0 | 1 |  1  |  0
    0 | 1 | 0 |  1  |  0
    0 | 1 | 1 |  0  |  1
    1 | 0 | 0 |  1  |  0
    1 | 0 | 1 |  0  |  1
    1 | 1 | 0 |  0  |  1
    1 | 1 | 1 |  1  |  1
    """
    sum_1, carry_1 = half_adder(a, b)
    sum_2, carry_2 = half_adder(sum_1, c)

    carry_out = org(carry_1, carry_2)

    return sum_2, carry_out


class DLatch:
    def __init__(self):
        self.nor_2_output = False

    def __call__(self, data: bool, store: bool) -> bool:
        and_1 = andg(data, store)
        and_2 = andg(notg(data), store)
        nor_1 = norg(and_1, self.nor_2_output)
        nor_2 = norg(and_2, nor_1)
        self.nor_2_output = nor_2

        return nor_2
