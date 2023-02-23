import xml.etree.ElementTree as ET

tree = ET.parse('countries.xml')
#print(tree)

root = tree.getroot()
#print(root)

# for element in root:
#     print(element)
#     print(element.tag)
#     print(element.text)
#     print(element.attrib)
#     print(f"{element.tail!r}")
#     print()

#print(root[0].attrib)

# for element in root.iter('year'):
#     print(element)
#     print(element.tag)
#     print(element.text)
#     print(element.attrib)
#     print()


# element = root.find('.//year')
# print(element.text)
#
# elements = root.findall('.//year')
# print(elements)
# print([e.text for e in elements])
#
# print(root[0].get('name'))


# root[0].set('name', 'Ukraine')
# root[0][0].text = 1111
#
#
# for element in root.iter('rank'):
#     print(element.tag)
#     print(element.text)
#     print(element.attrib)
#
#     print()

first_country = root[0]
root.remove(first_country)
# for element in root:
#     print(element.attrib)
#     print()

ET.SubElement(root, 'continent', {'name': 'Africa'})
# for element in root:
#     print(element.attrib)
#     print()

new_element = ET.Element('continent', {'name': 'Antarctida'})
new_element.text = "AHDJKADHAFJKDH"

root.append(new_element)
for element in root:
    print(element.attrib)
    print(element.text)
    print()


tree.write('output.xml')



xml_as_string = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

root = ET.fromstringlist(xml_as_string)
print(root)

# new_tree = ET.ElementTree(root)
# new_tree.write('another_output.xml')