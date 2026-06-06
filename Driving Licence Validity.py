# --------DRIVING LICENSE---------
# NAME
# BIRTH DATE (
#   1, IF AGE < 18 YOU NEED TO BE 18 OR 18 + FOR APPLY DRIVING LICENSE
#   IF AGE BETWEEN 18,30 LICENSE WILL BE VALID FOR AGE OF 40
#   IF AGE GREATER THAN 30 AND LESS THAN 50 VALID FOR 10 YEARS
#   IF AGE IS GREATER THAN 50 VALID FOR NEXT 5 YEARS
#   OF AGE IF GREATER THAN 55 THEN VALID TILL AGE OF 60 THEN AFETER )


name = input("Enter your name: ")
day = int(input("Enter your birthday: "))
month = int(input("Enter your birthmonth: "))
year = int(input("Enter your birthyear: "))

print(name)
print(day, month, year)

from datetime import date

birth_date = date(year,month,day)

today = date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
print(age)

if age < 16:
    print("Not eligible")

elif age < 18:
    print("You can apply for gearless licence")

elif age < 30:
    print("Licence valid till age 40")
    expiry_year = birth_date.year + 40
    expiry_date = date(expiry_year, birth_date.month, birth_date.day)


elif age < 50:
    print("Licence valid for 10 years")
    expiry_year = birth_date.year + 10
    expiry_date = date(expiry_year, birth_date.month, birth_date.day)


elif age < 55:
    print("Licence valid till age 60")
    expiry_year = birth_date.year + 60
    expiry_date = date(expiry_year, birth_date.month, birth_date.day)


else:
    print("licence valid for 5 years")
    expiry_year = birth_date.year + 5
    expiry_date = date(expiry_year, birth_date.month, birth_date.day)


print("\n-----DRIVING LICENCE-----")

print("Name",name)
print("Age",age)

print(
    "Expiry Date:",
    expiry_date.strftime("%d-%m-%y")

)


