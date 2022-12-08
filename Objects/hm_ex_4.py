try:

    class MusicalInstrument:
        Type = ''
        Model = ''
        Company = ''
        Color = ''
        Strings = ''
        Frets = ''
        Body = ''
        Neck = ''
        Fretboard = ''
        Neck_Mount_Type = ''
        Scale = ''
        Neck_Width = ''
        Pickups = ''
        Regulators = ''
        Bridge = ''

        def __init__(self):
            self.Type = 'Type = Electric Guitar'
            self.Model = 'Model = RGA742FM TGF'
            self.Company = 'Company = Ibanez'
            self.Color = 'Color = Transparent Gray Flat'
            self.Strings = 'Number of strings = 7'
            self.Frets = 'Number of frets = 24'
            self.Body = 'Body = Meranti with flamed maple top'
            self.Neck = 'Neck = Maple'
            self.Fretboard = 'Fretboard = Jatoba'
            self.Neck_Mount_Type = 'Neck mount type = Bolt-on'
            self.Scale = 'Scale = 648 mm'
            self.Neck_Width = 'Width of the neck at the nut = 48 mm'
            self.Pickups = 'Pickups = 2 x Quantum-7 (H) Passive/Ceramic'
            self.Regulators = 'Regulators = Volume - 1 / Timbre - 1'
            self.Bridge = 'Bridge = F107'

        def show_on(self):
            print('----------------------------------------------')
            print(self.Type)
            print(self.Model)
            print(self.Company)
            print(self.Color)
            print(self.Strings)
            print(self.Frets)
            print(self.Body)
            print(self.Neck)
            print(self.Fretboard)
            print(self.Neck_Mount_Type)
            print(self.Scale)
            print(self.Neck_Width)
            print(self.Pickups)
            print(self.Regulators)
            print(self.Bridge)
            print('----------------------------------------------')

        def __del__(self):
            print("Object 'MusicalInstrument' has been deleted")

    if __name__ == '__main__':
        musical_instrument = MusicalInstrument()
        musical_instrument.show_on()

except Exception as err:
    print(f'Error: {err}')
