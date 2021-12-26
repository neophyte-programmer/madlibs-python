def madlib():
    adj1 = input("Adjective: ")
    noun1 = input("Plural Noun: ")
    noun2 = input("Noun: ")
    adverb1 = input("Adverb: ")
    num1 = input("Number: ")
    verb1 = input("Verb, Past Tense: ")
    adj2 = input(" -est Adjective: ")
    verb2 = input("Verb, Past Tense: ")
    adverb2 = input("Adverb: ")
    adj3 = input("Adjective: ")

    madlib_string = f"Today, my fabulous camp group went to a(n) {adj1} amusement park. It was a fun park " \
                    f"with lots of cool {noun1} and enjoyable play structures. When we got there, my kind counsellor " \
                    f"shouted loudly, 'Everybody get off the {noun2}.' We all pushed out in a terrible hurry. " \
                    f"My counsellor handed our yellow tickets and we scurried in. I was so excited! I couldn't " \
                    f"figure out what exciting thing to do first. I saw a scary roller coaster I really liked so " \
                    f"I {adverb1} ran over to get in the long line that had about {num1} people in it. When I " \
                    f"finally got on the roller coaster, I was {verb1}. In fact, i was so nervous my two knees " \
                    f"were knocking each other. This was the {adj2} ride I had ever been on. In about two minutes " \
                    f"I heard the crank of gears. That's when the ride began! When I got to the bottom, I was a" \
                    f" little {verb2} but I was proud of myself. The rest of the day went {adverb2}. It was a(n) " \
                    f"{adj3} at the park!"

    print(madlib_string)
