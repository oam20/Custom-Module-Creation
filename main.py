# Normal import
import math_utils
from string_utils import reverse_string, count_words
import string_utils as su


print("=== Math Utilities ===")

percentage = math_utils.calculate_percentage(75, 100)
print(f"Percentage: {percentage:.1f}%")


numbers = [70, 80, 92, 100]
average = math_utils.calculate_average(numbers)
print(f"Average: {average:.1f}")


maximum, minimum = math_utils.find_max_min(numbers)
print(f"Max: {maximum}, Min: {minimum}")


prime_result = math_utils.is_prime(17)
print(f"Is 17 prime? {prime_result}")


print("\n=== String Utilities ===")


reversed_text = reverse_string("Hello World!")
print(f"Reversed: {reversed_text}")


word_count = count_words("Hello World Python")
print(f"Word Count: {word_count}")


capitalized_text = su.capitalize_words("hello world python")
print(f"Capitalized: {capitalized_text}")


no_duplicates = su.remove_duplicates("Hello World")
print(f"No Duplicates: {no_duplicates}")