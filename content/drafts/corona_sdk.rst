Corona SDK (draft)
#######################
:date: 2013-07-02 10:41
:status: draft
:category: computer
:tags: docs
:slug: corona_sdk

Tips
=================
顯示圖層遮住其他event, via: `Corona SDK: Avoid touch events through layered screens - BLOG - Monkeybin <http://www.monkeybin.no/blog/archives/2011/08/08/corona-sdk-avoid-touch-events-through-layered-screens/>`__

.. code-block:: lua

  rect:addEventListener("touch", function() return true end)
  rect:addEventListener("tap", function() return true end)



Snippets
====================

string
---------------------

**trim**

.. code-block:: lua

  local function trim( str )
     return ( str:gsub("^%s*(.-)%s*$", "%1") )
  end

via: http://www.coronalabs.com/blog/2013/07/02/tutorial-extending-libraries-without-native-code/

list
-----------

**sort by key**

.. code-block:: lua

    function pairsByKeys (t, f)
      local a = {}
      for n in pairs(t) do table.insert(a, n) end
      table.sort(a, f)
      local i = 0      -- iterator variable
      local iter = function ()   -- iterator function
        i = i + 1
        if a[i] == nil then return nil
        else return a[i], t[a[i]]
        end
      end
      return iter
    end

via: http://www.lua.org/pil/19.3.html


debug
=============================

adb logcat Corona:v *:s
