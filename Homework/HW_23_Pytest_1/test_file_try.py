from structure_without_list import StructureWithoutList, Item


class TestInit:
    """Класс для тестирования правильности создания экземпляра класса и метода reset"""
    issue = StructureWithoutList()

    def test_length(self):
        assert TestInit.issue.length == 0

    def test_cur_it(self):
        assert TestInit.issue.current_item is None

    def test_cur_ind(self):
        assert TestInit.issue.current_index == 0


class TestAddFirstItem:
    """Тест правильности добавления первого элемента"""
    issue = StructureWithoutList()
    issue.add(1)
    item = Item(1, None, None)

    def test_cur_it(self):
        assert TestAddFirstItem.item.value == TestAddFirstItem.issue.current_item.value

    def test_cur_ind(self):
        assert TestAddFirstItem.issue.current_index == 1

    def test_length(self):
        assert TestAddFirstItem.issue.length == 1


class TestAddSecondItem:
    """Тест правильности добавления второго элемента"""
    issue = StructureWithoutList()
    issue.add(1)
    issue.add('Hello second')
    item = Item('Hello second', 1, None)

    def test_cur_it(self):
        assert TestAddSecondItem.item.value == TestAddSecondItem.issue.current_item.value

    def test_prev_it(self):
        assert TestAddSecondItem.item.prev_item == 1

    def test_cur_ind(self):
        assert TestAddSecondItem.issue.current_index == 2

    def test_length(self):
        assert TestAddSecondItem.issue.length == 2
