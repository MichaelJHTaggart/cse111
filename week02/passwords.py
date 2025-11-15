LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

dictionary_word_message = "Password is a dictionary word and is not secure."
commonly_used_message = "Password is a commonly used password and is not secure."
too_short_message = "Password is too short and is not secure."
great_password_message = "Password is long, length trumps complexity this is a good password"

password_check_loop = True

"""
This function reads a file (specified by the filename parameter) in which each line of the file contains a single word. If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a false. If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false a case insensitive match is performed. The case_sensitive parameter should default to False
"""
def word_in_file(word, filename, case_sensitive = False):
    if not case_sensitive:
        word = word.lower()

    with open(filename, "r", encoding="utf-8") as file_word:
        for line in file_word:
            clean_line = line.strip()
            if not case_sensitive:
                clean_line = clean_line.lower()
            if word == clean_line:
                return True
        return False

"""
This function loops through each character in the string passed in the word parameter to see if that character is in the list of characters passed in the character_list parameter. If any of the characters in the word are present in the character list return a true, If none of the characters in the word are in the character list return false
"""
def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    return False

"""
This function creates a numeric complexity value based on the types of characters the word parameter contains. One point of complexity is given for each type of character in the word. The function calls the word_has_character function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a point is added to complexity rating. Since there are 4 kinds of characters the complexity rating will range from 0 to 4. (0 would be returned only if word contained no characters or only contains characters that are not in any of the lists.)
"""
def word_complexity(word):
    characters_the_word_parameter_contains = 1

    if word_has_character(word, LOWER):
        characters_the_word_parameter_contains += 1
    if word_has_character(word, UPPER):
        characters_the_word_parameter_contains += 1
    if word_has_character(word, DIGITS):
        characters_the_word_parameter_contains += 1
    if word_has_character(word, SPECIAL):
        characters_the_word_parameter_contains += 1

    return characters_the_word_parameter_contains

"""
This function checks length requirements
checks dictionary and known-passwords
calls word_complexity to calculate the word's complexity
determines the password's strength based on the user requirements
It should print the messages defined in the requirements
Return the password's strength as a number from 0 to 5
The min_length parameter should have a default value of 10
The strong_length parameter should have a default value of 16
"""
def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt"):
        print(dictionary_word_message)
        return 0

    if word_in_file(password, "toppasswords.txt", True):
        print(f"{commonly_used_message}")
        return 0

    if len(password) < min_length:
        print(f"{too_short_message}")
        return 1
    
    if len(password) > strong_length:
        print(f"{great_password_message}")
        return 5
    
    password_complexity = word_complexity(password)
    return password_complexity

"""
Provides the user input loop. The loop asks the user for a password to test. If that password is anything but "q" or "Q" call the password_strength function and report the results to the user. If the user enters "q" or "Q", quit the program.
"""
def main():
    global password_check_loop
    while password_check_loop == True:
        user_entered_password = input("What password would you like to test? ")
        if user_entered_password != 'q' and user_entered_password != 'Q':
            print(f"Your password Strength is: {password_strength(user_entered_password)}")
        else:
            password_check_loop = False

    print(f"quitting program just as Sven has outlined :)")


# Stay's at the bottom of my file per Sven's request
if __name__ == "__main__":
    main()