def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)."""
    return weight / (height ** 2)

def bmi_category(bmi):
    """Categorize BMI based on standard BMI categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    
    print("Welcome to the BMI Calculator!")
    
    # User input validation
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms: "))
            height = float(input("Please enter your height in meters: "))
            if weight <= 0 or height <= 0 or height>2.51 or weight> 635:
                raise ValueError("Weight and height must be positive and valid.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    # Display result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()
