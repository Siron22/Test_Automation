import xml.etree.ElementTree as ET
import json


with open('pages.xml', 'r') as f:
    pages = f.read()

root = ET.fromstringlist(pages)

page_list = {}

for page in root.iter('page'):
    page_name = page.attrib['name']
    element_list = {}
    for element in page.iter('element'):
        element_name = element.attrib['name']
        platform_list = {}
        for locator in element.iter('locator'):
            platform = locator.attrib['platform']
            locator_type = locator.attrib['locator_type']
            locator_value = locator.text
            locator_block = [locator_type, locator_value]
            platform_list[platform] = locator_block
        element_list[element_name] = platform_list
    page_list[page_name] = element_list


print(page_list)

json_pages = json.dumps(page_list)

print(json_pages)

with open('my_json_data.json', 'w') as f:
    json.dump(page_list, f, indent=4, separators=(". ", " = "))



