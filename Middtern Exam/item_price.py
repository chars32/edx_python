def items_price(a, b):
    final = []
    def mult_total(x, b):
        final.append(x*b)

    list(map(mult_total, a, b))

    return(sum(final))

        

print(items_price([2, 3, 5, 7, 9],[5, 8, 4, 1, 11]))
