#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if not isinstance(value, str):
      print("The value must be a string.")
    self._value = value

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    

  def count_sentences(self):
      sentence_count = 0
      i = 0
      while i < len(self.value):
          if self.value[i] in ".!?":
              sentence_count += 1
              while i < len(self.value) and self.value[i] in ".!?":
                  i += 1
          else:
              i += 1
      return sentence_count