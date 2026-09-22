idx = 0
while idx <= 10:
    print(f"Table de {idx}:", end="")
    rol = 0
    while rol <= 10:
        print(f" {rol * idx}", end="")
        rol += 1
    idx += 1
    print()