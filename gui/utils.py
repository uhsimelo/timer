from PyQt5 import QtGui


def try_parse_double(inp_str):
    if inp_str.isnumeric() or all(n.isnumeric() or not len(n) for n in inp_str.split('.', 1)):
        f = float(inp_str) if inp_str not in ('', '.') else 0.0
        return (True, f)
    return (False, None)

class DoubleValidator(QtGui.QDoubleValidator):
    def __init__(self, bottom=-999.0, top=999.0, precission=2):
        super().__init__(bottom, top, precission)
        self.precission = precission
        self._validate = self.validate

    def validate(self, inp_str, integ):
        parsed, fl = try_parse_double(inp_str)
        if not parsed or not (self.bottom() <= fl and fl <= self.top() and \
            (fl.is_integer() or len(inp_str.split('.')[1]) <= self.precission)):
            return (0, inp_str, integ)
        return (2, inp_str, integ)

