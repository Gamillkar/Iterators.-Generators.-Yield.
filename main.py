import json

class Cauntry_and_URL:

    def __init__(self):
        self.open_file()
        score = 0
        self.score = score
        name_URL = []
        self.name_URL = name_URL

    def open_file(self):
        with open('countries.json', 'r', encoding='utf-8') as file:
            self.countries_all_data = json.load(file)
            self.account = len(self.countries_all_data)

    def __iter__(self):
        return self

    def __next__(self):

        if self.account > self.score:
            name_dirty_cauntry = self.countries_all_data[self.score]
            name_cauntry = name_dirty_cauntry['name']['common'].replace(' ', '_')
            self.score += 1
            name_cauntry_URL = {name_cauntry: f'https://en.wikipedia.org/wiki/{name_cauntry}'}
            self.name_URL.append(name_cauntry_URL)
            return name_cauntry_URL
        else:
            self.save_in_file(self.name_URL)
            raise StopIteration('Конец итерации')




    def save_in_file(self, data):
        with open('way_file/country_url.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

data_cauntry = Cauntry_and_URL()

for num in data_cauntry:
    print(f'{num}\n')

