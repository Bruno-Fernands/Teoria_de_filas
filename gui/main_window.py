from PyQt6 import QtWidgets
from gui.model_widget import ModelWidget
from queue_models import (
    mm1, mms, mm1_k, mms_k, mm1_n, mms_n, mg1, priorities_preemptive,
    priorities_nonpreemptive, mm_inf
)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora de Modelos de Filas (com extras)')

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        vlayout = QtWidgets.QVBoxLayout(central)

        hl = QtWidgets.QHBoxLayout()
        vlayout.addLayout(hl)
        hl.addWidget(QtWidgets.QLabel('Modelo:'))
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems([
            'M/M/1',
            'M/M/s',
            'M/M/1/K',
            'M/M/s/K',
            'M/M/1/N',
            'M/M/s/N',
            'M/G/1',
            'Prioridades (preemptiva)',
            'Prioridades (Nao preemptiva)',
            'M/M/∞'
        ])
        hl.addWidget(self.combo)

        self.form = ModelWidget()
        vlayout.addWidget(self.form)

        btns = QtWidgets.QHBoxLayout()
        vlayout.addLayout(btns)
        self.solve_btn = QtWidgets.QPushButton('Resolver')
        btns.addWidget(self.solve_btn)
        self.clear_btn = QtWidgets.QPushButton('Limpar campos')
        btns.addWidget(self.clear_btn)
        self.example_btn = QtWidgets.QPushButton('Carregar exemplo')
        btns.addWidget(self.example_btn)

        self.output = QtWidgets.QTextEdit()
        self.output.setReadOnly(True)
        vlayout.addWidget(self.output)

        self.combo.currentIndexChanged.connect(self.load_fields_for_model)
        self.solve_btn.clicked.connect(self.solve)
        self.clear_btn.clicked.connect(self.form.clear_fields)
        self.example_btn.clicked.connect(self.load_example)

        self.load_fields_for_model()

    def load_fields_for_model(self):
        m = self.combo.currentText()
        self.form.clear()
        if m == 'M/M/1':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')
        elif m == 'M/M/s':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_int('s', 'Número de servidores (C)')
        elif m == 'M/M/1/K':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_int('K', 'Capacidade máxima (K)')
        elif m == 'M/M/s/K':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_int('s', 'Número de servidores (s)')
            self.form.add_int('K', 'Capacidade máxima (K)')
        elif m == 'M/M/1/N':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_int('N', 'População (N)')
        elif m == 'M/M/s/N':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_int('s', 'Número de servidores (s)')
            self.form.add_int('N', 'População (N)')
        elif m == 'M/G/1':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_float('sigma2', 'Variância do tempo de serviço (σ²)')
        elif m == 'Prioridades (preemptiva)':
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_text('lambdas', 'taxa de chegada por classe (λ) — prioridade desc')
        elif m == 'Prioridades (Nao preemptiva)':
            self.form.add_float('mu', 'Taxa de serviço (μ)')
            self.form.add_text('lambdas', 'taxa de chegada por classe (λ) — prioridade desc')
        elif m == 'M/M/∞':
            self.form.add_float('lambda_', 'taxa de chegada (λ)')
            self.form.add_float('mu', 'Taxa de serviço (μ)')

    def load_example(self):
        m = self.combo.currentText()
        self.form.clear()
        if m == 'M/M/1':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='0.3')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='0.5')
        elif m == 'M/M/s':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='5')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='7')
            self.form.add_int('s', 'Número de servidores (C)', default='2')
        elif m == 'M/M/1/K':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='0.3')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='0.5')
            self.form.add_int('K', 'Capacidade máxima (K)', default='2')
        elif m == 'M/M/s/K':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='20')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='5')
            self.form.add_int('s', 'Número de servidores (s)', default='3')
            self.form.add_int('K', 'Capacidade máxima (K)', default='5')
        elif m == 'M/M/1/N':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='0.2')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='1')
            self.form.add_int('N', 'População (N)', default='5')
        elif m == 'M/M/s/N':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='0.2')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='0.5')
            self.form.add_int('s', 'Número de servidores (s)', default='3')
            self.form.add_int('N', 'População (N)', default='15')
        elif m == 'M/G/1':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='4')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='6')
            self.form.add_float('sigma2', 'Variância do tempo de serviço (σ²)', default='0.02')
        elif m == 'Prioridades (preemptiva)':
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='3')
            self.form.add_text('lambdas', 'taxa de chegada por classe (λ) — prioridade desc', default='0.2,0.6,1.2')
        elif m == 'Prioridades (Nao preemptiva)':
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='3')
            self.form.add_text('lambdas', 'taxa de chegada por classe (λ) — prioridade desc', default='0.2,0.6,1.2')
        elif m == 'M/M/∞':
            self.form.add_float('lambda_', 'taxa de chegada (λ)', default='8')
            self.form.add_float('mu', 'Taxa de serviço (μ)', default='1')

    def solve(self):
        m = self.combo.currentText()
        self.output.clear()
        try:
            data = self.form.get_all()
            if m == 'M/M/1':
                res = mm1(**data)
            elif m == 'M/M/s':
                res = mms(**data)
            elif m == 'M/M/1/K':
                res = mm1_k(**data)
            elif m == 'M/M/s/K':
                res = mms_k(**data)
            elif m == 'M/M/1/N':
                res = mm1_n(**data)
            elif m == 'M/M/s/N':
                res = mms_n(**data)
            elif m == 'M/G/1':
                res = mg1(**data)
            elif m == 'Prioridades (preemptiva)':
                res = priorities_preemptive(**data)
            elif m == 'Prioridades (Nao preemptiva)':
                res = priorities_nonpreemptive(**data)
            elif m == 'M/M/∞':
                res = mm_inf(**data)
            else:
                res = {'error': 'Modelo não suportado'}

            self.output.setPlainText(self.pretty(res))
        except Exception as e:
            self.output.setPlainText(f'Erro: {e}')

    def pretty(self, data):
        if isinstance(data, dict):
            lines = []
            for k, v in data.items():
                if isinstance(v, list):
                    lines.append(f'{k}:')
                    for i, item in enumerate(v):
                        lines.append(f'  [{i}] {item}')
                else:
                    lines.append(f'{k}: {v}')
            return '\n'.join(lines)
        return str(data)
