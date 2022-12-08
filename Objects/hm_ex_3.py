try:

    class Phone:
        Model = ''
        Company = ''
        Color = ''
        Capacity = ''
        SIM_Cards = ''
        Display = ''
        CPU = ''
        RAM = ''
        Main_Camera = ''
        Front_Camera  = ''
        Battery_Capacity = ''
        Dimensions = ''
        Weight = ''
        Operating_System = ''

        def __init__(self):
            self.Model = 'Model = Galaxy S21 Ultra'
            self.Company = 'Company = Samsung'
            self.Color = 'Color = Phantom Black'
            self.Capacity = 'Memory Capacity = 256 Gb'
            self.SIM_Cards = 'SIM-Cards = 2'
            self.Display = 'Display = 3200x1440 / Dynamic AMOLED / 120 Hz / 6.8"'
            self.CPU = 'CPU = Samsung Exynos 2100'
            self.RAM = 'RAM = 12 Gb'
            self.Main_Camera = 'Main Camera = 108 MP + 12 MP + 10 MP + 10 MP'
            self.Front_Camera = 'Front Camera = 40 MP'
            self.Battery_Capacity = 'Battery Capacity = 5000 mAh'
            self.Dimensions = 'Dimensions = 165.1 x 75.6 x 8.9 mm'
            self.Weight = 'Weight = 229 g'
            self.Operating_System = 'Operating System = Android 11.0'

        def show_on(self):
            print('----------------------------------------------------------')
            print(self.Model)
            print(self.Company)
            print(self.Color)
            print(self.SIM_Cards)
            print(self.Display)
            print(self.CPU)
            print(self.RAM)
            print(self.Main_Camera)
            print(self.Front_Camera)
            print(self.Battery_Capacity)
            print(self.Dimensions)
            print(self.Weight)
            print(self.Operating_System)
            print('----------------------------------------------------------')

        def __del__(self):
            print("Object 'Phone' has been deleted")

    if __name__ == '__main__':
        phone = Phone()
        phone.show_on()

except Exception as err:
    print(f'Error: {err}')
