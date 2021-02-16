import csv
from math import ceil
import tkinter
from tkinter.filedialog import askopenfilename
import os.path

root = tkinter.Tk()
fname = askopenfilename()
root.destroy()

def nearlyInt(a):
    __EPS = 0.02
    return abs(round(a) - a ) < __EPS
qs = []
vals = []

with open(fname, newline='') as csvFile:
    reader = csv.reader(csvFile, dialect='excel')
    for row in reader:
        qs.append(str(row[0]))
        vals.append(int(row[1]))
    
valsUnique = set(vals)
totalMarks = sum(vals)
# assert 100 % totalMarks == 0, "This will only work if the total number of marks divides 100"
percentPerMark = 100.0 / totalMarks
weights = set()

for val in valsUnique:
    for i in range(val+1):
        weight = i*100/val # This is correct
        weight = ceil(10*weight)/10.0 #Tricky hack to round (up) to 1 dp
        weights.add(weight)
weights = list(weights)
weights.sort()

inFilePath, inFileName = os.path.split(fname)
outFileName = os.path.splitext(inFileName)[0] +"_Rubric.csv"
outFilePath = os.path.join(inFilePath, outFileName)
outFile = open(outFilePath, "w+", newline='')
writer = csv.writer(outFile, quoting=csv.QUOTE_ALL)
writer.writerow(["For the best editing experience, upload this .csv as a rubric in Microsoft Teams."])
writer.writerow([])
writer.writerow(["Title", totalMarks])
writer.writerow(["Description"])
writer.writerow([])
writer.writerow([""]+[*sum(zip(["w"]*len(weights), list(weights)), ())])
weightOfQList = []
for q, val in zip(qs, vals):
    rowToWrite = [q]
    if 100 % totalMarks == 0:
        weightOfQ = int(val*percentPerMark)
    else:
        weightOfQ = round(val*percentPerMark, 2)
    weightOfQList.append(weightOfQ)
    pmQ = percentPerMark*val*0.01
    for weight in weights: #Start iteration from second element because Teams
        # Get calculated mark (could do it in a more clever way(by just looking at the weight), 
        # but I think doing this dumb way might expose errors
        calcMark = pmQ*weight/ percentPerMark
        if nearlyInt(calcMark):
            rowToWrite.append('%d Marks'% (int(round(calcMark))))
        else:
            rowToWrite.append("N/A")
        rowToWrite.append("")
    writer.writerow(rowToWrite)
    writer.writerow([weightOfQ])
#assert sum(weightOfQList) == 100, "Total Weights don't add to 100"
outFile.close()