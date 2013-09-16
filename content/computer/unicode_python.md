Title: Python & unicode
Date: 2013-09-03 16:51
Category: computer
Status: draft

Byte
==========
電腦, 檔案系統,

Ascii
不夠
 using a number between 32 and 127. Space was 32, the letter "A" was 65, etc.
7bits

 128-255 可用? -> The trouble was, lots of people had this idea at the same time, and they had their own ideas of what should go where in the space from 128 to 255. 

 code pages: Israel DOS used a code page called 862, while Greek users used 737.
The national versions of MS-DOS had dozens of these code pages

 In Asia: DBCS, the "double byte character set"

ISO/IEC 8859-1 又稱Latin-1

map 1 byte to 1 char 
map 2 bype to 1 char: Shift-JIS, GB2312, Big5

unicode
===========
http://www.unicode.org/
In Unicode, a letter maps to something called a code point which is still just a theoretical concept. How that code point is represented in memory or on disk is a whole nuther story.

unicode 1M code points, 110k assigned ?

encoding: UTF-8
variable length, ASCII, 也是用1個byte






encoding
---------
BOM


- The traditional store-it-in-two-byte methods are called UCS-2 (because it has two bytes) or UTF-16 (because it has 16 bits), and you still have to figure out if it's high-endian UCS-2 or low-endian UCS-2.
- popular UTF-8 standard which has the nice property of also working respectably if you have the happy coincidence of English text and braindead programs that are completely unaware that there is anything other than ASCII.

-There are actually a bunch of other ways of encoding Unicode. There's something called UTF-7, which is a lot like UTF-8 but guarantees that the high bit will always be zero, so that if you have to pass Unicode through some kind of draconian police-state email system that thinks 7 bits are quite enough, thank you it can still squeeze through unscathed. There's UCS-4, which stores each code point in 4 bytes, which has the nice property that every single code point can be stored in the same number of bytes, but, golly, even the Texans wouldn't be so bold as to waste that much memory.

There Ain't No Such Thing As Plain Text.


python
===========
str, unicode

str: a sequence of bytes
unicode: a sequence of code points (unicode)

unicode -> encode() => bytes (str)
bytes -> decode() => unicode

http://nedbatchelder.com/text/unipain/unipain.html#19

length

Traceback (most recent call last):
UnicodeEncodeError: 'ascii' codec can't encode characters in
          position 3-8: ordinal not in range(128)

> s.encode('u8')

UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in
          position 3: ordinal not in range(128)


參雜
===========
u'' + ''

'aa%s' % (aa)

my_list = {}
my_list.append()

if a in b:
  p

for i in my_list:
    if 


http://nedbatchelder.com/text/unipain.html

http://www.charbase.com/1f40d-unicode-snake

好用unicode
==================
◎
