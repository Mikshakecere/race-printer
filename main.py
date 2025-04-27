import pip._vendor.requests as requests

# link to request info
url = "https://data.ninjakiwi.com/btd6/ct/"

ct_resp = requests.get(url).json()

if ct_resp['error'] is not None or ct_resp['success'] is False:
    print("Races category unavailable at the moment")
    exit()

ct_id = input("Input the ct id or type 0 to fetch the latest ct: ")

if ct_id == '0':
    # fetch the latest ct id (i forgor how)
    ct_id = ct_resp['body'][0]['id']

print(ct_id)

ct = url + ct_id + "/tiles"
ct_resp = requests.get(ct).json()
tiles = ct_resp['body']['tiles']
banners = []
relics = []
regular = []

for tile in tiles:
    if tile['gameType'] == "Race":
        if tile['type'] == "Regular":
            regular.append(tile['id'])
        elif tile['type'] == "Banner":
            banners.append(tile['id'])
        else:
            relics.append(tile['id'])

print("Regular Tiles:")
print("Counted " + str(len(regular)) + " tiles")
print(regular)
print("Banner Tiles:")
print("Counted " + str(len(banners)) + " tiles")
print(banners)
print("Relic Tiles:")
print("Counted " + str(len(relics)) + " tiles")
print(relics)