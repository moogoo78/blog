Lua的3元運算子 (Ternary Operator)
#################################
:date: 2013-09-23 00:39
:category: computer
:tags: lua
:slug: lua_ternary

很多語言都有簡潔的3元運算, 但是lua不支援這樣的語法.

.. code-block:: c

    // C
    sign = (x < 0) ? "negative" : "non-negative";

.. code-block:: php

    <?php
    $action = (empty($_POST['action'])) ? 'default' : $_POST['action'];
    ?>

.. code-block:: python

    # Python
    'true' if True else 'false'

.. code-block:: javascript

    // JavaScript
    x = (1 < 2) ? true : false;

不過, 還是可以利用 **and**, **or** 運算子的特性來達成. 例如:

.. code-block:: lua

    print('x is ' .. (x < 0 and 'negative' or 'non-negative'))
    print('x is ' .. ((x < 0 and 'negative') or 'non-negative')) -- 這樣好懂一點

道理何在?!

主要是利用 **and** 和 **or** 的優先循序規則看以下例子:

.. code-block:: lua

    print( 1 and "hello", "hello" and "there" )
    -- hello   there
    -- a, b 都是 *true*, 回傳b (第二個)

    print( "hello" or "there", 1 or 0 )
    -- hello   1
    -- a,b 都是 *true*, 回傳a (第一個)


Lua是很活的語言, 另外還可以用很多不同方式實現, 有興趣的人可以參考一下連結: 

* `lua-users wiki: Ternary Operator <http://lua-users.org/wiki/TernaryOperator>`__
* `lua-users wiki: Expressions Tutorial <http://lua-users.org/wiki/ExpressionsTutorial>`__
