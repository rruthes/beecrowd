def decompose_money(value):
    notes_and_coins = [
        (10000, "nota(s) de R$ 100.00"),
        (5000, "nota(s) de R$ 50.00"),
        (2000, "nota(s) de R$ 20.00"),
        (1000, "nota(s) de R$ 10.00"),
        (500, "nota(s) de R$ 5.00"),
        (200, "nota(s) de R$ 2.00"),
        (100, "moeda(s) de R$ 1.00"),
        (50, "moeda(s) de R$ 0.50"),
        (25, "moeda(s) de R$ 0.25"),
        (10, "moeda(s) de R$ 0.10"),
        (5, "moeda(s) de R$ 0.05"),
        (1, "moeda(s) de R$ 0.01")
    ]
    total_cents = round(value * 100)
    
    print("NOTAS:")
    for i, (amount, description) in enumerate(notes_and_coins):
        if i == 6: 
            print("MOEDAS:")
        
        count = total_cents // amount
        total_cents %= amount
        
        if "nota" in description:
            print(f"{count} {description}")
        else:
            print(f"{count} {description}")

N = float(input())
decompose_money(N)