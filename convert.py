def convert_temp(unit_in, unit_out, temp):
    """Converts Fahrenheit and Celcius temperatures.
    Goes through a series of if statements asking about what units are passed as arguments.
    If the units are workable, applies a formula and returns the new_temp.
    If the units are invalid, it returns which argument was invalid.
    If the units are the same (no conversion) just returns the input temp.
    """
    if unit_in == "c" and unit_out == "f":
        new_temp = (temp * (9/5) + 32)
        return new_temp
    elif unit_in == "f" and unit_out == "c":
        new_temp = ((temp - 32) * (5/9))
        return new_temp
    elif unit_in != "c" and unit_in != "f":
        return f"Invalid unit {unit_in}"
    elif unit_out != "c" and unit_out != "f":
        return f"Invalid unit {unit_out}"
    elif unit_in == unit_out:
        return temp


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

