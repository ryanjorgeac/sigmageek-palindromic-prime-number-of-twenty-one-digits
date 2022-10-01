import intervals

class inputFake():
    def __init__(self, lista):
        self.inputlist = lista
        self.outputlist = []

    def print(self, prompt):
        self.outputlist.append(prompt)

def test_intervals_insertSucess_1():

    interval = (0, 11)
    position = 3
    prime = 11
    i = inputFake([interval, position, prime])
    x = intervals.intervals(i)
    y = x.insertSuccess(i.inputlist[0], i.inputlist[1], i.inputlist[2])
    assert i.outputlist[0] == f"Prime: {prime}, Position: {position}"

def test_intervals_insertSucess_2():
    interval = (0, 20)
    interval1\
        = (19, 40)
    position = 4
    prime = 13
    i = inputFake([interval, position, prime])
    x = intervals.intervals(i)
    y = x.insertSuccess(i.inputlist[0], i.inputlist[1], i.inputlist[2])
    assert len(i.outputlist) == 0

