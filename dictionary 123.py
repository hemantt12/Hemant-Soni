animaldict = {
  "name": "Dog",
  "age":5,
  "Weight": 4,
  "Country": "US",
  "City":"California"
   
}
 
 
outDict = {key: animaldict[key] for key in animaldict.keys()-  ["name", "age"]}
print(outDict)
