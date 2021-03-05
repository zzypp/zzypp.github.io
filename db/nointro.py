import xml.etree.ElementTree as ET
import os

file = open('nointro.txt', 'w')

print('Dumping data...')
for filename in os.listdir('nointro'):
    tree = ET.parse('nointro/' + filename)
    root = tree.getroot()
    for game in root:
        if game.find('rom') is not None:
            file.write('"' + game.get('name').replace('＆', '&') + '"\n')
            for scan in game:
                if scan.get('md5') is not None:
                    file.write(scan.get('md5') + '\n')
print('Done!')
