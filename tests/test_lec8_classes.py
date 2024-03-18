import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

def test_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)
    
def test_16_coordinate():
    m = lc.Coordinate(7, 24)
    n = lc.Coordinate(0,0)
    assert m.x == 7
    assert m.y == 24
    assert m.distance(n) == 25
    assert n.distance(m) == 25
	
	

