Write a method, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.


The method should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

test_00

Source.uncompress("2c3a1t"); // -> "ccaaat"

test_01

Source.uncompress("4s2b"); // -> "ssssbb"

test_02

Source.uncompress("2p1o5p"); // -> "ppoppppp"

test_03

Source.uncompress("3n12e2z"); // -> "nnneeeeeeeeeeeezz"

test_04

Source.uncompress("127y"); // ->"yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"