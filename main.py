from kakuro_simple import Kakuro

INF = float('inf')
game = Kakuro(
    n=5,
    m=5,
    block_fields=[
        (0, 0),
        (0, 1),
        (0, 4),
        (4, 4),
        (1, 0),
        (4, 0),
    ],
    hint_fields=[
        {'i': 0, 'j': 2, 'limit': {"down": 22, "right": INF}},
        {'i': 0, 'j': 3, 'limit': {"down": 12, "right": INF}},
        {'i': 1, 'j': 1, 'limit': {"down": 15, "right": 12}},
        {'i': 1, 'j': 4, 'limit': {"down": 9, "right": INF}},
        {'i': 2, 'j': 0, 'limit': {"down": INF, "right": 13}},
        {'i': 3, 'j': 0, 'limit': {"down": INF, "right": 29}},
        {'i': 4, 'j': 1, 'limit': {"down": INF, "right": 4}},
    ]
)

game.solve()
game.show()
