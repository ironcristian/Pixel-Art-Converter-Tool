import requests

headers = {
    "User-Agent": "BlockImage/1.0 (block project)"
}

r = requests.get(
    "https://crystalrealms.wiki.gg/wiki/Blocks",
    headers=headers
)

print(r.status_code)
print(r.text[:100])