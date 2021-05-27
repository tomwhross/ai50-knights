from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),  # A is a knight or a knave
    Not(And(AKnight, AKnave)),  # A cannot be both knight and knave
    Biconditional(
        AKnight, Not(AKnave)
    ),  # can only be a knight if an only if not a knave
    # claims
    Biconditional(
        AKnight, And(AKnight, AKnave)
    ),  # if and only if A is a knight, then their claim is true
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),  # A is a knight or knave
    Not(And(AKnight, AKnave)),  # A cannot be both knight and knave
    Or(BKnave, BKnight),  # A is a knight or knave
    Not(And(BKnight, BKnave)),  # A cannot be both knight and knave
    Biconditional(
        AKnight, Not(AKnave)
    ),  # can only be a knight if an only if not a knave
    Biconditional(
        BKnight, Not(BKnave)
    ),  # can only be a knight if an only if not a knave
    # claims
    Biconditional(
        AKnight, And(AKnave, BKnave)
    ),  # if and only if A is a knight, then their claim is true
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),  # A is a knight or knave
    Not(And(AKnight, AKnave)),  # A cannot be both knight and knave
    Or(BKnave, BKnight),  # A is a knight or knave
    Not(And(BKnight, BKnave)),  # A cannot be both knight and knave
    Biconditional(
        AKnight, Not(AKnave)
    ),  # can only be a knight if an only if not a knave
    Biconditional(
        BKnight, Not(BKnave)
    ),  # can only be a knight if an only if not a knave
    # claims
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, Not(BKnight)), And(AKnave, Not(BKnave)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),  # A is a knight or knave
    Not(And(AKnight, AKnave)),  # A cannot be both knight and knave
    Or(BKnave, BKnight),  # A is a knight or knave
    Not(And(BKnight, BKnave)),  # A cannot be both knight and knave
    Or(CKnave, CKnight),  # A is a knight or knave
    Not(And(CKnight, CKnave)),  # A cannot be both knight and knave
    Biconditional(
        AKnight, Not(AKnave)
    ),  # can only be a knight if an only if not a knave
    Biconditional(
        BKnight, Not(BKnave)
    ),  # can only be a knight if an only if not a knave
    Biconditional(
        CKnight, Not(CKnave)
    ),  # can only be a knight if an only if not a knave
    # claims
    Biconditional(AKnight, Or(AKnight, AKnave)),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
