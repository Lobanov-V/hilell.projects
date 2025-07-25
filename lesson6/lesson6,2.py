seconds = abs(int(input("Enter a number that is greater than or equal to 0 and less than 8640000: ")))

if 0 <= seconds < 8640000:
    days, residue = divmod(seconds, 86400)
    hours, residue = divmod(residue, 3600)
    minutes, seconds = divmod(residue, 60)

    h_str = str(hours).zfill(2)
    m_str = str(minutes).zfill(2)
    s_str = str(seconds).zfill(2)

    if days == 1:
        day_count = "день"
    elif 2<= days <= 4:
        day_count = "дні"
    else:
        day_count = "днів"

    print(f"{days} {day_count}, {h_str}:{m_str}:{s_str}")

else:
    print("That's not a number")