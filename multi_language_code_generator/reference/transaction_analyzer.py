def analyze_transactions(transactions):
    valid_count = 0
    rejected_count = 0
    total_amount = 0
    category_totals = {}
    seen_ids = set()

    for transaction in transactions:
        if not isinstance(transaction, dict):
            rejected_count += 1
            continue

        transaction_id = transaction.get("id")
        category = transaction.get("category")
        amount = transaction.get("amount_cents")

        if (
            not isinstance(transaction_id, str)
            or not transaction_id.strip()
            or not isinstance(category, str)
            or not category.strip()
            or not isinstance(amount, int)
            or isinstance(amount, bool)
            or amount < 0
            or transaction_id in seen_ids
        ):
            rejected_count += 1
            continue

        seen_ids.add(transaction_id)
        valid_count += 1
        total_amount += amount
        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    return {
        "valid_transactions": valid_count,
        "rejected_transactions": rejected_count,
        "total_amount_cents": total_amount,
        "category_totals": dict(sorted(category_totals.items()))
    }
