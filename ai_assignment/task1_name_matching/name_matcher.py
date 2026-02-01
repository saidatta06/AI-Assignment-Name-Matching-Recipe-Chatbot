from rapidfuzz import process, fuzz
from names import NAMES

def find_matches(user_input, limit=5):
    results = process.extract(
        user_input,
        NAMES,
        scorer=fuzz.ratio,
        limit=limit
    )

    best_match = results[0]

    return {
        "best_match": {
            "name": best_match[0],
            "score": best_match[1]
        },
        "other_matches": [
            {"name": r[0], "score": r[1]} for r in results
        ]
    }

if __name__ == "__main__":
    name = input("Enter name: ")
    output = find_matches(name)
    print(output)
