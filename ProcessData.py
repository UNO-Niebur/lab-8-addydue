# ProcessData.py
# Name: Addy Duering
# Date: 3/29/26
# Assignment: Lab 8

import random


def year_to_code(year):
    year_map = {
        "Freshman": "FR",
        "Sophomore": "SO",
        "Junior": "JR",
        "Senior": "SR",
    }
    return year_map.get(year, "UN")


def make_user_id(first_name, last_name):
    last_padded = last_name.lower()
    if len(last_padded) < 5:
        last_padded = last_padded + "x" * (5 - len(last_padded))

    random_part = str(random.randint(100000, 999999))[3:6]
    return f"{first_name[0].lower()}{last_padded}{random_part}"


def major_abbrev(major_full):
    major_clean = major_full.strip()
    if len(major_clean) >= 3:
        return major_clean[:3].upper()
    return major_clean.upper().ljust(3, "X")


def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    line = line.strip()
    info = line.split()
    firstName = info[0]
    lastName = info[1]

    last_padded = lastName.lower()
    if len(last_padded) < 5:
      last_padded = last_padded + 'x' * (5 - len(last_padded))

    studentID = random.randint(100000, 999999)
    userID = f"{firstName[0].lower()}{last_padded}{str(studentID)[3:6]}"

    fullMajor = info[6]
     # abbrev major to first 3 letters, uppercase
    major_abbrev = fullMajor[:3].upper() if len(fullMajor) >= 3 else fullMajor.upper().ljust(3, 'X')
    Year = info[5]
    if Year == "Freshman":
      Year = "FR"
    elif Year == "Sophomore":
      Year = "SO"
    elif Year == "Junior":
      Year = "JR"
    elif Year == "Senior":
      Year = "SR"
    else:
      Year = "UN"  # Unknown year

    majorYear = major_abbrev + "-" +Year

    outFile.write(lastName + "," + firstName + "," + userID + "," + majorYear + "\n")

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
    main()
