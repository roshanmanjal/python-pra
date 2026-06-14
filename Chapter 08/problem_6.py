# to convert form inch to cms
def inch_to_cms(inch):
    return inch * 2.54

n = float(input("Enter thr value in inch:- "))
print(f"The corressponding value in cms is:- {inch_to_cms(n)}cms ")