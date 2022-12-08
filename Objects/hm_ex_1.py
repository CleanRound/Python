try:

    class Automobile:
        Model = ''
        Company = ''
        Color = ''
        Engine = ''
        Transmission = ''
        Doors = ''
        Height = ''
        Width = ''
        Length = ''

        def __init__(self):
            self.Model = 'Model = 911 Carrera 4 GTS PDK 2022'
            self.Company = 'Company = Porsche'
            self.Color = 'Color = Gentian Blue Metallic'
            self.Engine = 'Engine = Gasoline - 3.0 l \\ 480 hp \\ 9.2 l per 100 km'
            self.Transmission = 'Transmission = Automatic'
            self.Doors = 'Doors = 2'
            self.Height = 'Height = 1300 mm'
            self.Width = 'Width = 1852 mm'
            self.Length = 'Length = 4519 mm'

        def show_on(self):
            print('---------------------------------------------------------')
            print(self.Model)
            print(self.Company)
            print(self.Color)
            print(self.Engine)
            print(self.Transmission)
            print(self.Doors)
            print(self.Height)
            print(self.Width)
            print(self.Length)
            print('---------------------------------------------------------')

        def __del__(self):
            print("Object 'Automobile' has been deleted")

    if __name__ == '__main__':
        automobile = Automobile()
        automobile.show_on()

except Exception as err:
    print(f'Error: {err}')
