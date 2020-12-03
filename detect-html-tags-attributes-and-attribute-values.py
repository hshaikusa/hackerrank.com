# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

from html.parser import HTMLParser
from html.entities import name2codepoint
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        #print ("End   :", tag)
        pass
        
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

    def handle_comment(self, comment):
        #print("Comment  :", comment)
        pass

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)
                
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)
    def handle_decl(self, data):
        print("Decl     :", data)

if __name__ == '__main__':
    parser = MyHTMLParser()
    parser.feed(''.join([input().strip() for _ in range(int(input()))]))
