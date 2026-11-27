records = []
try:
    with open("scores.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            try:
                score = int(score)
                records.append([name, score])
            except ValueError:
                continue

    # Find Karim's score
    for record in records:
        if record[0] == "Karim":
            print(record[1])

    # Count valid scores
    print(len(records))

    # Update the records
    updated = []

    for record in records:
        name = record[0]
        score = record[1]

        if name == "Nour":
            continue

        if name == "Maya":
            score = 88

        updated.append([name, score])

    # Write the updated scores
    with open("scores.txt", "w") as file:
        for record in updated:
            file.write(record[0] + "," + str(record[1]) + "\n")

    # Create pass.txt
    with open("pass.txt", "w") as file:
        for record in updated:
            if record[1] >= 60:
                file.write(record[0] + "\n")

except FileNotFoundError:
    print("File not found.")
