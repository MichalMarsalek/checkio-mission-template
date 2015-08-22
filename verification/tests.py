"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

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
'''