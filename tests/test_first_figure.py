import unittest
from unittest.mock import patch


class TestFirstFigure(unittest.TestCase):

	@patch('scripts.first_figure.show')
	@patch('scripts.first_figure.output_file')
	def test_call_output_file(self, mock_show, mock_output):
		pass