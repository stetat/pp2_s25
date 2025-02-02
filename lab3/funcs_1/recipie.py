reqs = int(input("Enter grams amount: "))


def gtoo(grams):
    return 28.3495231 * grams

print(f"We support ounces only!\n {reqs} grams is {gtoo(reqs)} ounces")

