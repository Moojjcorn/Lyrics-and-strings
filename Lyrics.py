while True:
    Song = """Tonight I'm gonna have myself a real good time
    I feel alive
    And the world I'll turn it inside out, yeah
    I'm floating around in ecstasy
    So, (don't stop me now)
    (Don't stop me)
    'Cause I'm having a good time, having a good time
    I'm a shooting star leaping through the sky
    Like a tiger defying the laws of gravity
    I'm a racing car passing by like Lady Godiva
    I'm gonna go, go, go
    There's no stopping me
    I'm burnin' through the sky, yeah
    200 degrees
    That's why they call me Mister Fahrenheit
    I'm travelling at the speed of light
    I wanna make a supersonic man out of you
    I'm having such a good time
    I'm having a ball
    (Don't stop me now)
    If you wanna have a good time just give me a call
    (Don't stop me now)
    'Cause I'm having a good time
    (Don't stop me now)
    Yes, I'm havin' a good time
    I don't want to stop at all
    Yeah, I'm a rocket ship on my way to Mars
    On a collision course
    I am a satellite I'm out of control
    I am a sex machine ready to reload
    Like an atom bomb about to
    Oh, oh, oh, oh, oh, explode
    I'm burnin' through the sky, yeah
    200 degrees
    That's why they call me Mister Fahrenheit
    I'm travelling at the speed of light
    I wanna make a supersonic woman of you
    Don't stop me, don't stop me
    Don't stop me, hey, hey, hey
    Don't stop me, don't stop me
    Ooh, ooh, ooh, I like it
    Don't stop me, don't stop me
    Have a good time, good time
    Don't stop me, don't stop me, ah
    Let loose, honey, all right
    Oh, I'm burnin' through the sky, yeah
    200 degrees
    That's why they call me Mister Fahrenheit
    I'm travelling at the speed of light
    I wanna make a supersonic man out of you
    I'm having such a good time
    I'm having a ball
    (Don't stop me now)
    If you wanna have a good time (alright)
    Just give me a call
    (Don't stop me now)
    'Cause I'm having a good time
    (Don't stop me now)
    Yes, I'm havin' a good time
    I don't want to stop at all
    La-da-da-da-dah
    Da-da-da-ha
    Ha-da-da, ha-ha-ha
    Ha-da-da, ha-da-da-ah"""

    word1 = input("Replace a word in the song text: ").lower()
    word2 = input("What word to replace it with: ").lower()
    word3 = input("Second word to replace: ").lower()
    word4 = input("What word to replace it with: ").lower()

    Song1 = Song.lower().replace(word1 , word2).replace(word3, word4)
    print(Song1)