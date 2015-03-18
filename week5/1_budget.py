def on_budget(books, budget):
    result = {
        "books_on_budget": 0,
        "loan": 0
        }

    books = sorted(books)

    for book in books:
        if budget >= book:
            budget -= book
            result["books_on_budget"] += 1
        else:
            loan = book - budget
            budget = 0
            result["loan"] += loan

    return result
