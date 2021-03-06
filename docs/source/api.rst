API Reference
=============

.. py:currentmodule:: htmap

.. highlight:: python


Map IDs
-------

The `map_id` is the central, organizing feature of HTMap.
Every map that you run produces a :class:`MapResult` which is connected to a unique ``map_id``, a string that you must provide when you run the map.
A ``map_id`` cannot be re-used until the associated map has been deleted.


HTMapper
--------

The most powerful and flexible way to work with HTMap is to use the :func:`htmap` decorator to build an :class:`HTMapper`.
The mapper can distribute (i.e., map) function calls out over an HTCondor cluster.

.. autofunction:: htmap.htmap

.. autoclass:: htmap.HTMapper
   :members:

.. autoclass:: htmap.MapBuilder
   :members:


MapResult
---------

The :class:`MapResult` is your window into the status and output of your map.
Once you get a map result back from a map call, you can use its methods to get the status of jobs (both for display and further programmatic interaction),
change the properties of the map while its running,
pause, restart, or cancel the map,
and finally retrieve the output once the map is done.

.. autoclass:: htmap.MapResult
   :members:


Management
----------

These functions help you manage your maps.

.. autofunction:: htmap.clean

.. autofunction:: htmap.map_ids

.. autofunction:: htmap.status


Shortcut Functions
------------------

These are module-level shortcut functions which let you produce and recover :class:`MapResult`\s.

.. autofunction:: htmap.map

.. autofunction:: htmap.starmap

.. autofunction:: htmap.build_map

.. autofunction:: htmap.recover


Settings
--------

HTMap exposes configurable settings through ``htmap.settings``, which is an instance of the class :class:`htmap.settings.Settings`.
This settings object manages a lookup chain of dictionaries.
The settings object created during startup contains two dictionaries.
The lowest level contains HTMap's default settings, and the next level up is constructed from a settings file at ``~/.htmap.toml``.
If that file does not exist, an empty dictionary is used instead.
As you can guess from the extension, the file is be formatted in `TOML <https://github.com/toml-lang/toml>`_.

Alternate settings could be stored in other files or constructed at runtime.
HTMap provides tools for saving, loading, merging, prepending, and appending settings to each other.
Each map is search in order, so earlier settings can flexibly override later settings.

.. warning::
   To entirely replace your settings, do **not** do ``htmap.settings = <new settings object>``.
   Instead, use the :meth:`htmap.settings.Settings.replace` method.
   Replacing the settings by assignment breaks the internal linking between the settings objects and its dependencies.

.. autoclass:: htmap.settings.Settings
   :members:


Exceptions
----------

.. automodule:: htmap.exceptions
   :members:

