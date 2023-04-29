
conversions = {
    'length': {
        'm': {
            'km': lambda x: x / 1000,
            'cm': lambda x: x * 100,
            'mm': lambda x: x * 1000,
            'in': lambda x: x / 0.0254,
            'ft': lambda x: x / 0.3048,
            'yd': lambda x: x / 0.9144,
            'mi': lambda x: x / 1609.344
        },
        'km': {
            'm': lambda x: x * 1000
        },
        'cm': {
            'm': lambda x: x / 100
        },
        'mm': {
            'm': lambda x: x / 1000
        },
        'in': {
            'm': lambda x: x * 0.0254
        },
        'ft': {
            'm': lambda x: x * 0.3048
        },
        'yd': {
            'm': lambda x: x * 0.9144
        },
        'mi': {
            'm': lambda x: x * 1609.344
        }
    },
    'mass': {
        'kg': {
            'g': lambda x: x * 1000,
            'mg': lambda x: x * 1000000,
            'lb': lambda x: x * 2.20462,
            'oz': lambda x: x * 35.274
        },
        'g': {
            'kg': lambda x: x / 1000
        },
        'mg': {
            'kg': lambda x: x / 1000000
        },
        'lb': {
            'kg': lambda x: x / 2.20462
        },
        'oz': {
            'kg': lambda x: x / 35.274
        }
    }
}


def convert_unit(value, from_unit, to_unit, unit_type):
    if from_unit == to_unit:
        return value
    elif from_unit in conversions[unit_type] and to_unit in conversions[unit_type][from_unit]:
        conversion_func = conversions[unit_type][from_unit][to_unit]
        return conversion_func(value)
    else:
        print(f"Invalid conversion: {from_unit} to {to_unit} for {unit_type}")
        return None


print("Welcome to the unit converter!")
print("Please select the conversion you would like to make:")
print("1. Length")
print("2. Mass")
print("3. Custom Conversion")
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    value = float(input("Enter length value: "))
    from_unit = input("Enter current unit (m, km, cm, mm, in, ft, yd, mi): ")
    to_unit = input("Enter target unit (m, km, cm, mm, in, ft, yd, mi): ")
    converted_value = convert_unit(value, from_unit, to_unit, 'length')
    if converted_value is not None:
        print(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
elif choice == "2":
    value = float(input("Enter mass value: "))
    from_unit = input("Enter current unit (kg, g, mg, lb, oz): ")
    to_unit = input("Enter target unit")
