x, y = map(int, input().split())
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

day = sum(months[:x-1]) + y
week_idx = 1
print(weeks[(day+week_idx-1)%7])