def gym_cost(plan, age):
    costs = { "monthly": 1000, "quarterly": 2500, "yearly": 9000}
    cost = costs[plan]

    if age < 18:
        cost = cost - (cost * 20 / 100)

    return cost

plan = input("Enter plan (monthly/quarterly/yearly): ").lower()
age = int(input("Enter age: "))
print("Final Cost =", gym_cost(plan, age))

