import requests

def give_all_info(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    res = requests.get(url=url)
    all_about = {}
    definitions = ""
    json = res.json()

    if res.status_code == 200:
        for i in json:
            for j in i['meanings']:
                definitions += f"\n🫴🫴🫴 {j['partOfSpeech']}\n\n"
                for k in j['definitions']:
                    definitions += f"👉 {k['definition']}\n"
        all_about['definitions'] = definitions

        for i in json:
            for j in i['phonetics']:
                if j.get('audio') and (j['audio'][-6:] == 'uk.mp3' or j['audio'][-6:] == 'us.mp3'):
                    all_about['audio'] = j['audio']
                    return all_about
        return all_about
    else:
        return 'Sorry'




