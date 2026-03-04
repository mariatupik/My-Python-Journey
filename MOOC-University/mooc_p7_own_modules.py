def change_case(orig_string: str):
    new_string=""
    for char in orig_string:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char
    return new_string
 
def split_in_half(orig_string: str):
    middle=len(orig_string)//2
    first_half = orig_string[:middle]
    second_half = orig_string[middle:]
    return (first_half, second_half)
 
def remove_special_characters(orig_string: str):
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    new_string = ""
    for char in orig_string:
        if char in allowed:
            new_string += char
    return new_string