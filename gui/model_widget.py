from PyQt6 import QtWidgets

class ModelWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QFormLayout(self)
        self._fields = {}

    def clear(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self._fields = {}

    def add_float(self, key, label, default=''):
        ed = QtWidgets.QLineEdit()
        ed.setText(str(default))
        self.layout.addRow(label + ':', ed)
        self._fields[key] = ('float', ed)

    def add_int(self, key, label, default=''):
        ed = QtWidgets.QLineEdit()
        ed.setText(str(default))
        self.layout.addRow(label + ':', ed)
        self._fields[key] = ('int', ed)

    def add_text(self, key, label, default=''):
        ed = QtWidgets.QLineEdit()
        ed.setText(str(default))
        self.layout.addRow(label + ':', ed)
        self._fields[key] = ('text', ed)

    def get_all(self):
        out = {}
        for k, (typ, widget) in self._fields.items():
            txt = widget.text().strip()
            if typ == 'float':
                out[k] = float(txt) if txt != '' else 0.0
            elif typ == 'int':
                out[k] = int(txt) if txt != '' else 0
            elif typ == 'text':
                if k == 'lambdas':
                    items = [s.strip() for s in txt.split(',') if s.strip()]
                    out[k] = [float(x) for x in items]
                else:
                    out[k] = txt
        return out

    def clear_fields(self):
        for typ, widget in self._fields.values():
            widget.clear()
