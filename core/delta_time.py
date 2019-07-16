
class DeltaTime:
    def __init__(self, h=0, m=0, s=0):
        self._h = self._m = self._s = 0 
        self.h = h
        self.m = m
        self.s = s

    def __add__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError
        return DeltaTime(h=self.h + other.h, m=self.m + other.m, s=self.s + other.s)

    def __bool__(self):
        return True

    def __str__(self):
        return f'{self.h}:{self.m}:{self.s}'

    def __repr__(self):
        return f'delta_time({self.h}:{self.m}:{self.s})'

    @property   
    def h(self):
        return self._h
    
    @h.setter
    def h(self, value):
        assert isinstance(value, int)
        self._h = value    
    
    @property
    def m(self):
        return self._m
    
    @m.setter
    def m(self, value):
        assert isinstance(value, int)
        self._m = value
        if self._m >= 60:
            self.h += self._m // 60
            self._m = self._m % 60
    
    @property
    def s(self):
        return self._s
    
    @s.setter
    def s(self, value):
        assert isinstance(value, int)
        self._s = value
        if self._s >= 60:
            self.m += self._s // 60
            self._s = self._s % 60
                
