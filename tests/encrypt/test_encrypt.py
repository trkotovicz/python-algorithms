import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    """Testa os retornos com parâmetros válidos"""
    assert encrypt_message('AABBCC', 3) == 'BAA_CCB'

    assert encrypt_message('AABBCC', -1) == 'CCBBAA'

    """Testa se retorna erro quando os parâmetros são inválidos"""
    with pytest.raises(TypeError):
        encrypt_message(123, 2)

    with pytest.raises(TypeError):
        encrypt_message('AABBCC', 'AA')
