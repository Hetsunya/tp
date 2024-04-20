import pytest

from black_hole_list import BlackHoleList
from list_node import BlackHoleNode
from test_data import *


@pytest.mark.bhlist
def test_list_init_empty():
    lst1 = BlackHoleList()
    assert lst1.head is None
    assert lst1.tail is None
    assert isinstance(lst1, BlackHoleList)
    lst2 = BlackHoleList()
    assert isinstance(lst2, BlackHoleList)
    assert lst2.head is None
    assert lst2.tail is None


@pytest.mark.bhlist
@pytest.mark.parametrize("value, type", [
    (10, "quasar"),
    (20, "blazar"),
    (30, None),
])
def test_list_append_on_empty(value, type):
    lst = BlackHoleList()
    lst.append(value, type)
    assert isinstance(lst.head, BlackHoleNode)
    assert lst.head.value == value
    assert lst.head.type == type
    assert lst.head.next is None
    assert lst.head.prev is None
    assert lst.tail == lst.head


@pytest.mark.bhlist
@pytest.mark.parametrize("value1, type1, value2, type2", [
    (10, "quasar", 20, "blazar"),
    (20, "blazar", 30, None),
    (30, None, 40, "quasar"),
])
def test_list_append_on_nonempty(value1, type1, value2, type2):
    lst = BlackHoleList()
    lst.append(value1, type1)
    lst.append(value2, type2)
    assert lst.head.value == value1
    assert lst.head.type == type1
    assert lst.head.next.value == value2
    assert lst.head.next.type == type2
    assert lst.head.next.next is None
    assert lst.head.prev is None
    assert lst.tail == lst.head.next


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_multiple_appends(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)

    node = lst.head
    for i, (v, t) in enumerate(zip(values, types)):
        assert node.value == v
        assert node.type == t
        if i > 0:
            assert node.prev.value == values[i-1]
            assert node.prev.type == types[i-1]
        if i < len(values) - 1:
            assert node.next.value == values[i+1]
            assert node.next.type == types[i+1]
        node = node.next

    assert lst.tail == node.prev


@pytest.mark.bhlist
def test_list_len_empty():
    lst = BlackHoleList()
    assert len(lst) == 0


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_len_nonempty(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    assert len(lst) == len(values)


@pytest.mark.bhlist
def test_list_str_empty():
    assert str(BlackHoleList()) == "[]"


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_str_nonempty(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    expected_str = "[" + ", ".join([f"({v}, {t})" for v, t in zip(values, types)]) + "]"
    assert str(lst) == expected_str


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_repr_nonempty(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    expected_repr = "[" + ", ".join([f"({v}, {t})" for v, t in zip(values, types)]) + "]"
    assert repr(lst) == expected_repr


@pytest.mark.bhlist
@pytest.mark.parametrize("values1, types1, values2, types2", [
    ([10, 20, 30], ["quasar", "blazar", None], [10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], [5, 15, 25], ["blazar", "quasar", "blazar"]),
    ([10, 20, 30], ["quasar", "blazar", None], [10, 20], ["quasar", "blazar"]),
])
def test_list_eq(values1, types1, values2, types2):
    lst1 = BlackHoleList()
    lst2 = BlackHoleList()
    for v, t in zip(values1, types1):
        lst1.append(v, t)
    for v, t in zip(values2, types2):
        lst2.append(v, t)
    assert (lst1 == lst2) == (values1 == values2 and types1 == types2)


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, value_to_find, expected_result", [
    ([10, 20, 30], ["quasar", "blazar", None], 20, True),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 10, False),
    ([], [], 10, False),
])
def test_list_contains(values, types, value_to_find, expected_result):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    assert (value_to_find in lst) == expected_result


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, value_to_remove", [
    ([10, 20, 30], ["quasar", "blazar", None], 20),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 5),
    ([10], ["quasar"], 10),
])
def test_list_remove_present(values, types, value_to_remove):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    expected_len = len(values)
    lst.remove(value_to_remove)
    assert value_to_remove not in lst
    for v in values:
        if v != value_to_remove:
            assert v in lst
    assert len(lst) == expected_len - 1


    expected_quasars = [v for v, t in zip(values, types) if t == "quasar" and v != value_to_remove]
    expected_blazars = [v for v, t in zip(values, types) if t == "blazar" and v != value_to_remove]
    expected_unknown = [v for v, t in zip(values, types) if t is None and v != value_to_remove]

    assert str(lst.quasars) == get_list_str(expected_quasars)
    assert str(lst.blazars) == get_list_str(expected_blazars)
    assert str(lst.unknown) == get_list_str(expected_unknown)


@pytest.mark.bhlist
def test_list_remove_empty_raises_exception():
    lst = BlackHoleList()
    with pytest.raises(ValueError):
        lst.remove(666)


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, value_to_remove", [
    ([10, 20, 30], ["quasar", "blazar", None], 40),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 10),
    ([], [], 10),
])
def test_list_remove_absent_raises_exception(values, types, value_to_remove):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    expected_len = len(values)
    with pytest.raises(ValueError):
        lst.remove(value_to_remove)
    assert len(lst) == expected_len


@pytest.mark.bhlist
def test_list_pop_empty_raises_exception():
    lst = BlackHoleList()
    with pytest.raises(IndexError):
        lst.pop()


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10], ["quasar"]),
    ([5, 15], ["blazar", "quasar"]),
])
def test_list_pop_single(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    assert lst.pop() == values[0]
    assert len(lst) == 0
    assert lst.head is None
    assert lst.tail is None


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_pop_nonempty(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    val_len = len(values)
    pop_cnt = 0
    for v in values[::-1]:
        assert lst.pop() == v
        pop_cnt += 1
        assert len(lst) == val_len - pop_cnt


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, index, expected_value", [
    ([10, 20, 30], ["quasar", "blazar", None], 1, 20),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 0, 5),
    ([10], ["quasar"], 0, 10),
])
def test_list_pop_with_index(values, types, index, expected_value):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    assert lst.pop(index) == expected_value
    assert len(lst) == len(values) - 1


@pytest.mark.bhlist
def test_list_pop_with_index_out_of_range():
    lst = BlackHoleList()
    lst.append(10, "quasar")
    with pytest.raises(IndexError):
        lst.pop(1)


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_clear(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    lst.clear()
    assert lst.head is None
    assert lst.tail is None
    assert len(lst) == 0
    assert len(lst.quasars) == 0
    assert len(lst.blazars) == 0
    assert len(lst.unknown) == 0


@pytest.mark.bhlist
@pytest.mark.parametrize("values1, types1, values2, types2", [
    ([10, 20, 30], ["quasar", "blazar", None], [40, 50], ["blazar", "quasar"]),
    ([5, 15], ["blazar", "quasar"], [25, 35, 45], ["quasar", "blazar", None]),
    ([], [], [10], ["quasar"]),
])
def test_list_extend(values1, types1, values2, types2):
    lst1 = BlackHoleList()
    lst2 = BlackHoleList()
    for v, t in zip(values1, types1):
        lst1.append(v, t)
    for v, t in zip(values2, types2):
        lst2.append(v, t)
    lst1.extend(lst2)
    assert len(lst1) == len(values1) + len(values2)


    expected_quasars = [v for v, t in zip(values1 + values2, types1 + types2) if t == "quasar"]
    expected_blazars = [v for v, t in zip(values1 + values2, types1 + types2) if t == "blazar"]
    expected_unknown = [v for v, t in zip(values1 + values2, types1 + types2) if t is None]

    assert str(lst1.quasars) == get_list_str(expected_quasars)
    assert str(lst1.blazars) == get_list_str(expected_blazars)
    assert str(lst1.unknown) == get_list_str(expected_unknown)


@pytest.mark.bhlist
def test_list_extend_with_empty():
    lst1 = BlackHoleList()
    lst1.append(10, "quasar")
    lst2 = BlackHoleList()
    lst1.extend(lst2)
    assert len(lst1) == 1
    assert lst1.head.value == 10
    assert lst1.head.type == "quasar"


@pytest.mark.bhlist
def test_list_extend_empty_with_nonempty():
    lst1 = BlackHoleList()
    lst2 = BlackHoleList()
    lst2.append(10, "quasar")
    lst1.extend(lst2)
    assert len(lst1) == 1
    assert lst1.head.value == 10
    assert lst1.head.type == "quasar"


@pytest.mark.bhlist
def test_list_wrong_extend_raises_exception():
    lst = BlackHoleList()
    with pytest.raises(TypeError):
        lst.extend([1, 2, 3])


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_copy(values, types):
    lst1 = BlackHoleList()
    for v, t in zip(values, types):
        lst1.append(v, t)
    lst2 = lst1.copy()
    assert lst1 == lst2
    assert lst1 is not lst2
    assert lst1.head is not lst2.head
    assert lst1.tail is not lst2.tail


@pytest.mark.bhlist
@pytest.mark.parametrize("index, value, type", [
    (0, 10, "quasar"),
    (1, 20, "blazar"),
])
def test_list_insert_in_empty(index, value, type):
    lst = BlackHoleList()
    lst.insert(index, value, type)
    assert len(lst) == 1
    assert lst.head.value == value
    assert lst.head.type == type
    assert lst.head.next is None
    assert lst.head.prev is None
    assert lst.tail == lst.head


@pytest.mark.bhlist
def test_list_wrong_insert_raises_exception():
    lst = BlackHoleList()
    with pytest.raises(IndexError):
        lst.insert(-1, -1)


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, index, value, type", [
    ([10, 20, 30], ["quasar", "blazar", None], 0, 5, "blazar"),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 1, 12, "quasar"),
    ([10], ["quasar"], 0, 5, "blazar"),
])
def test_list_insert_in_head(values, types, index, value, type):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    lst.insert(index, value, type)
    assert len(lst) == len(values) + 1
    assert lst.head.value == value
    assert lst.head.type == type


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, index, value, type", [
    ([10, 20, 30], ["quasar", "blazar", None], 3, 35, "blazar"),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 2, 28, "quasar"),
    ([10], ["quasar"], 1, 15, "blazar"),
])
def test_list_insert_in_tail(values, types, index, value, type):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    lst.insert(index, value, type)
    assert len(lst) == len(values) + 1
    assert lst.tail.value == value
    assert lst.tail.type == type


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, index, value, type", [
    ([10, 20, 30], ["quasar", "blazar", None], 1, 15, "blazar"),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 2, 20, "quasar"),
])
def test_list_insert_in_nth_pos(values, types, index, value, type):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    lst.insert(index, value, type)
    assert len(lst) == len(values) + 1

    node = lst.head
    i = 0
    while node:
        if i == index:
            assert node.value == value
            assert node.type == type
        else:
            assert node.value == values[i]
            assert node.type == types[i]
        node = node.next
        i += 1


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types", [
    ([10, 20, 30], ["quasar", "blazar", None]),
    ([5, 15, 25], ["blazar", "quasar", "blazar"]),
])
def test_list_reverse(values, types):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    lst.reverse()
    assert len(lst) == len(values)

    node = lst.head
    for v, t in zip(reversed(values), reversed(types)):
        assert node.value == v
        assert node.type == t
        node = node.next


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, value_to_find, expected_index", [
    ([10, 20, 30], ["quasar", "blazar", None], 20, 1),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 5, 0),
])
def test_list_index(values, types, value_to_find, expected_index):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    assert lst.index(value_to_find) == expected_index


@pytest.mark.bhlist
def test_list_index_empty_raises_exception():
    lst = BlackHoleList()
    with pytest.raises(ValueError):
        lst.index(69)


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, value_to_find", [
    ([10, 20, 30], ["quasar", "blazar", None], 40),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 10),
])
def test_list_index_absent_raises_exception(values, types, value_to_find):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    with pytest.raises(ValueError):
        lst.index(value_to_find)


@pytest.mark.bhlist
@pytest.mark.parametrize("values, types, value_to_count, expected_count", [
    ([10, 20, 30], ["quasar", "blazar", None], 20, 1),
    ([5, 15, 25], ["blazar", "quasar", "blazar"], 5, 1),
    ([10, 10, 20], ["quasar", "quasar", "blazar"], 10, 2),
    ([], [], 10, 0),
])
def test_list_count(values, types, value_to_count, expected_count):
    lst = BlackHoleList()
    for v, t in zip(values, types):
        lst.append(v, t)
    assert lst.count(value_to_count) == expected_count
