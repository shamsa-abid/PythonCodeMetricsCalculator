def fruit_distribution(s, n):
    try:
        apples, oranges = [int(i) for i in s.split() if i.isdigit()]
        return n - (apples + oranges)
    except ValueError:
        return "Invalid input"
    except Exception as e:
        return str(e)
