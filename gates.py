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
