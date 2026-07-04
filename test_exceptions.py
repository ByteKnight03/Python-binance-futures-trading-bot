from bot.exceptions import ValidationError

try:
    raise ValidationError("Invalid quantity.")
except ValidationError as e:
    print("Custom exception works!")
    print(e)