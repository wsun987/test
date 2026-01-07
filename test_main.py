#!/usr/bin/env python3
"""
Basic tests for the desktop application
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys


class TestDesktopApp(unittest.TestCase):
    """Test cases for the DesktopApp class"""
    
    def setUp(self):
        """Set up mocks for tkinter module"""
        # Mock the entire tkinter module
        self.tkinter_mock = MagicMock()
        sys.modules['tkinter'] = self.tkinter_mock
    
    def tearDown(self):
        """Clean up mocks"""
        if 'tkinter' in sys.modules and isinstance(sys.modules['tkinter'], MagicMock):
            del sys.modules['tkinter']
        if 'main' in sys.modules:
            del sys.modules['main']
    
    def test_import(self):
        """Test that main module can be imported"""
        try:
            import main
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import main module: {e}")
    
    def test_app_has_required_methods(self):
        """Test that DesktopApp has required methods"""
        import main
        
        # Verify the class exists
        self.assertTrue(hasattr(main, 'DesktopApp'))
        
        # Verify required methods exist
        self.assertTrue(hasattr(main.DesktopApp, '__init__'))
        self.assertTrue(hasattr(main.DesktopApp, 'show_greeting'))
        self.assertTrue(hasattr(main.DesktopApp, 'clear_output'))
    
    def test_main_function_exists(self):
        """Test that main function exists"""
        import main
        
        self.assertTrue(hasattr(main, 'main'))
        self.assertTrue(callable(main.main))


if __name__ == '__main__':
    unittest.main()
