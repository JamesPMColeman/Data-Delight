import unittest
from unittest.mock import patch


class TestFirstFigure(unittest.TestCase):

	@patch('scripts.first_figure.show')
	def test_call_output_file(self, mock_show):
		pass