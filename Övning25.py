import requests


def main(startdate, enddate):
    r = requests.get("https://proagile.se/api/publicEvents")
    course_list = r.json()
    for course in course_list:
        coursedate = course['startDate']
        if startdate <= coursedate <= enddate:
            print()
            kursnamn = "Kursnamn:"
            startdatum = "Startdatum:"
            slutdatum = "Slutdatum:"
            print(f"{kursnamn:>12} {course['name']:100}")
            print(f"{startdatum:>12} {coursedate:100}")
            print(f"{slutdatum:>12} {course['endDate']:100}")


if __name__ == '__main__':
    year = input("Year:")
    month = input("Month:")

    start = f"{year:0}-{month:02}-01"
    end = f"{year:0}-{month:02}-31"

    main(startdate=start, enddate=end)
