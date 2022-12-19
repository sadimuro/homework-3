class Country:
    def __init__(self, name, area, population):
        self.name = name
        self.area = area
        self.population = population


    def __str__(self):
        return f'{self.name} {self.area}'

class City:
    def city(self):
        print('city')

class Economy:
    def economy(self):
        print('economy')


class Culture:
    def __init__(self, traditions, flag, sports):
        self.traditions = traditions
        self.flag = flag
        self.sports = sports
    def __str__(self):
        return  f'national traditions: {self.traditions} \n'\
                f'national flag: {self.flag}\n'\
                f'popular sports: {self.sports}\n'


class Education:
    def education(self):
        print('education')

class My_country(Country,City,Economy,Culture,Education):
    def __init__(self, name, area, population, traditions, flag, sports):
        Country.__init__(self,name, area, population)
        Culture.__init__(self, traditions, flag, sports)


    def __str__(self):
        return f'{self.name} {self.area} {self.population} {self.traditions} {self.flag} {self.sports}'


human = My_country('Kyrgyzstan', '199.9', '7 000 000','komuz','own flag', 'wrestling')
human.city()
print(human)
# 'Osh', 'progress',