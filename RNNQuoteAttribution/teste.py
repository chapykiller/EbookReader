from RNNmodels import teste
from array import array
from numpy import *

if __name__ == "__main__":
    # phrases = [
    #     "46	fry	i 've never seen a supernova blow up . but if it 's anything like my old chevy nova , it 'll light up the night sky !",
    #     "46	bender	yeah , anyone who misses this will regret it for the rest of his life ! hey fry could you go make some popcorn ?",
    #     "46	fry	ok .",
    #     "46	fry	let 's go microwave , i 'm in a hurry here ! hm ? hey , what smells like blue ?",
    #     "46	leela	fry get up here it 's starting !",
    #     "46	farnsworth	focus !",
    #     "46	bender	aw no !",
    #     "46	fry	hey , which crazy thing happening are you guys screaming about ?",
    #     "46	zoidberg	oooh my head is spinning .",
    #     "46	fry	ooo my popcorn 's done !",
    #     "46	fry	aw , it 's less popped than ever .",
    #     "46	leela	i do n't know what happened but we 've taken on a lot of clocks . let 's get back home ."
    # ]

    phrases = [
        "64	fry	what 's this ? this is the same toy surprise i got last time ! i ca n't work under these conditions . and without me there is no mission . i am the mission !",
        "64	leela	we 're back from the mission !",
        "64	fry	wh-what ? you went without me ?",
        "64	bender	you were looking up curse words in the dictionary . it seemed like a better use of your time .",
        "64	fry	but , but i 'm the delivery boy .",
        "64	leela	do n't worry , everything went fine ."
    ]

    teste(sentencernn = True, contextrnn = True, sentencebi = False, contextbi = False, phrases = phrases)
