while True:
    miles = input("Enter miles (type 0 to stop): ")

    if miles == "0":
        print("Program stopped.")
        break

    miles = float(miles)
    km = miles * 1.609

    print("Kilometers:", km)
