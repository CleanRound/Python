circle_diameter = int(input("Enter the circle diameter value: "))
choice = int(input("Enter 1 for the area.\nEnter 2 for the perimeter:\n"))

if choice == 1:
    radius = (circle_diameter // 2)
    squared = (radius * radius)
    print(f' The area of a circle is {squared * 3.14} square centimeters')
elif choice == 2:
    perimeter = (circle_diameter * 3.14)
    print('The perimeter of a circle is %.2f'
          %(perimeter))
else:
    print(f' Error, something is wrong with your choice')
