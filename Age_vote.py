#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Thu/May13/2021
# This program is a age vote program


def main():
    # This functon checks if the person is eligible to vote or not

    # input
    age_str = input("Please enter you age:")

    # process  & output
    try:
        age_int = int(age_str)

        if (age_int >= 18):
            print("\nYes, you are eligible to vote :)")
            print("Thank you!")
        else:
            print("\nNo,you are not eligible to vote :(")
            print("Thank you!")

    except Exception:
        print("invalid input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
