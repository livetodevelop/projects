#!/usr/bin/env python3
"""unit converter - length, weight, temperature, time"""

# conversion factors to base unit
LENGTH = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.34
}

WEIGHT = {
    "g": 1.0,
    "kg": 1000.0,
    "mg": 0.001,
    "lb": 453.592,
    "oz": 28.3495
}

TEMP = {
    "c": "celsius",
    "f": "fahrenheit", 
    "k": "kelvin"
}

TIME = {
    "s": 1.0,
    "min": 60.0,
    "h": 3600.0,
    "d": 86400.0,
    "wk": 604800.0
}

def convert_length(value, from_unit, to_unit):
    """convert between length units"""
    if from_unit not in LENGTH or to_unit not in LENGTH:
        return None
    
    # convert to meters then to target
    meters = value * LENGTH[from_unit]
    result = meters / LENGTH[to_unit]
    return result

def convert_weight(value, from_unit, to_unit):
    """convert between weight units"""
    if from_unit not in WEIGHT or to_unit not in WEIGHT:
        return None
    
    grams = value * WEIGHT[from_unit]
    result = grams / WEIGHT[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    """convert between temperature units"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # first convert to celsius
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5/9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        return None
    
    # then convert to target
    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return (celsius * 9/5) + 32
    elif to_unit == "k":
        return celsius + 273.15
    
    return None

def convert_time(value, from_unit, to_unit):
    """convert between time units"""
    if from_unit not in TIME or to_unit not in TIME:
        return None
    
    seconds = value * TIME[from_unit]
    result = seconds / TIME[to_unit]
    return result

def main():
    print("unit converter")
    print("types: length, weight, temp, time")
    print("type 'quit' to exit\n")
    
    while True:
        try:
            conv_type = input("conversion type: ").lower().strip()
            
            if conv_type == 'quit':
                break
            
            if conv_type == 'length':
                converters = {
                    'func': convert_length,
                    'units': list(LENGTH.keys())
                }
            elif conv_type == 'weight':
                converters = {
                    'func': convert_weight,
                    'units': list(WEIGHT.keys())
                }
            elif conv_type == 'temp':
                converters = {
                    'func': convert_temperature,
                    'units': list(TEMP.keys())
                }
            elif conv_type == 'time':
                converters = {
                    'func': convert_time,
                    'units': list(TIME.keys())
                }
            else:
                print(f"unknown type: {conv_type}\n")
                continue
            
            print(f"available units: {', '.join(converters['units'])}")
            
            value = float(input("value: "))
            from_unit = input("from: ").strip()
            to_unit = input("to: ").strip()
            
            result = converters['func'](value, from_unit, to_unit)
            
            if result is not None:
                print(f"result: {value} {from_unit} = {result:.6g} {to_unit}\n")
            else:
                print("invalid units for this conversion type\n")
        
        except ValueError:
            print("please enter valid numbers\n")
        except KeyboardInterrupt:
            print("\nbye!")
            break

if __name__ == "__main__":
    main()
