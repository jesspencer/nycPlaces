
nycPlaces = {'TimesSq': 'uptown', 'Brookyln Bridge': 'downtown', 'Astoria': 'uptown', 'Harlem':'uptown'}
while True:
    print('Enter a nyc place: (Blank to quit)')
    name = input()
    if name == ' ':
        break
    if name in nycPlaces:
        print(nycPlaces[name] + ' this is  ' + name)
    else:
        print('is it uptown or downtown?')
        location = input()
        nycPlaces[name] = location
        print('nycPlaces database updated.')
