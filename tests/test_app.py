# test_app.py

from src.app import sumar, restar

def test_sumar():
    assert sumar(2, 3) == 5

#cambiar el resultado pra que el test esté correcto
def test_restar():
    assert restar(5, 3) == 2