
import csv

csvFile = 'roadmap.csv'
xmlFile = 'roadmap.xml'
teams = {}
releases = {}
features = {}


csvData = csv.reader(open(csvFile, 'rU'), dialect='excel')
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<roadmap>' + "\n")

rowNum = 0
for row in csvData:

    if rowNum != 0:
        feature = [row[0], row[8], row[9], row[1]]
        # if team doesn't exist, create a dict of releases
        if row[3] not in teams:
            teams[row[3]] = {}
        # row[9] is date row[8] is release name
        release = (row[8], row[9])
        if release not in teams[row[3]]:
            teams[row[3]][release] = []
        teams[row[3]][release].append(feature)
        
    rowNum +=1
#loop through teams
for k in teams.keys():
    xmlData.write('\t<team name="' + k + '">\n')
    for release in teams[k].keys():
        xmlData.write('\t\t<release name="'+release[1]+'" date="'+release[0]+'">\n') 
        features = teams[k][release]
        for feature in features:
            xmlData.write('\t\t\t<feature tags="'+feature[3]+'">'+feature[0]+'</feature>\n')
        xmlData.write('\t\t</release>\n')
    xmlData.write('\t</team>\n')
xmlData.write('</roadmap>\n')
            

xmlData.close()
