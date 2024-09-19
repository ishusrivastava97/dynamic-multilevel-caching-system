import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from MultiLevelCache import MultiLevelCache

import unittest
from MultiLevelCache import MultiLevelCache

class TestMultiLevelCache(unittest.TestCase):
    def test_basic_operations(self):
        cache_system = MultiLevelCache()
        cache_system.add_cache_level(2, 'LRU')
        cache_system.add_cache_level(2, 'LFU')
        cache_system.put("A", "1")
        cache_system.put("B", "2")
        self.assertEqual(cache_system.get("A"), "1")
        cache_system.put("C", "3")
        self.assertIsNone(cache_system.get("B"))
        self.assertEqual(cache_system.get("C"), "3")

    def test_dynamic_levels(self):
        cache_system = MultiLevelCache()
        cache_system.add_cache_level(2, 'LRU')
        cache_system.put("A", "100")
        cache_system.put("B", "200")
        cache_system.remove_cache_level(1)
        cache_system.put("C", "300")
        self.assertEqual(cache_system.get("A"), "100")
        self.assertEqual(cache_system.get("C"), "300")

if __name__ == "__main__":
    unittest.main()
