def madlib():
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    verb1 = input("Verb: ")
    verb_past1 = input("Verb, Past tense: ")
    verb_past2 = input("Verb, Past tense: ")
    adverb1 = input("Adverb: ")
    adverb2 = input("Adverb: ")

    madlib_string = f"Today, I went to the zoo. I saw a(n) {adj1} {noun1} jumping up and down in its tree. " \
                    f"He {verb_past1} {adverb1} through the large tunnel that led to its {adj2} {noun2}. I got some " \
                    f"peanuts and passed them through a cage to a gigantic gray {noun3} towering above my head. " \
                    f"Feeding that animal made me hungry. I went to get a {adj3} scoop of ice cream. It filled my " \
                    f"stomach. Afterwards, I had to {verb1} {adverb2} to catch our bus. when I got home, I {verb_past2}" \
                    f" my mum for a {adj4} day at the zoo."

    print(madlib_string)



