def friendship_compatibility(name1, name2):
    """
    Calculate friendship compatibility based on the length of the names.
    """
    len1 = len(name1.replace(" ", "").lower())
    len2 = len(name2.replace(" ", "").lower())
    
    compatibility_score = min(len1, len2) / max(len1, len2) * 100
    
    return compatibility_score

# Example usage:
name1 = "ALICE"
name2 = "BOB"
compatibility_score = friendship_compatibility(name1, name2)
print(f"The friendship compatibility score between {name1} and {name2} is: {compatibility_score:.2f}%")
