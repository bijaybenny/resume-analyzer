def compute_score(match_result):
    direct = len(match_result["matched_direct"])
    inferred = len(match_result["matched_inferred"])
    missing = len(match_result["missing"])

    total = direct + inferred + missing

    if total == 0:
        return 0, "No skills detected"

    # Weighted scoring
    score = (direct * 1.0 + inferred * 0.5) / total

    # Explanation
    explanation = []

    if match_result["missing"]:
        explanation.append(
            "Missing skills: " + ", ".join(match_result["missing"])
        )

    if match_result["matched_inferred"]:
        explanation.append(
            "Inferred skills (not explicitly shown): " +
            ", ".join(match_result["matched_inferred"])
        )

    if match_result["matched_direct"]:
        explanation.append(
            "Strong skills: " +
            ", ".join(match_result["matched_direct"])
        )

    
    return score, explanation