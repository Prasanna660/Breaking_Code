```python
# Original code
def calculate_area(width, height):
  if width <= 0 or height <= 0:
    raise ValueError("Width and height must be positive.")
  return width * height

# Static testing - Unit Testing
import unittest

class TestCalculateArea(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(calculate_area(5, 10), 50)

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_area(0, 10)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_area(-5, 10)

# Code Review - Identify issues
# Incorrect error message in ValueError

# Code Correction
def calculate_area(width, height):
  if width <= 0 or height <= 0:
    raise ValueError("Both width and height must be positive.")
  return width * height

# Corrected code
import unittest

class TestCalculateArea(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(calculate_area(5, 10), 50)

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_area(0, 10)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_area(-5, 10)

# Run the corrected code
if __name__ == "__main__":
    unittest.main()
```