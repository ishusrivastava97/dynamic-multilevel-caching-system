import unittest
from Cache import Cache

class TestCache(unittest.TestCase):
    def test_lru_cache(self):
        cache = Cache(2, 'LRU')
        cache.put("A", "1")
        cache.put("B", "2")
        self.assertEqual(cache.get("A"), "1")
        cache.put("C", "3")
        self.assertIsNone(cache.get("B"))
        self.assertEqual(cache.get("C"), "3")

    def test_lfu_cache(self):
        cache = Cache(2, 'LFU')
        cache.put("X", "10")
        cache.put("Y", "20")
        self.assertEqual(cache.get("X"), "10")
        cache.put("Z", "30")
        self.assertIsNone(cache.get("Y"))
        self.assertEqual(cache.get("Z"), "30")

if __name__ == "__main__":
    unittest.main()
