def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight / (height ** 2)"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI based on standard BMI categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight, height)

        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    main()

