import xmltodict
import os


class xmldocker:
    def __init__(self, path):
        self.path = path
        self.xml_dict = None

    def xml_read(self):
        """ if file not found - return default xml dict"""
        if os.path.isfile(self.path):
            with open(self.path, 'r') as xfile:
                self.xml_dict = xmltodict.parse(xfile.read())
            return self.xml_dict
        else:
            return self.create_if_clear()

    def create_if_clear(self):
        with open(self.path, 'w') as xfile:
            xml_default = open("default_xml.xml", 'r').read()
            xfile.write(xml_default)
        return True

    def xml_write(self):
        """write file if was changed"""
        with open(self.path, 'r') as xfile:
            if xmltodict.parse(xfile.read()) != self.xml_dict:
                xmltodict.unparse(self.xml_dict, output=open(self.path, 'w'))
            else:
                print("File not changing...")
        return True

if __name__ == '__main__':
    c = xmldocker('test_case.xml')