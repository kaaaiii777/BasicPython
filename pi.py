text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

result = list(map(lambda word: len(word.strip('.,')), text.split()))

output = ''.join(map(str, result))
print(output)

