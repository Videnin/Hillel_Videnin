import pytest

from pixel import Pixel

def test_create_pixel_with_valid_components():
    pixel = Pixel(100, 150, 200)
    assert pixel.red == 100
    assert pixel.green == 150
    assert pixel.blue == 200

def test_create_pixel_with_invalid_components():
    with pytest.raises(ValueError):
        Pixel(300, 150, 200)  # Red component exceeds the valid range
    with pytest.raises(ValueError):
        Pixel(100, 400, 200)  # Green component exceeds the valid range
    with pytest.raises(ValueError):
        Pixel(100, 150, -50)  # Blue component is below the valid range

def test_get_components():
    pixel = Pixel(100, 150, 200)
    assert pixel.get_red() == 100
    assert pixel.get_green() == 150
    assert pixel.get_blue() == 200

def test_pixel_addition():
    pixel1 = Pixel(100, 150, 200)
    pixel2 = Pixel(50, 75, 100)
    result = pixel1 + pixel2
    assert isinstance(result, Pixel)
    assert result.red == 150
    assert result.green == 225
    assert result.blue == 255  # The maximum value is capped at 255

def test_pixel_subtraction():
    pixel1 = Pixel(100, 150, 200)
    pixel2 = Pixel(50, 75, 100)
    result = pixel1 - pixel2
    assert isinstance(result, Pixel)
    assert result.red == 50
    assert result.green == 75
    assert result.blue == 100

@pytest.mark.xfail(reason="Multiplication by zero should raise a ValueError")
def test_pixel_multiplication_by_zero():
    pixel = Pixel(100, 150, 200)
    result = pixel * 0

@pytest.mark.xfail(reason="Multiplication by a negative number should raise a ValueError")
def test_pixel_multiplication_by_negative_number():
    pixel = Pixel(100, 150, 200)
    result = pixel * (-1)

@pytest.mark.xfail(reason="Multiplication by a non-numeric type should raise a TypeError")
def test_pixel_multiplication_by_non_numeric_type():
    pixel = Pixel(100, 150, 200)
    result = pixel * "2"

def test_pixel_multiplication_by_integer():
    pixel = Pixel(100, 150, 200)
    result = pixel * 2
    assert isinstance(result, Pixel)
    assert result.red == 200
    assert result.green == 255
    assert result.blue == 255

def test_pixel_multiplication_by_float():
    pixel = Pixel(100, 150, 200)
    result = pixel * 1.5
    assert isinstance(result, Pixel)
    assert result.red == 150
    assert result.green == 225
    assert result.blue == 255

@pytest.mark.xfail(reason="Division by zero should raise a ValueError")
def test_pixel_division_by_zero():
    pixel = Pixel(100, 150, 200)
    result = pixel / 0

@pytest.mark.xfail(reason="Division by a non-numeric type should raise a TypeError")
def test_pixel_division_by_non_numeric_type():
    pixel = Pixel(100, 150, 200)
    result = pixel / "2"

def test_pixel_division_by_integer():
    pixel = Pixel(100, 150, 200)
    result =
