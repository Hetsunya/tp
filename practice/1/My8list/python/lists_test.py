import pytest

from black_hole_node import BlackHoleNode
from my_black_hole_list import MyBlackHoleList
from test_data import *

@pytest.fixture(params=[SINGLE_VALUES1, SINGLE_VALUES2])
def get_5_black_holes(request):
    return {
        "values": request.param,
        "black_holes": BlackHoleNode(
            request.param[0],
            BlackHoleNode(
                request.param[1],
                BlackHoleNode(
                    request.param[2],
                    BlackHoleNode(request.param[3], BlackHoleNode(request.param[4])),
                ),
            ),
        ),
        "str": get_list_str(request.param),
    }

# Тесты для BlackHoleNode

@pytest.mark.blackholenode
@pytest.mark.parametrize("value", SINGLE_VALUES1)
def test_single_black_hole_node_init(value):
    bhn = BlackHoleNode(value)
    assert isinstance(bhn, BlackHoleNode)
    assert bhn.value == value
    assert bhn.next is None
    assert bhn.prev is None
    assert bhn.is_black_hole is False

@pytest.mark.blackholenode
def test_wrong_black_hole_node_init_raises_exception():
    with pytest.raises(TypeError):
        BlackHoleNode(1, 2)

@pytest.mark.blackholenode
@pytest.mark.parametrize("value1, value2", DOUBLE_VALUES)
def test_double_black_hole_node_init(value1, value2):
    bhn2 = BlackHoleNode(value2)
    bhn1 = BlackHoleNode(value1, next=bhn2)
    assert isinstance(bhn1, BlackHoleNode)
    assert bhn1.value == value1
    assert bhn1.next == bhn2
    assert bhn1.prev is None

    assert isinstance(bhn2, BlackHoleNode)
    assert bhn2.value == value2
    assert bhn2.next is None
    assert bhn2.prev == bhn1

@pytest.mark.blackholenode
@pytest.mark.parametrize("value", SINGLE_VALUES2)
def test_single_black_hole_node_str(value):
    bhn = BlackHoleNode(value)
    assert str(bhn) == f"({value}) -> None"

@pytest.mark.blackholenode
@pytest.mark.parametrize("values, str_values", STR_CHECK_2_VALUES)
def test_double_black_hole_node_str(values, str_values):
    black_holes = BlackHoleNode(values[0], BlackHoleNode(values[1]))
    assert str(black_holes) == str_values

# Тесты для MyBlackHoleList

@pytest.mark.myblackholelist
def test_black_hole_list_init_empty():
    bhlst1 = MyBlackHoleList()
    assert bhlst1.head is None
    assert isinstance(bhlst1, MyBlackHoleList)

@pytest.mark.myblackholelist
@pytest.mark.parametrize("value", SINGLE_VALUES1)
def test_black_hole_list_init_nonempty(value):
    bhlst = MyBlackHoleList(value)
    assert isinstance(bhlst, MyBlackHoleList)
    assert isinstance(bhlst.head, BlackHoleNode)
    assert bhlst.head.value == value
    assert bhlst.head.next is None

@pytest.mark.myblackholelist
@pytest.mark.parametrize("value", SINGLE_VALUES2)
def test_black_hole_list_append_on_empty(value):
    bhlst = MyBlackHoleList()
    bhlst.append(value)
    assert isinstance(bhlst.head, BlackHoleNode)
    assert bhlst.head.value == value
    assert bhlst.head.next is None

@pytest.mark.myblackholelist
@pytest.mark.parametrize("value1, value2", DOUBLE_VALUES)
def test_black_hole_list_append_on_nonempty(value1, value2):
    bhlst = MyBlackHoleList(value1)
    bhlst.append(value2)
    assert bhlst.head.value == value1
    assert bhlst.head.next == BlackHoleNode(value2)
    assert bhlst.head.next.value == value2
    assert bhlst.head.next.next is None

# Другие тесты для MyBlackHoleList можно адаптировать из предыдущих тестов для MyList, добавив тесты, специфичные для работы с "чёрными дырами".
