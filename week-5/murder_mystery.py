
def investigate(name, clues):
    rules = [
        {"if": {"owns_chef_knives", "watches_true_crime"}, "then": "had_means"},
        {"if": {"criminal_record"}, "then": "had_means"},
        {"if": {"passed_over_for_promotion"}, "then": "had_motive"},
        {"if": {"was_home_at_10pm"}, "then": "had_opportunity"},
        {"if": {"had_means", "had_motive", "had_opportunity"}, "then": "prime_suspect"}
    ]
    facts = set(clues)
    changed = True
    passes = 0
    while changed:
        changed = False
        passes += 1
        for rule in rules:
            if rule["if"] <= facts and rule["then"] not in facts:
                facts.add(rule["then"])
                changed = True
                print(name, " --> fired:", rule["then"])
    print(name, "- passes:", passes)
    return facts

# Which of the suspects is the murderer? Use investigate(name, clues).
suspects = {
    "Jay": {"owns_chef_knives", "watches_true_crime", "was_home_at_10pm", "passed_over_for_promotion"},
    "Jessie": {"criminal_record", "was_home_at_10pm"},
    "Beth": {"watches_true_crime", "passed_over_for_promotion"}
}

for name, clues in suspects.items():
    result = investigate(name, clues)
    print(name, "prime suspect?", "prime_suspect" in result)
    print()