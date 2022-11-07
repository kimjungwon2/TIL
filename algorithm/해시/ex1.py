hashDict = {'ftp': 21, 'ssh': 22, 'stmp': 25, 'http': 80}

print(hashDict.keys())
print(hashDict.values())
print(hashDict.items())
print(hashDict.get('ftps'))

del hashDict['stmp']
print(hashDict)

hass = list(hashDict.keys())
print(hass)


hashDict.setdefault('e')
print(hashDict)

hashDict.setdefault('fg', 50)
print(hashDict)

hashDict.update(ftp=50,g=30)
print(hashDict)

print("ftp" in hashDict)
print("철수" in hashDict)

hashDict.clear()
print(hashDict)