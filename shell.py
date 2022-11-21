import blackstone

while True:
    text = input('BlackStone > ')
    result, error = blackstone.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)