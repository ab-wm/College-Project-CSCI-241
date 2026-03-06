import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):
  
    def setUp(self):
        self.__tree = Binary_Search_Tree()

    ####################
    # Core BST testing #
    ####################
    def test_coreBST_empty_str_insert (self):
        self.assertEqual('[ ]', str(self.__tree))
    def test_coreBST_empty_height_insert (self):
        self.assertEqual(0, self.__tree.get_height())
    def test_coreBST_empty_preOrder_insert (self):
        self.assertEqual('[ ]', self.__tree.pre_order())
    def test_coreBST_empty_postOrder_insert (self):
        self.assertEqual('[ ]', self.__tree.post_order())
    def test_coreBST_empty_toList_insert (self):
        self.assertEqual([], self.__tree.to_list())
    def test_coreBST_empty_str_remove_root (self):
        try:
            self.__tree.remove_element(10)
        except:
            pass
        self.assertEqual('[ ]', str(self.__tree))
    def test_coreBST_empty_height_remove_root (self):
        try:
            self.__tree.remove_element(10)
        except:
            pass
        self.assertEqual(0, self.__tree.get_height())
    def test_coreBST_empty_preOrder_remove_root (self):
        try:
            self.__tree.remove_element(10)
        except:
            pass
        self.assertEqual('[ ]', self.__tree.pre_order())
    def test_coreBST_empty_postOrder_remove_root (self):
        try:
            self.__tree.remove_element(10)
        except:
            pass
        self.assertEqual('[ ]', self.__tree.post_order())
    def test_coreBST_empty_toList_remove_root (self):
        try:
            self.__tree.remove_element(10)
        except:
            pass
        self.assertEqual([], self.__tree.to_list())
    def test_coreBST_empty_exception_remove_root (self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(10)


    def test_coreBST_insert_10_success (self):
        self.__tree.insert_element(10)
    def test_coreBST_insert_10_height (self):
        self.__tree.insert_element(10)
        self.assertEqual(1, self.__tree.get_height())
    def test_coreBST_insert_10_str (self):
        self.__tree.insert_element(10)
        self.assertEqual('[ 10 ]', str(self.__tree))
    def test_coreBST_insert_10_preOrder (self):
        self.__tree.insert_element(10)
        self.assertEqual('[ 10 ]', self.__tree.pre_order())    
    def test_coreBST_insert_10_postOrder (self):
        self.__tree.insert_element(10)
        self.assertEqual('[ 10 ]', self.__tree.post_order())
    def test_coreBST_insert_10_toList (self):
        self.__tree.insert_element(10)
        self.assertEqual([10], self.__tree.to_list()) 
    def test_coreBST_insert_10_remove_10_success (self):
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
    def test_coreBST_insert_10_remove_10_height (self):
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual(0, self.__tree.get_height())
    def test_coreBST_insert_10_remove_10_str (self):
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ ]', str(self.__tree))
    def test_coreBST_insert_10_remove_10_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ ]', self.__tree.pre_order())    
    def test_coreBST_insert_10_remove_10_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ ]', self.__tree.post_order())
    def test_coreBST_insert_10_remove_10_toList (self):
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual([], self.__tree.to_list()) 
    def test_coreBST_insert_10_remove_10_exception (self):
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(10)
#####
    def test_coreBST_insert_20_10_success (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
    def test_coreBST_insert_20_10_height (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_20_10_str (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 20 ]', str(self.__tree))
    def test_coreBST_insert_20_10_preOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.assertEqual('[ 20, 10 ]', self.__tree.pre_order())
    def test_coreBST_insert_20_10_postOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 20 ]', self.__tree.post_order())
    def test_coreBST_insert_20_10_toList (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.assertEqual([10,20], self.__tree.to_list())
#
    def test_coreBST_insert_20_10_remove_10_success (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
    def test_coreBST_insert_20_10_remove_10_height (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual(1, self.__tree.get_height())
    def test_coreBST_insert_20_10_remove_10_str (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ 20 ]', str(self.__tree))
    def test_coreBST_insert_20_10_remove_10_preOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ 20 ]', self.__tree.pre_order())
    def test_coreBST_insert_20_10_remove_10_postOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('[ 20 ]', self.__tree.post_order())
    def test_coreBST_insert_20_10_remove_10_toList (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual([20], self.__tree.to_list())
    def test_coreBST_insert_20_10_remove_10_exception (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10) 
        with self.assertRaises(ValueError):
            self.__tree.remove_element(10)    
#
    def test_coreBST_insert_20_10_remove_20_success (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
    def test_coreBST_insert_20_10_remove_20_height (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual(1, self.__tree.get_height())
    def test_coreBST_insert_20_10_remove_20_str (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10 ]', str(self.__tree))
    def test_coreBST_insert_20_10_remove_20_preOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10 ]', self.__tree.pre_order())
    def test_coreBST_insert_20_10_remove_20_postOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10 ]', self.__tree.post_order())
    def test_coreBST_insert_20_10_remove_20_toList (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual([10], self.__tree.to_list())
    def test_coreBST_insert_20_10_remove_20_exception (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.remove_element(20) 
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20) 
###
    def test_coreBST_insert_10_20_success (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)       
    def test_coreBST_insert_10_20_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_10_20_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.assertEqual('[ 10, 20 ]', str(self.__tree))
    def test_coreBST_insert_10_20_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.assertEqual('[ 10, 20 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_20_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.assertEqual('[ 20, 10 ]', self.__tree.post_order())
    def test_coreBST_insert_10_20_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.assertEqual([10,20], self.__tree.to_list())
#
    def test_coreBST_insert_10_20_remove_10_success (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)       
    def test_coreBST_insert_10_20_remove_10_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)   
        self.assertEqual(1, self.__tree.get_height())
    def test_coreBST_insert_10_20_remove_10_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)   
        self.assertEqual('[ 20 ]', str(self.__tree))
    def test_coreBST_insert_10_20_remove_10_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)   
        self.assertEqual('[ 20 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_20_remove_10_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)   
        self.assertEqual('[ 20 ]', self.__tree.post_order())
    def test_coreBST_insert_10_20_remove_10_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)   
        self.assertEqual([20], self.__tree.to_list())
    def test_coreBST_insert_10_20_remove_10_exception (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)   
        with self.assertRaises(ValueError):
            self.__tree.remove_element(10)
#
    def test_coreBST_insert_10_20_remove_20_success (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)       
    def test_coreBST_insert_10_20_remove_20_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)   
        self.assertEqual(1, self.__tree.get_height())
    def test_coreBST_insert_10_20_remove_20_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)   
        self.assertEqual('[ 10 ]', str(self.__tree))
    def test_coreBST_insert_10_20_remove_20_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)   
        self.assertEqual('[ 10 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_20_remove_20_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)   
        self.assertEqual('[ 10 ]', self.__tree.post_order())
    def test_coreBST_insert_10_20_remove_20_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)   
        self.assertEqual([10], self.__tree.to_list())
    def test_coreBST_insert_10_20_remove_20_exception (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)   
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20) 
###
    def test_coreBST_insert_10_20_30_success (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30) 

    def test_coreBST_insert_10_20_30_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_10_20_30_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30) 
        self.assertEqual('[ 10, 20, 30 ]', str(self.__tree))
    def test_coreBST_insert_10_20_30_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30) 
        self.assertEqual('[ 20, 10, 30 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_20_30_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30) 
        self.assertEqual('[ 10, 30, 20 ]', self.__tree.post_order())
    def test_coreBST_insert_10_20_30_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30) 
        self.assertEqual([10,20,30], self.__tree.to_list())
#
    def test_coreBST_insert_10_20_30_remove_10_success (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(10) 
    def test_coreBST_insert_10_20_30_remove_10_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(10) 
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_10_20_30_remove_10_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(10) 
        self.assertEqual('[ 20, 30 ]', str(self.__tree))
    def test_coreBST_insert_10_20_30_remove_10_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(10) 
        self.assertEqual('[ 20, 30 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_20_30_remove_10_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(10) 
        self.assertEqual('[ 30, 20 ]', self.__tree.post_order())
    def test_coreBST_insert_10_20_30_remove_10_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(10) 
        self.assertEqual([20,30], self.__tree.to_list())
    def test_coreBST_insert_10_20_30_remove_10_exception (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(10) 
        with self.assertRaises(ValueError):
            self.__tree.remove_element(10)
#
    def test_coreBST_insert_10_20_30_remove_20_success (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(20) 
    def test_coreBST_insert_10_20_30_remove_20_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(20) 
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_10_20_30_remove_20_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(20) 
        self.assertEqual('[ 10, 30 ]', str(self.__tree))
    def test_coreBST_insert_10_20_30_remove_20_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(20) 
        self.assertEqual('[ 30, 10 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_20_30_remove_20_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(20) 
        self.assertEqual('[ 10, 30 ]', self.__tree.post_order())
    def test_coreBST_insert_10_20_30_remove_20_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(20) 
        self.assertEqual([10,30], self.__tree.to_list())
    def test_coreBST_insert_10_20_30_remove_20_exception (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(30)
        self.__tree.remove_element(20) 
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
###
    def test_coreBST_insert_30_20_10_success (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)  
    def test_coreBST_insert_30_20_10_height (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_30_20_10_str (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 20, 30 ]', str(self.__tree))
    def test_coreBST_insert_30_20_10_preOrder (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.assertEqual('[ 20, 10, 30 ]', self.__tree.pre_order())
    def test_coreBST_insert_30_20_10_postOrder (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 30, 20 ]', self.__tree.post_order())
    def test_coreBST_insert_30_20_10_toList (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.assertEqual([10,20,30], self.__tree.to_list())
#
    def test_coreBST_insert_30_20_10_remove_30_success (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(30)  
    def test_coreBST_insert_30_20_10_remove_30_height (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(30)
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_30_20_10_remove_30_str (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(30)
        self.assertEqual('[ 10, 20 ]', str(self.__tree))
    def test_coreBST_insert_30_20_10_remove_30_preOrder (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(30)
        self.assertEqual('[ 20, 10 ]', self.__tree.pre_order())
    def test_coreBST_insert_30_20_10_remove_30_postOrder (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(30)
        self.assertEqual('[ 10, 20 ]', self.__tree.post_order())
    def test_coreBST_insert_30_20_10_remove_30_toList (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(30)
        self.assertEqual([10,20], self.__tree.to_list())
    def test_coreBST_insert_30_20_10_remove_30_exception (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(30)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(30)
###
    def test_coreBST_insert_30_20_10_remove_20_success (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)  
    def test_coreBST_insert_30_20_10_remove_20_height (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual(2, self.__tree.get_height())
    def test_coreBST_insert_30_20_10_remove_20_str (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 30 ]', str(self.__tree))
    def test_coreBST_insert_30_20_10_remove_20_preOrder (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 30, 10 ]', self.__tree.pre_order())
    def test_coreBST_insert_30_20_10_remove_20_postOrder (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 30 ]', self.__tree.post_order())
    def test_coreBST_insert_30_20_10_remove_20_toList (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        self.assertEqual([10,30], self.__tree.to_list())
    def test_coreBST_insert_30_20_10_remove_20_exception (self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)
###
    def test_coreBST_insert_fulllevel_2_success (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)    
    def test_coreBST_insert_fulllevel_2_heightAfterEachInsert (self):
        self.__tree.insert_element(20)
        self.assertEqual(1, self.__tree.get_height())
        self.__tree.insert_element(30)
        self.assertEqual(2, self.__tree.get_height())   
        self.__tree.insert_element(10)  
        self.assertEqual(2, self.__tree.get_height()) 
    def test_coreBST_insert_fulllevel_2_str (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)  
        self.assertEqual('[ 10, 20, 30 ]', str(self.__tree)) 
    def test_coreBST_insert_fulllevel_2_preOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)  
        self.assertEqual('[ 20, 10, 30 ]', self.__tree.pre_order()) 
    def test_coreBST_insert_fulllevel_2_postOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)  
        self.assertEqual('[ 10, 30, 20 ]', self.__tree.post_order()) 
    def test_coreBST_insert_fulllevel_2_toList (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)  
        self.assertEqual([10,20,30], self.__tree.to_list()) 
##
    def test_coreBST_insert_fulllevel_2_remove_root_success (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)    
    def test_coreBST_insert_fulllevel_2_remove_root_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)  
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)  
        self.assertEqual(2, self.__tree.get_height()) 
    def test_coreBST_insert_fulllevel_2_remove_root_str (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)  
        self.assertEqual('[ 10, 30 ]', str(self.__tree)) 
    def test_coreBST_insert_fulllevel_2_remove_root_preOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)  
        self.assertEqual('[ 30, 10 ]', self.__tree.pre_order()) 
    def test_coreBST_insert_fulllevel_2_remove_root_postOrder (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)  
        self.assertEqual('[ 10, 30 ]', self.__tree.post_order()) 
    def test_coreBST_insert_fulllevel_2_remove_root_toList (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)  
        self.assertEqual([10,30], self.__tree.to_list())
    def test_coreBST_insert_fulllevel_2_remove_root_exception (self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)   
        self.__tree.insert_element(10)
        self.__tree.remove_element(20)  
        with self.assertRaises(ValueError):
            self.__tree.remove_element(20)

###
    def test_coreBST_insert_fulllevel_3_success (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)  
    def test_coreBST_insert_fulllevel_3_heightAfterEachInsert (self):
        self.__tree.insert_element(50)
        self.assertEqual(1, self.__tree.get_height())
        self.__tree.insert_element(20)
        self.assertEqual(2, self.__tree.get_height())   
        self.__tree.insert_element(10)
        self.assertEqual(2, self.__tree.get_height())
        self.__tree.insert_element(30)
        self.assertEqual(3, self.__tree.get_height())
        self.__tree.insert_element(70)
        self.assertEqual(3, self.__tree.get_height())
        self.__tree.insert_element(60)
        self.assertEqual(3, self.__tree.get_height())
        self.__tree.insert_element(80)
        self.assertEqual(3, self.__tree.get_height())
    def test_coreBST_insert_fulllevel_3_str (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual('[ 10, 20, 30, 50, 60, 70, 80 ]', str(self.__tree))
    def test_coreBST_insert_fulllevel_3_preOrder (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual('[ 50, 20, 10, 30, 70, 60, 80 ]', self.__tree.pre_order())
    def test_coreBST_insert_fulllevel_3_postOrder (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual('[ 10, 30, 20, 60, 80, 70, 50 ]', self.__tree.post_order())
    def test_coreBST_insert_fulllevel_3_toList (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual([10,20,30,50,60,70,80], self.__tree.to_list())
    def test_coreBST_insert_fulllevel_3_toList_remove2 (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.remove_element(30)
        self.__tree.remove_element(50)
        self.assertEqual([10,20,60,70,80], self.__tree.to_list())
    def test_coreBST_insert_fulllevel_3_height_remove2 (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.remove_element(30)
        self.__tree.remove_element(50)
        self.assertEqual(3, self.__tree.get_height()) 
    def test_coreBST_insert_fulllevel_3_toList_remove3 (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.remove_element(20)
        self.__tree.remove_element(10)
        self.__tree.remove_element(30)
        self.assertEqual([50,60,70,80], self.__tree.to_list()) 
    def test_coreBST_insert_fulllevel_3_height_remove3 (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.remove_element(20)
        self.__tree.remove_element(10)
        self.__tree.remove_element(30)
        self.assertEqual(3, self.__tree.get_height()) 
    def test_coreBST_insert_fulllevel_3_toList_remove4 (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.remove_element(30)
        self.__tree.remove_element(50)
        self.__tree.remove_element(70)
        self.__tree.remove_element(80)
        self.assertEqual([10,20,60], self.__tree.to_list())   
    def test_coreBST_insert_fulllevel_3_height_remove4 (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.remove_element(30)
        self.__tree.remove_element(50)
        self.__tree.remove_element(70)
        self.__tree.remove_element(80)
        self.assertEqual(2, self.__tree.get_height())      

    def test_coreBST_insert_fulllevel_3_success_3Exception (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(60)
        self.__tree.insert_element(80) 

    def test_coreBST_insert_fulllevel_3_heightAfterEachInsert_3Exception (self):
        ## Note, these test are to ensure no data is changed
        self.__tree.insert_element(50)
        self.assertEqual(1, self.__tree.get_height())
        self.__tree.insert_element(20)
        self.assertEqual(2, self.__tree.get_height())   
        self.__tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(10)
        self.assertEqual(2, self.__tree.get_height())
        self.__tree.insert_element(30)
        self.assertEqual(3, self.__tree.get_height())
        self.__tree.insert_element(70)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(70)
        self.assertEqual(3, self.__tree.get_height())
        self.__tree.insert_element(60)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(60)
        self.assertEqual(3, self.__tree.get_height())
        self.__tree.insert_element(80)
        self.assertEqual(3, self.__tree.get_height())

    def test_coreBST_insert_fulllevel_3_str_3Exception (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual('[ 10, 20, 30, 50, 60, 70, 80 ]', str(self.__tree))

    def test_coreBST_insert_fulllevel_3_preOrder_3Exception (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual('[ 50, 20, 10, 30, 70, 60, 80 ]', self.__tree.pre_order())

    def test_coreBST_insert_fulllevel_3_postOrder_3Exception (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual('[ 10, 30, 20, 60, 80, 70, 50 ]', self.__tree.post_order())
        
    def test_coreBST_insert_fulllevel_3_toList_3Exception (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.assertEqual([10,20,30,50,60,70,80], self.__tree.to_list())

    def test_coreBST_insert_multipleException_success (self):
        # Check for exception for each value inserted
        self.__tree.insert_element(50)
        self.__tree.insert_element(20)   
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(20)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(30)     
        with self.assertRaises(ValueError):
            self.__tree.insert_element(50) 
        with self.assertRaises(ValueError):
            self.__tree.insert_element(60)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(70) 
        with self.assertRaises(ValueError):
            self.__tree.insert_element(80)     
###
    #####
    # Special cases. Testing for height and transversals
    #####
###
    def test_coreBST_insert_50_30_70_20_40_35_33_height (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.assertEqual(4, self.__tree.get_height())
    def test_coreBST_insert_50_30_70_20_40_35_33_str (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.assertEqual('[ 20, 30, 33, 35, 40, 50, 70 ]', str(self.__tree))
    def test_coreBST_insert_50_30_70_20_40_35_33_preOrder (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.assertEqual('[ 40, 30, 20, 35, 33, 50, 70 ]', self.__tree.pre_order())
    def test_coreBST_insert_50_30_70_20_40_35_33_postOrder (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.assertEqual('[ 20, 33, 35, 30, 70, 50, 40 ]', self.__tree.post_order())
    def test_coreBST_insert_50_30_70_20_40_35_33_toList (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.assertEqual([20,30,33,35,40,50,70], self.__tree.to_list())
#
    def test_coreBST_insert_50_30_70_20_40_35_33_remove_30_height (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.__tree.remove_element(30)
        self.assertEqual(3, self.__tree.get_height())
    def test_coreBST_insert_50_30_70_20_40_35_33_remove_30_str (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.__tree.remove_element(30)
        self.assertEqual('[ 20, 33, 35, 40, 50, 70 ]', str(self.__tree))
    def test_coreBST_insert_50_30_70_20_40_35_33_remove_30_preOrder (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.__tree.remove_element(30)
        self.assertEqual('[ 40, 33, 20, 35, 50, 70 ]', self.__tree.pre_order())
    def test_coreBST_insert_50_30_70_20_40_35_33_remove_30_postOrder (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.__tree.remove_element(30)
        self.assertEqual('[ 20, 35, 33, 70, 50, 40 ]', self.__tree.post_order())
    def test_coreBST_insert_50_30_70_20_40_35_33_remove_30_toList (self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(30)
        self.__tree.insert_element(70)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(35)
        self.__tree.insert_element(33)
        self.__tree.remove_element(30)
        self.assertEqual([20,33,35,40,50,70], self.__tree.to_list())
#
    def test_coreBST_insert_zigZag_1eft_8elements_height (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.assertEqual(4, self.__tree.get_height())     
    def test_coreBST_insert_zigZag_left_8elements_str (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.assertEqual('[ 50, 60, 70, 73, 75, 80, 90, 100 ]', str(self.__tree))
    def test_coreBST_insert_zigZag_left_8elements_preOrder (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.assertEqual('[ 80, 60, 50, 73, 70, 75, 90, 100 ]', self.__tree.pre_order())    
    def test_coreBST_insert_zigZag_left_8elements_postOrder (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)   
        self.assertEqual('[ 50, 70, 75, 73, 60, 100, 90, 80 ]', self.__tree.post_order())
    def test_coreBST_insert_zigZag_left_8elements_toList (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.assertEqual([50,60,70,73,75,80,90,100], self.__tree.to_list())
#
    def test_coreBST_insert_zigZag_1eft_8elements_1remove_height (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.__tree.remove_element(60)
        self.assertEqual(4, self.__tree.get_height())     
    def test_coreBST_insert_zigZag_left_8elements_1remove_str (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.__tree.remove_element(60)
        self.assertEqual('[ 50, 70, 73, 75, 80, 90, 100 ]', str(self.__tree))
    def test_coreBST_insert_zigZag_left_8elements_1remove_preOrder (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.__tree.remove_element(60)
        self.assertEqual('[ 80, 70, 50, 73, 75, 90, 100 ]', self.__tree.pre_order())    
    def test_coreBST_insert_zigZag_left_8elements_1remove_postOrder (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.__tree.remove_element(60)   
        self.assertEqual('[ 50, 75, 73, 70, 100, 90, 80 ]', self.__tree.post_order())
    def test_coreBST_insert_zigZag_left_8elements_1remove_toList (self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(90)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(70)
        self.__tree.insert_element(75)
        self.__tree.insert_element(73)
        self.__tree.remove_element(60)
        self.assertEqual([50,70,73,75,80,90,100], self.__tree.to_list())
#
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_70_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(70)
        self.assertEqual(4, self.__tree.get_height())
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_70_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(70)        
        self.assertEqual('[ 10, 40, 50, 60, 75, 80, 100 ]', str(self.__tree))
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_70_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(70)        
        self.assertEqual('[ 50, 40, 10, 75, 60, 80, 100 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_70_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(70)        
        self.assertEqual('[ 10, 40, 60, 100, 80, 75, 50 ]', self.__tree.post_order())        
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_70_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(70)               
        self.assertEqual([10,40,50,60,75,80,100], self.__tree.to_list())
#
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_50_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(50)
        self.assertEqual(4, self.__tree.get_height())
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_50_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(50)        
        self.assertEqual('[ 10, 40, 60, 70, 75, 80, 100 ]', str(self.__tree))
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_50_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(50)        
        self.assertEqual('[ 60, 40, 10, 80, 70, 75, 100 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_50_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(50)        
        self.assertEqual('[ 10, 40, 75, 70, 100, 80, 60 ]', self.__tree.post_order())        
    def test_coreBST_insert_10_50_40_100_70_60_80_75_remove_50_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(80)
        self.__tree.insert_element(75)
        self.__tree.remove_element(50)               
        self.assertEqual([10,40,60,70,75,80,100], self.__tree.to_list())
#
    def test_coreBST_insert_10_50_40_100_70_60_65_55_remove_40_height (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(55)
        self.__tree.remove_element(40)
        self.assertEqual(3, self.__tree.get_height())
    def test_coreBST_insert_10_50_40_100_70_60_80_65_remove_50_str (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(55)
        self.__tree.remove_element(40)      
        self.assertEqual('[ 10, 50, 55, 60, 65, 70, 100 ]', str(self.__tree))
    def test_coreBST_insert_10_50_40_100_70_60_80_65_remove_50_preOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(55)
        self.__tree.remove_element(40)       
        self.assertEqual('[ 60, 50, 10, 55, 70, 65, 100 ]', self.__tree.pre_order())
    def test_coreBST_insert_10_50_40_100_70_60_80_65_remove_50_postOrder (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(55)
        self.__tree.remove_element(40)     
        self.assertEqual('[ 10, 55, 50, 65, 100, 70, 60 ]', self.__tree.post_order())        
    def test_coreBST_insert_10_50_40_100_70_60_80_65_remove_50_toList (self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(55)
        self.__tree.remove_element(40)         
        self.assertEqual([10,50,55,60,65,70,100], self.__tree.to_list())
###




if __name__ == '__main__':
  unittest.main()

