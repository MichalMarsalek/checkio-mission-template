"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

'''
TESTS = {
    "Basics": [
        {
            "input": "h",
            "answer": verificator_hq9plus("h")
        },
        {
            "input": "q",
            "answer": verificator_hq9plus("q")
        },
        {
            "input": "9",
            "answer": verificator_hq9plus("9")
        },
        {
            "input": "+",
            "answer": verificator_hq9plus("+")
        }
    ],
    "Extra": [
        {
            "input": "hq9+",
            "answer": verificator_hq9plus("hq9+")
        }
    ]
}

def verificator_bottles():
    verses = []
    for i in range(99,0,-1):
        verses.append("{0} bottles of beer on the wall,\n{0} bottles of beer.\nTake one down, pass it around,\n{1} bottles of beer on the wall.".format(i,i-1))
    return "\n".join(verses).replace("1 bottles", "1 bottle").replace("0 bottles", "None bottles")

def verificator_hq9plus(source_code):
    outputs = []
    for char in source_code:
        if char == "h":
            outputs.append("Hello, world!")
        elif char == "q":
            outputs.append(source_code)
        elif char == "9":
            outputs.append(verificator_bottles())
    return "\n".join(outputs)
    
'''
TESTS = {
    "Basics": [
        {
            "input": "h",
            "answer": "Hello, world!"
        },
        {
            "input": "q",
            "answer": "q"
        },
        {
            "input": "+",
            "answer": ""
        }
    ]
}