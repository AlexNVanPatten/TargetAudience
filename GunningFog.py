#countsyl is by shallowsky, with some editing

#!//usr/bin/env python

# Count syllables in a word.
#
# Doesn't use any fancy knowledge, just a few super simple rules:
# a vowel starts each syllable;
# a doubled vowel doesn't add an extra syllable;
# two or more different vowels together are a diphthong,
# and probably don't start a new syllable but might;
# y is considered a vowel when it follows a consonant.
#
# Even with these simple rules, it gets results far better
# than python-hyphenate with the libreoffice hyphenation dictionary.
#
# Copyright 2013 by Akkana Peck http://shallowsky.com.
# Share and enjoy under the terms of the GPLv2 or later.

def count_syllables(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    on_vowel = False
    in_diphthong = False
    minsyl = 0
    maxsyl = 0
    lastchar = None
    word = word.lower()
    for c in word:
        is_vowel = c in vowels
        if on_vowel == None:
            on_vowel = is_vowel
        # y is a special case
        if c == 'y':
            is_vowel = not on_vowel
        if is_vowel:
            if not on_vowel:
                # We weren't on a vowel before.
                # Seeing a new vowel bumps the syllable count.
                minsyl += 1
                maxsyl += 1
            elif on_vowel and not in_diphthong and c != lastchar:
                # We were already in a vowel.
                # Don't increment anything except the max count,
                # and only do that once per diphthong.
                in_diphthong = True
                maxsyl += 1
        on_vowel = is_vowel
        lastchar = c
    # Some special cases:
    if word[-1] == 'e':
        minsyl -= 1
    # if it ended with a consonant followed by y, count that as a syllable.
    if word[-1] == 'y' and not on_vowel:
        maxsyl += 1
    return (minsyl + maxsyl) / 2

#returns Gunning Fog number for given text
def count(text):
    clauses, words, hardwords = 0, 0, 0
    # assuming major clauses end in '.', '!', '?', ':', or ';', count clauses
    clauses += text.count('.') + text.count('!') + text.count('?') + text.count(':') + text.count(';')
    tempwords = text.split(None)
    for word in tempwords:
        #four+ syllable words can be considered complex
        syllables = count_syllables(word.strip())
        if syllables > 3:
            hardwords += 1
        #discount words that are three syllables because of common endings
        #otherwise three syllable words are also complex
        elif syllables == 3:
            if not (word.endswith('ed') or word.endswith('ing') or word.endswith('es') or word.endswith('ly')):
                hardwords += 1
    #number of words in text
    words += len(tempwords)
    #making decimals work
    wordy = float(words)
    #The Gunning Fog formula for readability of text, in number of years of education necessary
    #to understand the material
    GunningFog = 0.4 * ((wordy / clauses) + 100 * (hardwords / wordy))
    return GunningFog

print(count("Did you know that nature's deadliest predator is probably lurking in your neighborhood? Odds are, you may be even harboring it in your home. Confused? We are talking about your pet cat. Though they may appear cuddly and innocent, they are known to wreak havoc on their local ecology, killing birds, small mammals, and reptiles at an alarming rate. In addition to being beloved companions, cats have been a preferred method of pest control for humans for thousands of years. However, as the human population has increased, so has the number of these relentless hunters. In the United States alone, about 80 million homes house at least one cat, while another 80 million wander as strays. Combined, these felines kill about 2.4 billion birds, and 20.7 billion small mammals like mice, moles, and chipmunks, annually! A 2013 study printed in the journal Nature Communications suggests that the domestic cat species is responsible for the extinction of up to 33 species across the globe. It calls cats \"likely the single greatest source of anthropogenic mortality for U.S birds and mammals! While cat owners don't have an issue with the felines taking care of pesky mice and rats, they certainly have no desire to lose the innocent birds that are chirping in their yards. In order to prevent that cats are often collared with tiny bells that signal their presence to the critters they are trying to snare. However, the clever hunters have been known to silence the noisy bells by either pulling them off or getting rid of the collar altogether. Some cats are even smart enough to keep the bells from ringing by taking stealthier steps. Dr. Michael Calver of Australia's Murdoch University, is so concerned about the plight of the birds that he has published several research papers trying to solve the issue. Hence when he and Ph.D. student Catherine Hall stumbled upon a website that claimed their brightly colored collar scrunchies could reduce the number of bird deaths by 87%, they decided to investigate it. Hall teamed up with 114 cat owners and asked them to \"freeze\" everything their pets killed for two years, with and without them wearing the brightly colored scrunchies. Sure enough, the number of birds, reptiles, and amphibians killed when the cats were wearing the bright collars reduced by 54%. Though not as high as the 87% claimed by the website, it is substantial enough to make a difference. Hall, who published her findings in the scientific journal Applied Animal Behavior Science in January 2015, believes that the simple solution works because it enables songbirds to see the cats approaching from a distance. This allows them to make a quick escape. Interestingly, the number of mice and other small mammals the cats captured was not reduced when the scrunchie was implemented. This is likely because their color vision isn't as developed as that of birds. Hence, the colorful scrunchie is a win-win for both humans and birds!  A similar study done in the US around the same time confirmed these findings. But before you rush to place a normal scrunchie onto your cat's neck, be careful for it may be too tight and result in constricting his/her neck. Instead, seek out ones specially created for this very purpose and save those poor birds!"))




