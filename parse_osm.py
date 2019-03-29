# -*- coding: utf-8 -*-
import csv
import sys

from imposm.parser import OSMParser


class AddressExtractor:
    def __init__(self, csv_file):
        self.writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self.num_addresses = 0
        self.writer.writerow(
            ['geometry', 'country', 'city', 'pc', 'street', 'house_number'])

    @staticmethod
    def extract(tags, key):
        value = tags[key] if key in tags else ''
        return value.encode('utf-8')

    def extract_nodes(self, nodes):
        for osmid, tags, refs in nodes:
            if 'addr:city' in tags and 'addr:postcode' in tags and 'addr:street' in tags and \
                    'addr:housenumber' in tags and 'addr:country' in tags:
                self.num_addresses += 1
                country = self.extract(tags, 'addr:country')
                city = self.extract(tags, 'addr:city')
                pc = self.extract(tags, 'addr:postcode')
                street = self.extract(tags, 'addr:street')
                house_number = self.extract(tags, 'addr:housenumber')
                geom = 'SRID=4326;POINT(%s %s)' % (refs[0], refs[1])
                self.writer.writerow(
                    [geom, country, city, pc, street, house_number])
                print self.num_addresses


def main(input_file):
    with open('out-all.csv', 'wb') as csv_file:
        counter = AddressExtractor(csv_file)
        p = OSMParser(concurrency=8, nodes_callback=counter.extract_nodes)
        p.parse(input_file)
        print('Found %i addresses.' % counter.num_addresses)


if __name__ == '__main__':
    main(sys.argv[1])
