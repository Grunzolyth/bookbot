def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(get_wordcount(file_contents))
    print("")
    print(get_dict(file_contents))
    print("")
    get_report(file_contents)

def get_dict(text):
    chars = {}
    for i in text:
        if i.lower() in chars:
            chars[i.lower()] += 1
        else:
            chars[i.lower()] = 1
    return chars
    
def get_wordcount(text):
    text_split = text.split()
    wordcount = 0
    for i in text_split:
        wordcount += 1
    return wordcount

def get_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_wordcount(text)} words found in the document")
    print("")

    list_of_dict = []

    for k, v in get_dict(text).items():
        if k.isalpha():
            list_of_dict.append({"key" : k, "value" : v})

    list_of_dict.sort(reverse=True, key=sort_on)

    for i in list_of_dict:
        print(f"The '{i["key"]}' character was found {i["value"]} times")


def sort_on(dict):
    return dict["value"]

main()