import pandas as pd
from collections import OrderedDict, defaultdict

if __name__ == '__main__':
    dd = defaultdict(list)
    hero = pd.read_csv("./hero.csv")
    hero_map = hero.to_dict('records', into=dd)

    dd2 = defaultdict(list)
    en_hero = pd.read_csv("./en_hero.csv")
    name_map = en_hero.to_dict('records', into=dd2)

    for row in hero_map:
        for name in name_map:
            if row['en_name'].lower() == name['en_name'].lower():
                row['en_title2'] = name['en_title'].strip()
                break

    export_csv = pd.DataFrame(hero_map).to_csv(r'./ff.csv', index=None, header=True,
                                               encoding='utf-8-sig')
