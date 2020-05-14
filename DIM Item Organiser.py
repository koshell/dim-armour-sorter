#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Destiny 2 'God Roll' Organiser

Parses a given accounts inventory and sort 'god roll' items.
"""

__author__ = "Matthew Koschel"
__contact__ = "zone1135@gmail.com"

# Standard library imports
import csv

if __name__ == "__main__":
    print()
    print('DIM armour sorter/tagger thingy')
    print()
    print('This program sorts through an exported DIM armour excel file.')
    print('It sums three stats of your choosing and then marks any items that surpasses the two thresholds given.')
    print('The first threshold is for items that are considered good enough to keep. It is recommended to set this to 35.')
    print('The second threshold is if the item is worthy of being masterworked. It is recommended to set this to 40.')
    print('Items that pass the first threshold will be tagged as "keep", items that pass the second will be tagged as "infuse".')
    print('Itmes that pass neither will be tagged as "junk".')
    print()
    print('Now select the three stats you would like to use for the calculation:')
    print('Type "1" for Mobility')
    print('Type "2" for Resilience')
    print('Type "3" for Recovery')
    print('Type "4" for Discipline')
    print('Type "5" for Intellect')
    print('Type "6" for Strength')
    
    print()
    
    x1 = input('Please enter the first stat: ')
    x2 = input('Please enter the second stat: ')
    x3 = input('Please enter the third stat: ')
    print()
    thresholdL = input('Now please enter the first threshold: ')
    thresholdH = input('Now please enter the second threshold: ')
    print()
    print('Thankyou, processing now...')

    stats = {
        '1' : 'Mobility (Base)',
        '2' : 'Resilience (Base)',
        '3' : 'Recovery (Base)',
        '4' : 'Discipline (Base)',
        '5' : 'Intellect (Base)',
        '6' : 'Strength (Base)'
    }

    with open('destinyArmor.csv') as destinyArmor:
        with open('destinyArmorUpdated.csv', 'w', newline='') as destinyArmorUpdated:
            destinyArmorDict = csv.DictReader(destinyArmor, delimiter=',')
            updatedDestinyArmorDict = csv.DictWriter(destinyArmorUpdated, fieldnames=destinyArmorDict.fieldnames)
            updatedDestinyArmorDict.writeheader()
            for row in destinyArmorDict:

                tempDict = row.copy()

                if int(row[stats[x1]]) + int(row[stats[x2]]) + int(row[stats[x3]]) >= int(thresholdH):
                        tempDict['Tag'] = 'infuse'
                        updatedDestinyArmorDict.writerow(tempDict)
                elif row['Type'] != 'Warlock Bond' and row['Type'] != 'Hunter Cloak' and row['Type'] != 'Titan Mark':
                    if int(row[stats[x1]]) + int(row[stats[x2]]) + int(row[stats[x3]]) >= int(thresholdL):
                        tempDict['Tag'] = 'keep'
                        updatedDestinyArmorDict.writerow(tempDict)
                    else:
                        tempDict['Tag'] = 'junk'
                        updatedDestinyArmorDict.writerow(tempDict)

    print()
    input('Processing completed, press any key to exit...')