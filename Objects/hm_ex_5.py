try:

    class Profession:
        Type = ''
        Company = ''
        Salary = ''
        Insurances = ''
        Sick_Days = ''
        Degrees = ''
        License = ''
        State_Bar = ''
        Experience = ''
        Skills = ''
        Benefits = ''

        def __init__(self):
            self.Type = 'Job Type = Attorney'
            self.Company = 'Company = Stiner & Sons'
            self.Salary = 'Salary = $109,000 - $163,000'
            self.Insurances = 'Insurances = Health, dental, vision'
            self.Sick_Days = 'Sick Days = Unlimited sick days'
            self.Degrees = "Required degrees = Bachelor's and Juris Doctorate "
            self.License = 'Required license = License to practice law in N.M.'
            self.State_Bar = 'State Bar = Active member in good standing with N.M. State Bar'
            self.Experience = 'Experience = Minimum 3 years of criminal trial experience'
            self.Skills = 'Required skills = Intermediate experience with Microsoft Word, Excel, and PowerPoint & ' \
                          'Organized with excellent time-management skills'
            self.Benefits = 'Benefits = Parental leave & Gym membership'

        def show_on(self):
            print('--------------------------------------------------------------------------------------------------'
                  '----------------------------------------')
            print(self.Type)
            print(self.Company)
            print(self.Salary)
            print(self.Insurances)
            print(self.Sick_Days)
            print(self.Degrees)
            print(self.License)
            print(self.Experience)
            print(self.Skills)
            print(self.Benefits)
            print('--------------------------------------------------------------------------------------------------'
                  '----------------------------------------')

        def __del__(self):
            print("Object 'Profession' has been deleted")

    if __name__ == '__main__':
        profession = Profession()
        profession.show_on()

except Exception as err:
    print(f'Error: {err}')
