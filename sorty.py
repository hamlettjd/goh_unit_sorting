import os

print('--------------' + os.getlogin() + " starting sorty.py ---------------")

fileobj = open("./scn_files/americaaa/campaign.scn", "r")

Lines = fileobj.readlines()
numSquads = -4 # negative 4 to account for BS Lines
squadFound = False

campaignLine = "{CampaignSquads"
for row in Lines:
    # print("Line{}: {}".format(count, row.strip()))
    if row.find(campaignLine) != -1:
        startingLine = Lines.index(row) + 2 # adding 2 to account for starting at 0 and line after this is actual first squad
        print('campaign squads on line: ', Lines.index(row))
        squadFound = True
        
    if squadFound == True:
        numSquads = numSquads + 1

print ('starting Line: ', startingLine)
print ('numSquads: ', numSquads)
endingLine = startingLine + numSquads
print ('ending line: ', endingLine)
