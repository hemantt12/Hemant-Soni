fruitsDict = {
  'Apple': 100,
  'Orange': 200,
  'Banana': 400,
  'pomegranate':600
}
 
print('min value key = ',min(fruitsDict, key=fruitsDict.get))
print('max value key =',max(fruitsDict,key=fruitsDict.get))
