"""Finds the first and follow for a given grammar"""
# Author Ojas Shirekar
# Under the GPL license
from collections import OrderedDict

# Opening the rules file, doing it the hard coded way for development


rules = []  # Raw grammar rules
firsts = []  # Used as temp storage for firsts if needed

# Ordered dictionary to maintain the order of saving in the dictionary
# useful when doing the actual first finding in one pass.
rules_dict = OrderedDict()  # Dictionary to store all the rules in the grammar
firsts_dict = OrderedDict()  # Dictionary to store all the firsts
follow_dict = OrderedDict()  # Dictionary that stores all follows


def write_dict(dict, file_name):
    with open(file_name, "w+") as write_ptr:
        for k in dict:
            write_ptr.write("%s\t" % k)
            write_ptr.write("%s\n" % dict[k])


def non_term_appender(firsts, rules):
    """Adds the non terminals on the left to the firsts_dict"""
    for rule in rules:
        if rule[0][0] not in firsts:
            firsts.append(rule[0][0])
            firsts_dict[rule[0][0]] = []
            follow_dict[rule[0][0]] = []


with open("rules_test.txt", "r") as fp:
    for line in fp:
        # Splitting on newline and turning it into an array
        rules.append(line.strip().split('\n'))

# ++++++    Following code is used to find firsts   +++++++++
number_of_rules = len(rules)
rule_count = first_count = 0
non_term_appender(firsts, rules)
for first in firsts:
    rules_dict[first] = rules[rule_count][0][3:]
    rule_count += 1

for rule in rules:
    if rule[0][3].islower():
        firsts_dict[rule[0][0]].extend(rule[0][3])
# TODO try and re implement one pass, as an else condition in the above loop.
for rule in rules:
    if rule[0][3].isupper():
        firsts_dict[rule[0][0]].extend(firsts_dict[rule[0][3]])

with open("firsts.txt", "w+") as wp:
    for k in firsts_dict:
        wp.write("first(%s): \t " % k)
        wp.write("%s\n" % firsts_dict[k])

# ++++++    Following code is used to find the follows  ++++++

rules_keys = rules_dict.keys()
key_count = len(rules_keys)

for k in rules_dict:
    tmp_rule_str = rules_dict[k]
    if k == rules_keys[0]:
        follow_dict[k].append('$')
    for i in xrange(key_count):
        if rules_keys[i] in tmp_rule_str:
            # Follow finding for last non-terminal in the
            tmp_rule_list = list(tmp_rule_str)
            # stores the index non-terminal we are finding the follow for in a
            # variable
            current_non_term_index = tmp_rule_list.index(rules_keys[i])

            if current_non_term_index == (len(tmp_rule_list) - 1) and tmp_rule_list[current_non_term_index].isupper():
                # if the index of the current non-term is at last one,
                #  means that the follow for the current non-term will be the
                # follow of the left-hand side
                follow_dict[rules_keys[i]].extend(follow_dict[rules_keys[0]])
            else:
                # If not then the first of the next non-term from the current
                # non-term becomes the follow of the current
                follow_dict[rules_keys[i]].extend(
                    firsts_dict[rules_keys[(i + 1) % key_count]])

with open("follows.txt", "w+") as wp:
    for k in follow_dict:
        wp.write("follow(%s): \t" % k)
        wp.write("%s\n" % follow_dict[k])
print "Firsts Dict:" + " ", follow_dict
print "Follow Dict:" + " ", firsts_dict

write_dict(follow_dict, "test")
write_dict(firsts_dict, "test2")
