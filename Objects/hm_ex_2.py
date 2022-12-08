try:

    class ParcelLocker:
        Company = ''
        Color = ''
        Allowed_Dimensions = ''
        Allowed_Weight = ''
        Declared_Value = ''
        Tariffs_Documents = ''
        Tariffs_Parcels = ''
        Fees = ''

        def __init__(self):
            self.Company = 'Company = Nova Poshta'
            self.Color = 'Color = Red, Black or Metallic'
            self.Allowed_Dimensions = 'Allowed Dimensions of a parcel = No more than 40x60x30 cm'
            self.Allowed_Weight = 'Allowed Weight of a parcel = No more than 20 kg'
            self.Declared_Value = 'Declared value of a parcel = No more than 10,000 UAH'
            self.Tariffs_Documents = 'Tariff for shipping documents = 45 UAH for sending the parcel to parcel locker ' \
                                     'or to post office \\ Delivery to address - +30 UAH per unit.'
            self.Tariffs_Parcels = 'Tariff for shipping parcels = 60 UAH for sending the parcel to parcel locker ' \
                                     'or to post office \\ Delivery to address - +30 UAH per unit.'
            self.Fees = 'Fees = Up to 500 uah is included in the tariff, over 500 UAH: 0,5 %. The maximum declared ' \
                        'value = 10,000 UAH'

        def show_on(self):
            print('--------------------------------------------------------------------------------------------------'
                  '---------------------------------------------')
            print(self.Company)
            print(self.Color)
            print(self.Allowed_Dimensions)
            print(self.Allowed_Weight)
            print(self.Declared_Value)
            print(self.Tariffs_Documents)
            print(self.Tariffs_Parcels)
            print(self.Fees)
            print('--------------------------------------------------------------------------------------------------'
                  '---------------------------------------------')

        def __del__(self):
            print("Object 'ParcelLocker' has been deleted")

    if __name__ == '__main__':
        parcel_locker = ParcelLocker()
        parcel_locker.show_on()

except Exception as err:
    print(f'Error: {err}')
