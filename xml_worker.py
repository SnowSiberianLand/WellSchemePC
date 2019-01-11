import xmltodict
import os


def xml_read(path):
    """ if file not found - return FileNotFoundError"""
    if os.path.isfile(path):
        with open(path, 'r') as xfile:
            dictionary_xml = xmltodict.parse(xfile.read())
            return dictionary_xml
    else:
        raise FileNotFoundError


def xml_write(temp_dict, path):
    with open(path, 'r') as xfile:
        if xmltodict.parse(xfile.read()) != temp_dict:
            xmltodict.unparse(temp_dict, output=open(path+'1', 'w'))
        else:
            print("File not changing...")
            return True


def create_if_clear(path):
    with open(path, 'w') as xfile:
        xml_default = open("default_xml.xml", 'r').read()
        xfile.write(xml_default)
    return True


if __name__ == '__main__':
    # create_if_clear("E://first_try.xml")
    a = xml_read("default_xml.xml")

    for item in a['WellSchemeData']['Tags']['Tag']['Group']['Wells']['Well'][0].items():
        print (item)
    # print ([item for item in a['WellSchemeData']['Tags']['Tag']['Group']['Wells'].items()], sep="\n")
    # a = xml_write(a, "E:\qtQuick\well_1_3.xml")
    if a:
        print("Ok")
