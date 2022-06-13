import xml.etree.ElementTree as et


tree = et.parse('./test.xml')
root = tree.getroot()

for node in root.findall('hosts'):
    print(node.tag, node.text)
    tmp_node = 'host2'
    node.tag = tmp_node
    print(node.tag, node.text)
tree.write('test_alter_result.xml')








