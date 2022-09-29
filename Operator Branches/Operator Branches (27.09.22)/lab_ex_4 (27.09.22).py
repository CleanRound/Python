file_size = int(input("Enter the file size: "))
internet_speed = int(input("Enter the internet speed: "))
choice = int(input("Enter 1 to see how much time left to download file in seconds.\nEnter 2 to see how much time"
                   "left to download file in minutes.\nEnter 3 to see how much time left to download file in "
                   "hours:\n"))
megabyte = (file_size * 1024)
seconds = ((megabyte * 1024 * 1024 * 8) / internet_speed)
minutes = (seconds / 60)
hours = (seconds / 3600)

if choice == 1:
    print('The time left in seconds is %.d'
          %(seconds))
elif choice == 2:
    print('The time left in minutes is %.d'
          %(minutes))
elif choice == 3:
    print('The time left in hours is %.d'
          %(hours))
else:
    print(f' Error, something is wrong with your choice')
