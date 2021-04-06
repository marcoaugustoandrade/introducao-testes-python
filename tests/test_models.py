from src.models import Conta

def test_realiza_deposito_na_conta_criada():
    c1 = Conta(1)
    c1.depositar(100.00)
    assert 100.00 == c1.saldo()
    c1.depositar(50.00)
    assert 150.00 == c1.saldo()

def test_realiza_saque_na_conta_criada():
    c1 = Conta(1)
    c1.sacar(20)
    assert -20.00 == c1.saldo()
    c1.depositar(100)
    assert 80.00 == c1.saldo()

