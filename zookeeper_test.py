import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    def test_versiones(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.delete('/node1', 1)
    
    def test_exists(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.exist('/node1')

    def test_show_nodes(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.create('/node2', 'algo', True, True, 10, '/node1')
        tree.showTree()
    
    def test_crear_multinodes(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.create('/node2', 'algo', True, True, 10, '/')
        tree.create('/node3', 'algo', True, True, 10, '/')
        tree.create('/node4', 'algo', True, True, 10, '/')
        tree.create('/node5', 'algo', True, True, 10, '/')
        tree.create('/node6', 'algo', True, True, 10, '/')
        tree.create('/node7', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node2'), 'algo')

    def test_crear_znode_error(self):
        tree = Ztree()
        tree.create('/node1/node2/node3', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')


if __name__ == '__main__':
    unittest.main()

