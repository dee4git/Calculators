x = 10000
for i in range(6):
    sale = x*1.4
    processing = x*1.2
    profit = sale - processing
    print('sale:', round((x * 1.4), 2))
    print('Next month:', round((x * 1.18), 2))
    print('processing:', round((x * .2), 2))
    print('pocket e:', round((x * .08), 2))
    print()

    x = x * 1.18
