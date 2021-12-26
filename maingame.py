from sample_madlibs import dayAtZoo, funPark, arcade, jungle, dayAtSchool, videogame
import random


if __name__ == "__main__":
    m = random.choice([dayAtZoo, funPark, arcade, jungle, dayAtSchool, videogame])
    m.madlib()
