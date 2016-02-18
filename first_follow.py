# Author Ojas Shirekar
# Under the GPL license
from collections import OrderedDict
# Opening the rules file, doing it the hard coded way for development


rules = []  # Raw grammar rules
firsts = []

# Ordered dictionary to maintain the order of saving in the dictionary, useful when doing the actual
# first finding in one pass.
rules_dict = OrderedDict()  # Dictionary to store all the rules in the grammar
firsts_dict = OrderedDict()  # Dictionary to store all the firsts


def non_term_appender(firsts, rules):
    for rule in rules:
        if (rule[0][0] not in firsts):
            firsts.append(rule[0][0])
            firsts_dict[rule[0][0]] = []


with open("rules_test.txt", "r") as fp:
    for line in fp:
        rules.append(line.strip().split('\n'))  # Splitting on newline and
        # and turning it into an array

number_of_rules = len(rules)
# Printing the array
rule_count = first_count = 0
non_term_appender(firsts, rules)
for first in firsts:
    rules_dict[first] = rules[rule_count][0][3:]
    rule_count += 1

for rule in rules:
    if (rule[0][3].islower()):
        firsts_dict[rule[0][0]].append(rule[0][3])
# TODO try and re implement one pass, as an else condition in the above loop.
for rule in rules:
    if rule[0][3].isupper():
        firsts_dict[rule[0][0]].extend(firsts_dict[rule[0][3]])

with open("firsts.txt", "w+") as wp:
    for k in firsts_dict:
        wp.write("first(%s): \t " % k)
        wp.write("%s\n" % firsts_dict[k])

print(firsts_dict)