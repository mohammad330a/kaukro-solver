INF = float('inf')

custom_version = {
    "n":5,
    "m":5,
    "block_fields": [
        (0, 0),
        (0, 1),
        (0, 4),
        (4, 4),
        (1, 0),
        (4, 0),
    ],
    "hint_fields":[
        {'i': 0, 'j': 2, 'limit': {"down": 22, "right": INF}},
        {'i': 0, 'j': 3, 'limit': {"down": 12, "right": INF}},
        {'i': 1, 'j': 1, 'limit': {"down": 15, "right": 12}},
        {'i': 1, 'j': 4, 'limit': {"down": 9, "right": INF}},
        {'i': 2, 'j': 0, 'limit': {"down": INF, "right": 13}},
        {'i': 3, 'j': 0, 'limit': {"down": INF, "right": 29}},
        {'i': 4, 'j': 1, 'limit': {"down": INF, "right": 4}},
    ]
}

easy_puzzle = {
    "n": 8,
    "m": 8,
    "block_fields": [
        (0, 0),
        (0, 1),
        (0, 4),
        (0, 7),
        (1, 0),
        (1, 7),
        (2, 7),
        (3, 7),
        (4, 0),
        (5, 0),
        (5, 1),
        (6, 0),
        (7, 0),
        (7, 7)
    ],
    "hint_fields": [
        {'i': 0, 'j': 2, 'limit': {"down": 11, "right": INF}},
        {'i': 0, 'j': 3, 'limit': {"down": 5, "right": INF}},
        {'i': 0, 'j': 5, 'limit': {"down": 15, "right": INF}},
        {'i': 0, 'j': 6, 'limit': {"down": 15, "right": INF}},
        {'i': 1, 'j': 1, 'limit': {"down": 3, "right": 3}},
        {'i': 1, 'j': 4, 'limit': {"down": 4, "right": 17}},
        {'i': 2, 'j': 0, 'limit': {"down": INF, "right": 22}},
        {'i': 3, 'j': 0, 'limit': {"down": INF, "right": 3}},
        {'i': 3, 'j': 3, 'limit': {"down": 11, "right": 4}},
        {'i': 3, 'j': 6, 'limit': {"down": 10, "right": INF}},
        {'i': 4, 'j': 1, 'limit': {"down": INF, "right": 8}},
        {'i': 4, 'j': 4, 'limit': {"down": 7, "right": 3}},
        {'i': 4, 'j': 7, 'limit': {"down": 8, "right": INF}},
        {'i': 5, 'j': 2, 'limit': {"down": 4, "right": 4}},
        {'i': 5, 'j': 5, 'limit': {"down": 3, "right": 4}},
        {'i': 6, 'j': 1, 'limit': {"down": INF, "right": 21}},
        {'i': 7, 'j': 1, 'limit': {"down": INF, "right": 3}},
        {'i': 7, 'j': 4, 'limit': {"down": INF, "right": 4}},
    ]
}

medium_puzzle = {
    "n": 8,
    "m": 8,
    "block_fields": [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 6),
        (0, 7),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 6),
        (1, 7),
        (2, 0),
        (2, 1),
        (3, 0),
        (5, 6),
        (5, 7),
        (6, 0),
        (6, 1),
        (6, 6),
        (6, 7),
        (7, 0),
        (7, 1),
        (7, 5),
        (7, 6),
        (7, 7)
    ],
    "hint_fields": [
        {'i': 0, 'j': 4, 'limit': {"down": 40, "right": INF}},
        {'i': 0, 'j': 5, 'limit': {"down": 3, "right": INF}},
        {'i': 1, 'j': 3, 'limit': {"down": 8, "right": 6}},
        {'i': 2, 'j': 2, 'limit': {"down": INF, "right": 7}},
        {'i': 2, 'j': 6, 'limit': {"down": 3, "right": INF}},
        {'i': 2, 'j': 7, 'limit': {"down": 14, "right": INF}},
        {'i': 3, 'j': 1, 'limit': {"down": 6, "right": INF}},
        {'i': 3, 'j': 2, 'limit': {"down": 4, "right": 10}},
        {'i': 3, 'j': 5, 'limit': {"down": 24, "right": 9}},
        {'i': 4, 'j': 0, 'limit': {"down": INF, "right": 28}},
        {'i': 5, 'j': 0, 'limit': {"down": INF, "right": 3}},
        {'i': 5, 'j': 3, 'limit': {"down": 17, "right": 17}},
        {'i': 6, 'j': 2, 'limit': {"down": INF, "right": 23}},
        {'i': 7, 'j': 2, 'limit': {"down": INF, "right": 16}},
    ]
}


hard_puzzle = {
    "n": 10,
    "m": 10,
    "block_fields": [
        (0, 0),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (1, 4),
        (1, 5),
        (1, 6),
        (2, 5),
        (3, 0),
        (3, 9),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 8),
        (4, 9),
        (5, 0),
        (5, 1),
        (5, 2),
        (5, 7),
        (5, 8),
        (5, 9),
        (6, 0),
        (6, 1),
        (6, 9),
        (7, 0),
        (8, 4),
        (8, 5),
        (9, 3),
        (9, 4),
        (9, 5),
        (9, 6),
    ],
    "hint_fields": [
        {'i': 0, 'j': 1, 'limit': {"down": 10, "right": INF}},
        {'i': 0, 'j': 2, 'limit': {"down": 10, "right": INF}},
        {'i': 0, 'j': 8, 'limit': {"down": 23, "right": INF}},
        {'i': 0, 'j': 9, 'limit': {"down": 16, "right": INF}},
        {'i': 1, 'j': 0, 'limit': {"down": INF, "right": 4}},
        {'i': 1, 'j': 3, 'limit': {"down": 17, "right": INF}},
        {'i': 1, 'j': 7, 'limit': {"down": 17, "right": 16}},
        {'i': 2, 'j': 0, 'limit': {"down": INF, "right": 23}},
        {'i': 2, 'j': 4, 'limit': {"down": 20, "right": INF}},
        {'i': 2, 'j': 6, 'limit': {"down": 30, "right": 24}},
        {'i': 3, 'j': 1, 'limit': {"down": INF, "right": 13}},
        {'i': 3, 'j': 5, 'limit': {"down": 20, "right": 23}},
        {'i': 4, 'j': 3, 'limit': {"down": INF, "right": 11}},
        {'i': 5, 'j': 3, 'limit': {"down": 6, "right": 23}},
        {'i': 6, 'j': 2, 'limit': {"down": 7, "right": 25}},
        {'i': 6, 'j': 7, 'limit': {"down": 3, "right": INF}},
        {'i': 6, 'j': 8, 'limit': {"down": 9, "right": INF}},
        {'i': 7, 'j': 1, 'limit': {"down": 4, "right": 8}},
        {'i': 7, 'j': 5, 'limit': {"down": INF, "right": 7}},
        {'i': 7, 'j': 9, 'limit': {"down": 4, "right": INF}},
        {'i': 8, 'j': 0, 'limit': {"down": INF, "right": 6}},
        {'i': 8, 'j': 6, 'limit': {"down": INF, "right": 6}},
        {'i': 9, 'j': 0, 'limit': {"down": INF, "right": 3}},
        {'i': 9, 'j': 7, 'limit': {"down": INF, "right": 4}}
    ]
}



expert_puzzle = {
    "n": 10,
    "m": 10,
    "block_fields": [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 7),
        (0, 8),
        (0, 9),

        (1, 0),
        (1, 1),
        (1, 8),
        (1, 9),

        (2, 0),
        (2, 9),

        (7, 0),

        (8, 0),
        (8, 1),
        (8, 8),
        (8, 9),

        (9, 0),
        (9, 1),
        (9, 2),
        (9, 8),
        (9, 9),
    ],
    "hint_fields": [
        {'i': 0, 'j': 3, 'limit': {"down": 3, "right": INF}},
        {'i': 0, 'j': 4, 'limit': {"down": 23, "right": INF}},
        {'i': 0, 'j': 5, 'limit': {"down": 45, "right": INF}},
        {'i': 0, 'j': 6, 'limit': {"down": 6, "right": INF}},
        {'i': 1, 'j': 2, 'limit': {"down": INF, "right": 12}},
        {'i': 1, 'j': 7, 'limit': {"down": 4, "right": INF}},
        {'i': 2, 'j': 1, 'limit': {"down": 20, "right": INF}},
        {'i': 2, 'j': 2, 'limit': {"down": 32, "right": 21}},
        {'i': 2, 'j': 8, 'limit': {"down": 15, "right": INF}},
        {'i': 3, 'j': 0, 'limit': {"down": INF, "right": 3}},
        {'i': 3, 'j': 3, 'limit': {"down": 17, "right": 15}},
        {'i': 3, 'j': 6, 'limit': {"down": 5, "right": 4}},
        {'i': 3, 'j': 9, 'limit': {"down": 16, "right": INF}},

        {'i': 4, 'j': 0, 'limit': {"down": INF, "right": 24}},
        {'i': 4, 'j': 4, 'limit': {"down": 16, "right": 3}},
        {'i': 4, 'j': 7, 'limit': {"down": 4, "right": 7}},

        {'i': 5, 'j': 0, 'limit': {"down": INF, "right": 45}},

        {'i': 6, 'j': 0, 'limit': {"down": INF, "right": 17}},
        {'i': 6, 'j': 3, 'limit': {"down": 13, "right": 17}},
        {'i': 6, 'j': 6, 'limit': {"down": 24, "right": 6}},

        {'i': 7, 'j': 1, 'limit': {"down": INF, "right": 16}},
        {'i': 7, 'j': 4, 'limit': {"down": 17, "right": 15}},
        {'i': 7, 'j': 7, 'limit': {"down": 13, "right": 6}},

        {'i': 8, 'j': 2, 'limit': {"down": INF, "right": 32}},

        {'i': 9, 'j': 3, 'limit': {"down": INF, "right": 30}},
    ]
}