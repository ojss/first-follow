# Author Ojas Shirekar

# Opening the rules file, doing it the hard coded way for development


rules = []
firsts = []
rules_dict = {}
firsts_dict = {}


def non_term_appender(firsts, rules):
    for rule in rules:
        if (rule[0][0] not in firsts):
            firsts.append(rule[0][0])
            # firsts_dict[rule[0][0]] = []
            firsts_dict.update({rule[0][0]: []})


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

for rule in rules:
    if rule[0][3].isupper():
        firsts_dict[rule[0][0]].extend(firsts_dict[rule[0][3]])

with open("firsts.txt", "w") as wp:
    for k in firsts_dict:
        wp.write("first(%s): \t " % k)
        wp.write("%s\n" % firsts_dict[k])
