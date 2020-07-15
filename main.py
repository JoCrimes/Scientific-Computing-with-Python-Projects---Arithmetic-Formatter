# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],False))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print("*****************\n")
print("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----")

print("*****************\n")
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
print("*****************\n")
print("   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172")

# Run unit tests automatically
main(module='test_module', exit=False)