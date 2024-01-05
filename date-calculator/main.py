# Made by Mikus

import datetime
from sys import argv

def main():
	if len(argv) != 3:
		print("Bad number of arguments"), exit(-1)

	if argv[1] == "today":
		date1 = str(datetime.date.today()).split('-')
		date1.reverse()
	else:
		date1 = argv[1].split('/')

	if argv[2] == "today":
		date2 = str(datetime.date.today()).split('-')
		date2.reverse()
	else:
		date2 = argv[2].split('/')

	if len(date1) > 3 or len(date2) > 3:
		print("Argument not a date"), exit (-1)

	for i in range(0, len(date1)):
		if not date1[i].isdigit():
			print("Bad argument format")
			exit (0)

	for i in range(0, len(date2)):
		if not date2[i].isdigit():
			print("Bad argument format")
			exit (0)

	date1 = datetime.date(int(date1[2]), int(date1[1]), int(date1[0]))
	date2 = datetime.date(int(date2[2]), int(date2[1]), int(date2[0]))

	delta = date1 - date2

	if argv[1] != "today" and argv[2] != "today":
		if date1 < date2:
			print(f"{argv[1]} is {int(delta.days) * -1} days before {argv[2]}")
		elif date1 > date2:
			print(f"{argv[1]} is {int(delta.days)} days after {argv[2]}")
		else:
			print("Those are the same dates!")
	else:
		if date1 < date2:
			print(f"That date will be in {int(delta.days) * -1} days")
		elif date1 > date2:
			print(f"That date was {int(delta.days)} days in the past")
		else:
			print("Today is indeed today")

if __name__ == '__main__':
	main()