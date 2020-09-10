import json


packageData = json.load(open('../package.json'))
templateFolder = packageData['flaskConfig']['templatePath']
staticFolder = packageData['flaskConfig']['staticPath']
