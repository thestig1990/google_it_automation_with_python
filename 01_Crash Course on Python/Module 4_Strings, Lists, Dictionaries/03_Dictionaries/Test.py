def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for continent, countries in countries_dict.items():
        # Use a string method to format the required string.
        # result += ", ".join(countries) + "\n"
        #print(countries)
        result += "{}".format(countries) +  "\n"
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))