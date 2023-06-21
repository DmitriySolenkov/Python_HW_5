names = ["John", "Bob", "Arianna", "Ann"]
salaries = [15000, 12000, 165000, 4500]
premiums = ["12.5", "22", "1.2", "240"]


my_iter = iter({name: salary*float(premium)/100 for name, salary, premium in zip(names, salaries, premiums)}.items())


for _ in range(len(names)):
    print(next(my_iter))
