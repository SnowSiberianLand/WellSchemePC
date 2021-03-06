import unittest
import document_worker
from well_worker import Well, ManyOfWell
from collections import OrderedDict


class MyTestCase(unittest.TestCase):
    def test_read_spacer(self):
        soult = document_worker.xmldocker('test_case.xml')
        res = soult.xml_read()
        flx = document_worker.xmldocker('default_xml.xml')
        flx_res = flx.xml_read()
        self.assertEqual(res, flx_res)
        soult.xml_write()
        s = open('test_case.xml', 'r')
        s1 = open('default_xml.xml', 'r')
        self.assertEqual(s.read() ,s1.read())
        s.close(), s1.close()

    def testManyWell(self):
        w = Well()
        m = ManyOfWell()
        m.add_well(w)
        print (m)
        m.remove_well(w)
        print (m)
        # self.assertEqual(m, OrderedDict())



if __name__ == '__main__':
    unittest.main()
