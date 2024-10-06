def fix_spaces(text):
    text = text.replace("  ", "-")  # replace 2 consecutive spaces with -
    text = text.replace(" ", "_")   # replace all remaining spaces with _
    return text


# Test cases
print(fix_spaces("Example"))      # Output: "Example"
print(fix_spaces("Example 1"))    # Output: "Example_1"
print(fix_spaces(" Example 2"))   # Output: "_Example_2"
print(fix_spaces(" Example   3"))  # Output: "_Example-3"
