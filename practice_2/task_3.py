# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a correct positive real number.")


if __name__ == '__main__':
    weight = get_positive_float_input("Weight (kg):")
    height = get_positive_float_input("Height (cm):")

    height = height / 100
    bmi = weight / height ** 2
    print(f"BMI: {bmi:.2f}")
