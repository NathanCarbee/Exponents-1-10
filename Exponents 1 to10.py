import pygame, sys, random

pygame.init()

while True :
    
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
        
    you = raw_input("Choose a Number: ")
        
    if you == "1":
        print 1 
        answer = 1
    if you == "2":
        print 2
        answer = 2
    if you == "3":
        print 3
        answer = 3
    if you == "4":
        print 4
        answer = 4
    if you == "5":
        print 5
        answer = 5
    if you == "6":
        print 6
        answer = 6
    if you == "7":
        print 7
        answer = 7
    if you == "8":
        print 8
        answer = 8
    if you == "9":
        print 9
        answer = 9
    if you == "10":
        print 10
        answer = 10
        
    you2 = raw_input("Choose an Exponent: ")
        
    if you2 == "1":
        print answer
    if you2 == "2":
        print answer * answer
    if you2 == "3":
        print answer * answer * answer
    if you2 == "4":
        print answer * answer * answer * answer
    if you2 == "5":
        print answer * answer * answer * answer * answer
    if you2 == "6":
        print answer * answer * answer * answer *answer * answer
    if you2 == "7":
        print answer * answer * answer * answer * answer * answer * answer
    if you2 == "8":
        print answer * answer * answer * answer * answer * answer * answer * answer
    if you2 == "9":
        print answer * answer * answer * answer * answer * answer * answer * answer *answer
    if you2 == "10":
        print answer * answer * answer * answer * answer * answer * answer * answer * answer *answer
        
    pygame.quit()
    sys.exit
