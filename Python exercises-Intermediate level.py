#Check if a String is a Palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("madam"))   
print(is_palindrome("hello"))


#Return Only Even Numbers from a List
def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

print(get_even_numbers([1, 2, 3, 4, 5, 6])) 
