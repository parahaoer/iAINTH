import os
from ModifyFileContent import ModifyFileContent

ruleDir = './procedures/'

id = 46
ruleList = os.listdir(ruleDir)
for file in ruleList:
    filepath = ruleDir + file
    modifyFileData(filepath, id)
    id = id + 1

