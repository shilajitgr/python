"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

alison heck => Alison Heck


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, S.

"""


def solve(s):

    name_split = s.split(" ")
    copy_name = []
    for word in name_split:
        if word:
            word_list = list(word)
            word_list[0] = word_list[0].upper()
            copy_name.append("".join(word_list))
        else:
            copy_name.append("")

    return " ".join(copy_name)


if __name__ == '__main__':

    print(solve(input("Please enter your name: ")))