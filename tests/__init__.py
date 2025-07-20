import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from your_module import YourClass

@pytest.fixture
def your_class():
    return YourClass()

def test_your_method(your_class):
    with patch.object(your_class, 'your_method') as mock_method:
        mock_method.return_value = 'mocked_value'
        result = your_class.your_method()
        assert result == 'mocked_value'
        mock_method.assert_called_once()

def test_your_property(your_class):
    with patch.object(your_class, 'your_property', new_callable=PropertyMock) as mock_property:
        mock_property.return_value = 'mocked_value'
        assert your_class.your_property == 'mocked_value'
        mock_property.assert_called_once()

def test_your_method_with_side_effect(your_class):
    with patch.object(your_class, 'your_method') as mock_method:
        mock_method.side_effect = Exception('Mocked exception')
        with pytest.raises(Exception):
            your_class.your_method()
        mock_method.assert_called_once()

def test_your_property_with_side_effect(your_class):
    with patch.object(your_class, 'your_property', new_callable=PropertyMock) as mock_property:
        mock_property.side_effect = Exception('Mocked exception')
        with pytest.raises(Exception):
            your_class.your_property
        mock_property.assert_called_once()