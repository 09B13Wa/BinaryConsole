#  Copyright [2022] [Jascha MERLE]
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from __future__ import annotations


class Byte:
    """
    An 8-bit unsigned integer. Uses little endian representation.

    Attributes\:
            __first_bit: a boolean representing the least significant bit
            (the eighth most significant bit) in the byte.
            It represents the 2⁰ (1) value of the byte. True if the bit is 1. False if the bit is 0.\n
            __second_bit: a boolean representing the second least significant bit
            (the seventh most significant bit) in the byte.
            It represents the 2¹ (2) value of the byte. True if the bit is 1. False if the bit is 0.\n
            __third_bit: a boolean representing the third least significant bit
            (the sixth most significant bit) in the byte.
            It represents the 2² (4) value of the byte. True if the bit is 1. False if the bit is 0.\n
            __forth_bit: a boolean representing the forth least significant bit
            (the fifth most significant bit) in the byte.
            It represents the 2³ (8) value of the byte. True if the bit is 1. False if the bit is 0.\n
            __fifth_bit: a boolean representing the fifth least significant bit
            (the forth most significant bit) in the byte.
            It represents the 2⁴ (16) value of the byte. True if the bit is 1. False if the bit is 0.\n
            __sixth_bit: a boolean representing the sixth least significant bit
            (the third most significant bit) in the byte.
            It represents the 2⁵ (32) value of the byte. True if the bit is 1. False if the bit is 0.\n
            __seventh_bit: a boolean representing the seventh least significant bit
            (the second most significant bit) in the byte.
            It represents the 2⁶ (64) value of the byte. True if the bit is 1. False if the bit is 0.\n
            __eighth_bit: a boolean representing the eighth least significant bit
            (the most significant bit) in the byte.
            It represents the 2⁷ (128) value of the byte. True if the bit is 1. False if the bit is 0.

            __byte_value_zero: a Byte representing the integer value 0 (0000 0000).
            This value is used in methods and may be uninitialized. Use at your own risks.\n
            __byte_value_one: a Byte representing the integer value 1 (0000 0001)
            This value is used in methods and may be uninitialized. Use at your own risks.\n
            __byte_value_two: a Byte representing the integer value 3 (0000 0010)
            This value is used in methods and may be uninitialized. Use at your own risks.\n
            __byte_value_three: a Byte representing the integer value 4 (0000 0100)
            This value is used in methods and may be uninitialized. Use at your own risks.\n
            __byte_value_four: a Byte representing the integer value 5 (0000 0101)
            This value is used in methods and may be uninitialized. Use at your own risks.\n
            __byte_value_five: a Byte representing the integer value 6 (0000 0110)
            This value is used in methods and may be uninitialized. Use at your own risks.\n
            __byte_value_six: a Byte representing the integer value 7 (0000 0111)
            This value is used in methods and may be uninitialized. Use at your own risks.\n

            __value: an unsigned integer representing the current integer value of the byte.\n
            __char: a string containing the current extended ASCII
            character represented by the integer the byte is representing.
            The string contains only this character and no other characters.
    """

    __first_bit: bool
    __second_bit: bool
    __third_bit: bool
    __forth_bit: bool
    __fifth_bit: bool
    __sixth_bit: bool
    __seventh_bit: bool
    __eighth_bit: bool

    __byte_value_zero: Byte
    __byte_value_one: Byte
    __byte_value_two: Byte
    __byte_value_three: Byte
    __byte_value_four: Byte
    __byte_value_five: Byte
    __byte_value_six: Byte
    __byte_value_seven: Byte

    __value: int
    __char: str

    def __init__(self, first_bit: bool = False, second_bit: bool = False, third_bit: bool = False,
                 forth_bit: bool = False, fifth_bit: bool = False, sixth_bit: bool = False,
                 seventh_bit: bool = False, eighth_bit: bool = False) -> None:
        """
        Create a new byte (8-bit unsigned integer) by assigning manually the bit values.
        The values are represented using little endian which means the first bytes
        are the least significant. For each bit, represented by a boolean, True stands for 1
        and 0 for False. False is the default value for unspecified bits.

        :param first_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 1 (2⁰).
        :param second_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 2 (2¹).
        :param third_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 4 (2²).
        :param forth_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 8 (2³).
        :param fifth_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 16 (2⁴).
        :param sixth_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 32 (2⁵).
        :param seventh_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 64 (2⁶).
        :param eighth_bit: True if the value is 1 or False if the value is 0. The default value is 0. In decimal, this value is 128 (2⁷).
        """
        self.__first_bit = first_bit
        self.__second_bit = second_bit
        self.__third_bit = third_bit
        self.__forth_bit = forth_bit
        self.__fifth_bit = fifth_bit
        self.__sixth_bit = sixth_bit
        self.__seventh_bit = seventh_bit
        self.__eighth_bit = eighth_bit

        self.__value = self.__compute_int()
        self.__char = chr(self.__value)

    def __compute_int(self) -> int:
        """
        Computes the unsigned integer the byte represents in decimal.
        :return: The int object which represents the decimal unsigned integer represented by the byte.
        """
        total: int = 0
        total += self.__first_bit * 1
        total += self.__second_bit * 2
        total += self.__third_bit * 4
        total += self.__forth_bit * 8
        total += self.__fifth_bit * 16
        total += self.__sixth_bit * 32
        total += self.__seventh_bit * 64
        total += self.__eighth_bit * 128

        return total

    @staticmethod
    def from_int(number: int) -> Byte:
        first_bit: int = number & 1
        second_bit = (number >> 1) & 1
        third_bit: int = (number >> 2) & 1
        forth_bit: int = (number >> 3) & 1
        fifth_bit: int = (number >> 4) & 1
        sixth_bit: int = (number >> 5) & 1
        seventh_bit: int = (number >> 6) & 1
        eighth_bit: int = (number >> 7) & 1

        first_bit_bool: bool = first_bit == 1
        second_bit_bool: bool = second_bit == 1
        third_bit_bool: bool = third_bit == 1
        forth_bit_bool: bool = forth_bit == 1
        fifth_bit_bool: bool = fifth_bit == 1
        sixth_bit_bool: bool = sixth_bit == 1
        seventh_bit_bool: bool = seventh_bit == 1
        eighth_bit_bool: bool = eighth_bit == 1

        return Byte(first_bit_bool, second_bit_bool, third_bit_bool, forth_bit_bool,
                    fifth_bit_bool, sixth_bit_bool, seventh_bit_bool, eighth_bit_bool)

    @staticmethod
    def from_str(string: str):
        str_len: int = len(string)
        first_bit: bool = False
        second_bit: bool = False
        third_bit: bool = False
        forth_bit: bool = False
        fifth_bit: bool = False
        sixth_bit: bool = False
        seventh_bit: bool = False
        eighth_bit: bool = False

        if str_len > 0:
            first_bit = string[0] == "1"
        if str_len > 1:
            second_bit = string[1] == "1"
        if str_len > 2:
            third_bit = string[2] == "1"
        if str_len > 3:
            forth_bit = string[3] == "1"
        if str_len > 4:
            fifth_bit = string[4] == "1"
        if str_len > 5:
            sixth_bit = string[5] == "1"
        if str_len > 6:
            seventh_bit = string[6] == "1"
        if str_len > 7:
            eighth_bit = string[7] == "1"

        return Byte(first_bit, second_bit, third_bit, forth_bit,
                    fifth_bit, sixth_bit, seventh_bit, eighth_bit)

    @staticmethod
    def from_char(char: str) -> Byte:
        char_ord: int = ord(char)
        return Byte.from_int(char_ord)

    @staticmethod
    def from_byte(byte: Byte) -> Byte:
        return Byte(byte.__first_bit, byte.__second_bit, byte.__third_bit, byte.__forth_bit,
                    byte.__fifth_bit, byte.__sixth_bit, byte.__seventh_bit, byte.__eighth_bit)

    @staticmethod
    def __transform_int_to_bool(number: int) -> bool:
        if number == 0:
            return False
        else:
            return True

    @staticmethod
    def __transform_str_to_bool(number: str) -> bool:
        if number == "0":
            return False
        else:
            return True

    @property
    def first_bit(self) -> bool:
        return self.__first_bit

    @first_bit.setter
    def first_bit(self, new_value: bool):
        self.__first_bit = new_value

    @property
    def first_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__first_bit)

    @first_bit_int.setter
    def first_bit_int(self, new_value: int):
        self.__first_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def first_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__first_bit)

    @first_bit_str.setter
    def first_bit_str(self, new_value: str):
        self.__first_bit = Byte.__transform_str_to_bool(new_value)

    @property
    def second_bit(self) -> bool:
        return self.__second_bit

    @second_bit.setter
    def second_bit(self, new_value: bool):
        self.__second_bit = new_value

    @property
    def second_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__second_bit)

    @second_bit_int.setter
    def second_bit_int(self, new_value: int):
        self.__second_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def second_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__second_bit)

    @second_bit_str.setter
    def second_bit_str(self, new_value: str):
        self.__second_bit = Byte.__transform_str_to_bool(new_value)

    @property
    def third_bit(self) -> bool:
        return self.__third_bit

    @third_bit.setter
    def third_bit(self, new_value: bool):
        self.__third_bit = new_value

    @property
    def third_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__third_bit)

    @third_bit_int.setter
    def third_bit_int(self, new_value: int):
        self.__third_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def third_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__third_bit)

    @third_bit_str.setter
    def third_bit_str(self, new_value: str):
        self.__third_bit = Byte.__transform_str_to_bool(new_value)

    @property
    def forth_bit(self) -> bool:
        return Byte.__forth_bit

    @forth_bit.setter
    def forth_bit(self, new_value: bool):
        self.__forth_bit = new_value

    @property
    def forth_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__forth_bit)

    @forth_bit_int.setter
    def forth_bit_int(self, new_value: int):
        self.__forth_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def forth_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__forth_bit)

    @forth_bit_str.setter
    def forth_bit_str(self, new_value: str):
        self.__forth_bit = Byte.__transform_str_to_bool(new_value)

    @property
    def fifth_bit(self) -> bool:
        return Byte.__fifth_bit

    @fifth_bit.setter
    def fifth_bit(self, new_value: bool):
        self.__fifth_bit = new_value

    @property
    def fifth_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__fifth_bit)

    @fifth_bit_int.setter
    def fifth_bit_int(self, new_value: int):
        self.__fifth_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def fifth_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__fifth_bit)

    @fifth_bit_str.setter
    def fifth_bit_str(self, new_value: str):
        self.__fifth_bit = Byte.__transform_str_to_bool(new_value)

    @property
    def sixth_bit(self) -> bool:
        return Byte.__sixth_bit

    @sixth_bit.setter
    def sixth_bit(self, new_value: bool):
        self.__sixth_bit = new_value

    @property
    def sixth_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__sixth_bit)

    @sixth_bit_int.setter
    def sixth_bit_int(self, new_value: int):
        self.__sixth_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def sixth_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__sixth_bit)

    @sixth_bit_str.setter
    def sixth_bit_str(self, new_value: str):
        self.__sixth_bit = Byte.__transform_str_to_bool(new_value)

    @property
    def seventh_bit(self) -> bool:
        return Byte.__seventh_bit

    @seventh_bit.setter
    def seventh_bit(self, new_value: bool):
        self.__seventh_bit = new_value

    @property
    def seventh_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__seventh_bit)

    @seventh_bit_int.setter
    def seventh_bit_int(self, new_value: int):
        self.__seventh_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def seventh_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__seventh_bit)

    @seventh_bit_str.setter
    def seventh_bit_str(self, new_value: str):
        self.__seventh_bit = Byte.__transform_str_to_bool(new_value)

    @property
    def eighth_bit(self) -> bool:
        return Byte.__eighth_bit

    @eighth_bit.setter
    def eighth_bit(self, new_value: bool):
        self.__eighth_bit = new_value

    @property
    def eighth_bit_int(self) -> int:
        return Byte.__convert_bool_to_int(self.__eighth_bit)

    @eighth_bit_int.setter
    def eighth_bit_int(self, new_value: int):
        self.__eighth_bit = Byte.__transform_int_to_bool(new_value)

    @property
    def eighth_bit_str(self) -> str:
        return Byte.__convert_bool_to_str(self.__eighth_bit)

    @eighth_bit_str.setter
    def eighth_bit_str(self, new_value: str):
        self.__eighth_bit = Byte.__transform_str_to_bool(new_value)

    @staticmethod
    def __convert_bool_to_str(bool_value: bool) -> str:
        if bool_value:
            return "1"
        else:
            return "0"

    @staticmethod
    def __convert_bool_to_int(bool_value: bool) -> int:
        if bool_value:
            return 1
        else:
            return 0

    def __str__(self) -> str:
        return f"{self.first_bit_str}{self.second_bit_str}{self.third_bit_str}{self.forth_bit_str}" \
               f"{self.fifth_bit_str}{self.sixth_bit_str}{self.seventh_bit_str}{self.eighth_bit_str}"

    def __int__(self) -> int:
        return self.__value

    def __bool__(self) -> bool:
        return bool(self.__value)

    def __len__(self) -> int:
        return 8

    def __initialize_if_uninitialized_predefined_byte_values(self):
        if self.__byte_value_zero is None:
            self.__byte_value_zero = Byte()
            self.__byte_value_one = Byte(True)
            self.__byte_value_two = Byte(second_bit=True)
            self.__byte_value_three = Byte(True, True)
            self.__byte_value_four = Byte(third_bit=True)
            self.__byte_value_five = Byte(True, third_bit=True)
            self.__byte_value_six = Byte(second_bit=True, third_bit=True)
            self.__byte_value_seven = Byte(True, True, True)

    def __getitem__(self, item) -> int:
        self.__initialize_if_uninitialized_predefined_byte_values()
        if isinstance(item, int):
            if item == 0:
                return self.first_bit_int
            elif item == 1:
                return self.second_bit_int
            elif item == 2:
                return self.third_bit_int
            elif item == 3:
                return self.forth_bit_int
            elif item == 4:
                return self.fifth_bit_int
            elif item == 5:
                return self.sixth_bit_int
            elif item == 6:
                return self.seventh_bit_int
            elif item == 7:
                return self.eighth_bit_int
        elif isinstance(item, Byte):
            if item == self.__byte_value_zero:
                return self.first_bit_int
            elif item == self.__byte_value_one:
                return self.second_bit_int
            elif item == self.__byte_value_two:
                return self.third_bit_int
            elif item == self.__byte_value_three:
                return self.forth_bit_int
            elif item == self.__byte_value_four:
                return self.fifth_bit_int
            elif item == self.__byte_value_five:
                return self.sixth_bit_int
            elif item == self.__byte_value_six:
                return self.seventh_bit_int
            elif item == self.__byte_value_seven:
                return self.eighth_bit_int
        elif isinstance(item, str):
            int_value: int = int(item)
            return self.__getitem__(int_value)

    def __setitem__(self, key, value):
        if isinstance(value, bool):
            self.__initialize_if_uninitialized_predefined_byte_values()
            if isinstance(key, int):
                if key == 0:
                    self.first_bit = value
                elif key == 1:
                    self.second_bit = value
                elif key == 2:
                    self.third_bit = value
                elif key == 3:
                    self.forth_bit = value
                elif key == 4:
                    self.fifth_bit = value
                elif key == 5:
                    self.sixth_bit = value
                elif key == 6:
                    self.seventh_bit = value
                elif key == 7:
                    self.eighth_bit = value
            elif isinstance(key, Byte):
                if key == self.__byte_value_zero:
                    self.first_bit = value
                elif key == self.__byte_value_one:
                    self.second_bit = value
                elif key == self.__byte_value_two:
                    self.third_bit = value
                elif key == self.__byte_value_three:
                    self.forth_bit = value
                elif key == self.__byte_value_four:
                    self.fifth_bit = value
                elif key == self.__byte_value_five:
                    self.sixth_bit = value
                elif key == self.__byte_value_six:
                    self.seventh_bit = value
                elif key == self.__byte_value_seven:
                    self.eighth_bit = value
            else:
                value_int: int = int(value)
                self.__setitem__(key, value_int)
        elif isinstance(value, int):
            value_bool: bool = self.__transform_int_to_bool(value)
            self.__setitem__(key, value_bool)
        elif isinstance(value, str):
            value_bool: bool = self.__transform_str_to_bool(value)
            self.__setitem__(key, value_bool)

    def __add__(self, other) -> Byte:
        """
        Add operator for Byte. Supports adding with Byte, int and str
        and any type which has int() (self.__int__()) and str() (self.__str__())
        functions that convert to valid binary data.
        Valid binary data is a type that has
        an implemented integer conversion which converts the object into an integer
        between 0 and 255 included or if that is not implemented,
        an implementation of the str() function which returns an eight or less character long
        string which is only made up '0' (value: 48) and '1' (value: 49) characters.
        :param other: the other object to add. It must be either a byte
        or a positive integer included or a string made up of eight or fewer characters
        which is only made up '0' (value: 48) and '1' (value: 49) characters.
        If the object isn't of those types, if it implements the int() (self.__int__()) function
        and returns a positive integer, then the calculation will be performed
        with that integer. If the object isn't of those types nor doesn't implement
        an int() (self.__int__()) function, if it implements an str() (self.__str__()) function,
        then the function is called and if it is made up of no more than 8 characters which are all
        only '0' (value: 48) or '1' (value: 49) characters, then the calculation is performed with those
        that string being parsed into a Byte object. Otherwise, nothing is added and a warning is sent
        to the standard error stream.
        """
        if isinstance(other, Byte):
            # the current carry, initialized at 0
            current_carry: int = 0
            addition_byte: Byte = Byte()
            for i in range(8):
                # gather the binary values at the current index
                # from the current object as well as the passed object
                self_value_at_position: int = self[i]
                other_value_at_position: int = other[i]
                # compute total amount at position
                sum_value: int = current_carry + self_value_at_position + other_value_at_position
                # adjust carry depending on sum. The sum can be 0, 1, 2 or 3.
                # The carry must be 1 for integral values 2 (10) and 3 (11)
                # and 0 for integral values 0 (00) and 1 (01)
                if sum_value > 1:
                    current_carry = 1
                else:
                    current_carry = 0

                # the final value to set in place of the old value.
                # Since the possible values are 0 (00), 1 (01), 2 (10) and 3 (11),
                # the final value must be 1 if the value is 1 (01) or 3 (11).
                # The final value must be 0 if the value is 0 (00) or 2 (10).
                final_value: int
                if sum_value == 1 or sum_value == 3:
                    final_value = 1
                else:
                    final_value = 0

                # the calculated final value to set in place is set in place.
                addition_byte[i] = final_value

            return addition_byte

        elif isinstance(other, int):
            total: int = self.__value + other
            byte: Byte = Byte.from_int(total)
            return byte

        elif isinstance(other, str):
            byte_to_add: Byte = Byte.from_str(other)
            return byte_to_add + self

        elif hasattr(other, '__int__'):
            int_value: int = int(other)
            byte_to_add: Byte = Byte.from_int(int_value)
            return self + byte_to_add

        elif hasattr(other, '__str__'):
            str_value: str = str(other)
            byte_to_add: Byte = Byte.from_str(str_value)
            return self + byte_to_add

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        if isinstance(other, Byte):
            return self.__first_bit == other.__first_bit \
                   and self.__second_bit == other.__second_bit \
                   and self.__third_bit == other.__third_bit \
                   and self.__forth_bit == other.__forth_bit \
                   and self.__fifth_bit == other.__fifth_bit \
                   and self.__sixth_bit == other.__sixth_bit \
                   and self.__seventh_bit == other.__seventh_bit \
                   and self.__eighth_bit == other.__eighth_bit
        elif isinstance(other, int):
            return self.__value == other
        elif isinstance(other, str):
            return str(self) == other
        elif hasattr(other, "__int__"):
            other_int: int = int(other)
            return self.__value == other_int
        elif hasattr(other, "__str__"):
            other_str: str = str(other)
            return str(self) == other_str

    def __ne__(self, other):
        if isinstance(other, Byte):
            return self.__first_bit != other.__first_bit \
                   or self.__second_bit != other.__second_bit \
                   or self.__third_bit != other.__third_bit \
                   or self.__forth_bit != other.__forth_bit \
                   or self.__fifth_bit != other.__fifth_bit \
                   or self.__sixth_bit != other.__sixth_bit \
                   or self.__seventh_bit != other.__seventh_bit \
                   or self.__eighth_bit != other.__eighth_bit
        elif isinstance(other, int):
            return self.__value != other
        elif isinstance(other, str):
            return str(self) != other
        elif hasattr(other, "__int__"):
            other_int: int = int(other)
            return self.__value != other_int
        elif hasattr(other, "__str__"):
            other_str: str = str(other)
            return str(self) != other_str

    def __hash__(self):
        hash(self.__char)
