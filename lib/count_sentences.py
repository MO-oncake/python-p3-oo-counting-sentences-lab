#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    # Use property to access value like an attribute
    value = property(get_value, set_value)

    def is_sentence(self):
        #returns True if value ends with a period and False otherwise.
        if self._value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        #returns True if value ends with a question mark and False otherwise.
        if self._value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        #returns True if value ends with an exclamation mark and False otherwise.
        if self._value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        # Using regular expression to match sentence-ending punctuation
        sentences = re.findall(r'[.!?]+(?:\s|$)', self._value.strip())
        return len(sentences)