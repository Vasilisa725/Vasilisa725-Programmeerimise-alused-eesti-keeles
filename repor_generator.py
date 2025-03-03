def generator_repor(data):
    ip_count = data[0]
    error_counts = data[1]
    with open("repor.txt", "w") as file:
        file.write("Loogianalüüs report \n")
        file.write("Kõige aktivsem ip oli: \n")
        for ip,count in ip_count.items():
            file.write(f"{ip}: {count} korda \n" )
        