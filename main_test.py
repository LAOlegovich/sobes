import pytest

from main import is_correct_str



@pytest.mark.parametrize (
        "inp_str, output",
        [
            ('({)][)]', 'Несбалансированно'), ('((({[]})))','Сбалансированно'), ('(r{()})','В строке содержатся символы, несоответствующие шаблону!')
        ]
    )
def test(inp_str,output):
    result = is_correct_str(inp_str)

    assert result == output
