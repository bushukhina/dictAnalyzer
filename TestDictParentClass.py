class DictParentTest:
    dict_type = dict

    def test_add(self):
        d = self.dict_type()
        d['a'] = 'b'
        self.assertIn('a', d)
        self.assertNotIn('b', d)

    def test_get(self):
        d = self.dict_type()
        d['a'] = 'b'
        d['c'] = 'd'
        d['e'] = 'f'
        self.assertEqual(d['e'], 'f')
        self.assertRaises(KeyError, d.__getitem__, 'z')

    def test_delete(self):
        d = self.dict_type()
        d['a'] = 'b'
        d['c'] = 'd'
        d['e'] = 'f'
        del d['e']
        self.assertSetEqual(set(d.values()), {'b', 'd'})
        self.assertRaises(KeyError, d.__delitem__, 'z')

    def test_items(self):
        d = self.dict_type()
        d['a'] = 'b'
        d['c'] = 'd'
        d['e'] = 'f'
        expected_set = {'a': 'b', 'c': 'd', 'e': 'f'}
        self.assertEqual(d, expected_set)

    def test_keys(self):
        d = self.dict_type()
        d['a'] = 'b'
        d['c'] = 'd'
        d['e'] = 'f'
        self.assertSetEqual(set(d.keys()), {'a', 'c', 'e'})

    def test_values(self):
        d = self.dict_type()
        d['a'] = 'b'
        d['c'] = 'd'
        d['e'] = 'f'
        self.assertSetEqual(set(d.values()), {'b', 'd', 'f'})
