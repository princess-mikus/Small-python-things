# Made by Mikus

import datetime
from sys import argv

def check_valid_day(date):
	day = int(date[0])
	month = int(date[1])
	year = int(date[2])

	if month == 4 or month == 6 or month == 9 or month == 11:
		if day > 30:
			return (0)
	elif month == 2:
		if not year % 4 and year % 100:
			if day > 29:
				return (0)
		else:
			if day > 28:
				return (0)
	return (1)

def main():
	arg = 1
	custom_format = False

	if len(argv) < 3:
		print("Bad number of arguments"), exit(2)

	if argv[1] == "-f" or argv[1] == "--format":
		arg += 2
		custom_format = True
		if argv[2].upper() == "YMD" or argv[2].upper() == "ISO":
			date1 = argv[arg].split('/')
			date2 = argv[arg + 1].split('/')
			date1.reverse()
			date2.reverse()
		elif argv[2].upper() == "MDY" or argv[2].lower() == "american":
			date1 = argv[arg].split('/')
			date2 = argv[arg + 1].split('/')
			date1 = [date1[1], date1[0], date1[2]]
			date2 = [date2[1], date2[0], date2[2]]
		else:
			print("Wrong format"), exit (2)

	if argv[arg] == "today":
		date1 = str(datetime.date.today()).split('-')
		date1.reverse()
	elif not custom_format:
		date1 = argv[arg].split('/')

	if argv[arg + 1] == "today":
		date2 = str(datetime.date.today()).split('-')
		date2.reverse()
	elif not custom_format:
		date2 = argv[arg + 1].split('/')

	if len(date1) > 3 or len(date2) > 3:
		print("Argument not a date"), exit (-1)

	for i in range(0, len(date1)):
		if not date1[i].isdigit():
			print("Bad argument format in first argument"), exit (0)
		elif i == 0 and int(date1[i]) > 31:
			print("Day must be less than 31"), exit (0)
		elif i == 1 and int(date1[i]) > 12:
			print("Month must be less than 12"), exit (0)

	for i in range(0, len(date2)):
		if not date2[i].isdigit():
			print("Bad argument format in second argument"), exit (0)
		elif i == 0 and int(date2[i]) > 31:
			print("Day must be less than 31"), exit (0)
		elif i == 1 and int(date2[i]) > 12:
			print("Month must be less than 12"), exit (0)

	if not check_valid_day(date1) or not check_valid_day(date2):
		print("Correct format but day not valid for that month"), exit (0)

	date1 = datetime.date(int(date1[2]), int(date1[1]), int(date1[0]))
	date2 = datetime.date(int(date2[2]), int(date2[1]), int(date2[0]))

	delta = date1 - date2

	if argv[arg] != "today" and argv[arg + 1] != "today":
		if date1 < date2:
			print(f"{argv[arg]} is {int(delta.days) * -1} days before {argv[arg + 1]}")
		elif date1 > date2:
			print(f"{argv[arg]} is {int(delta.days)} days after {argv[arg + 1]}")
		else:
			print("Those are the same dates!")
	else:
		if argv[arg] == "today":
			if date1 < date2:
				print(f"That date will be in {int(delta.days) * -1} days")
			elif date1 > date2:
				print(f"That date was {int(delta.days)} days in the past")
			else:
				print("Today is indeed today")
		else:
			if date1 > date2:
				print(f"That date will be in {int(delta.days)} days")
			elif date1 < date2:
				print(f"That date was {int(delta.days) * -1} days in the past")
			else:
				print("Today is indeed today")

if __name__ == '__main__':
	main()