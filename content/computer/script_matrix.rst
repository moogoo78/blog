Scripting 比較 (draft)
#######################################
:date: 2013-04-09 11:38
:category: computer
:tags: docs


PHP, Python, Javascript, Lua


易搞混
================

hash/dictionary/table
------------------------
json:

.. code-block:: json

  {
       "firstName": "John",
       "lastName": "Smith",
       "male": true,
       "age": 25,
       "address": 
       {
           "streetAddress": "21 2nd Street",
           "city": "New York",
           "state": "NY",
           "postalCode": "10021"
       },
       "phoneNumber": 
       [
           {
             "type": "home",
             "number": "212 555-1234"
           },
           {
             "type": "fax",
             "number": "646 555-4567"
           }
       ]
   }


python dictionary:

.. code-block:: python

  dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}


lua table:

.. code-block:: lua

  t = {"a", "b", [123]="foo", "c", name="bar", "d", "e"}


Data Type
===========
**Array**

::

  # python
  arr = [1, 2, 3]

  # lua
  squares = {1, 4, 9, 16, 25, 36, 49, 64, 81}
  squares[1] # 1




statement/expression
==============================

函式
------------

**引數**

::

  # python
  def func(a, *pargs, **kargs): print a, pargs, kargs
  # >>> f(1, 2, 3, x=1, y=2)
  # 1 (2, 3) {'y': 2, 'x': 1}
  # *pargs: 任意引數 (tuple)
  # *kargs: 任意引數 (dict)

  # lua
  function foo(a, ...)  
      print (a)
      print (spam)
  end

  foo(1, 'lovely') -- 1, nil
  foo(1,'lovely') -- 1, lovely


Lib funtions
=================


String
------

**substring**

::

  # php
  echo substr('abcdef', 1, 3);  // bcd

  # python 
  foostring[a:b]

  # javascript
  foostring.substr(a,len) // 從a剪取len長度
  foostring.subString(a,b) // 從a剪到b

  # lua
  string.sub( foostring, i [,j] ) // i: start, j:end
  foostring:sub(i [,j])

**string replace**

::

  # python 
  foostring.replace('old', 'new')

  # javascript
  var s = "abxxef";
  s.replace("xx","cd");

  # lua
  s = "abxxef"
  s = s:gsub("xx", "cd")

  # php
  $foo = str_replace("old", "new", "STRING");


**string format**

::

  # lua
  string.format("%02d/%02d/%04d", d, m, y)

**upper lower**

::

 # Lua
 string.upper(s)
 s:upper()

**string to array**

::

  # php
  explode(',', $string)

  # python 
  str.split(',')

  # lua
  split("a,b,c", ",") --> {"a", "b", "c"}


**array to string**

::

  # php
  implode(1,, $array);

  # python 
  str.join(list)

  # lua
  table.concat({"a", "b", "c"}, ",") --> "a,b,c"  


頭尾空白 Jinja2
php trim($string)
python s.strip()

Array
-----

**append**

::

  # python 
  t.append(21)

  # lua
  table.insert(t, 21)


** array length**

::

  # Python 
  len(arr) # arr.count("foo") 是算"foo"在arr裡出現幾次

  # PHP
  count(arr)

  # Lua
  #arr



**PHP**

.. code-block:: html+php

   <?php
       $arr = array();
       $fruits = array("a" => "orange", "b" => "banana", "c" => "apple");
       array_push();
   ?>

**Python**

.. code-block:: python

   append(x) # push 
   insert(i,x) # insert x to i
   remove(x) # delete first 
   pop(i) # delete index i
   len(arr) 


**JavaScript**

.. code-block:: javascript

   append(x) # push 
   var arr:Array = new Array();
   arr.length

**ActionScript**

.. code-block:: actionscript

   push() 
   arr.length

File
----
**PHP**

.. code-block:: html+php

   <?php
       $fp = fopen('foo.txt', 'w');
       fwrite($fp, 'abc'); 
       fclose($fp);
   ?>

explode join


**Python**

.. code-block:: py

   f = open('foo.txt', 'w') 
   f.write('abc')
   f.close()


Math
-------

.. code-block:: python

  # python 
  random.random() # Random float x, 0.0 <= x < 1.0
  random.randint(1, 10)  # Integer from 1 to 10

  # javascript
  Math.random() # 0 ~ 0.9999999

  # lua
  math.random(100)

  # php
  rand(5, 15) # min: 0 


Array
-----

============ =============================
Reverse
============ =============================
PHP          | array_reverse($a); 
             | $a = array_reverse($a);
Python       | a.reverse() 
             | a[::-1]
JavaScript   | a.reverse()
ActionScript |
============ =============================

* `Scripting Languages: PHP, Perl, Python, Ruby - Hyperpolyglot <http://hyperpolyglot.org/scripting>`__
* `Php2Python - Python alternatives to PHP functions, classes and libraries - Php2Python <http://www.php2python.com/>`__

http://code.google.com/p/ppython/wiki/data_convert



tmp
----
ternary operator
