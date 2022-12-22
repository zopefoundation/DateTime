Changelog
=========

4.9 (2022-12-22)
----------------

- Fix regression in 4.7 on Python 2 when calling ``asdatetime``.
  (`#47 <https://github.com/zopefoundation/DateTime/issues/47>`_)


4.8 (2022-12-16)
----------------

- Fix insidious buildout configuration bug that prevented tests on Python 2.7
  and 3.5, and fix test code that was incompatible with Python 3.5.
  (`#44 <https://github.com/zopefoundation/DateTime/issues/44>`_)

- Add support for Python 3.11.


4.7 (2022-09-14)
----------------

- Fix rounding problem with `DateTime` addition beyond the year 2038
  (`#41 <https://github.com/zopefoundation/DateTime/issues/41>`_)


4.6 (2022-09-10)
----------------

- Fix ``__format__`` method for DateTime objects
  (`#39 <https://github.com/zopefoundation/DateTime/issues/39>`_)


4.5 (2022-07-04)
----------------

- Add ``__format__`` method for DateTime objects
  (`#35 <https://github.com/zopefoundation/DateTime/issues/35>`_)


4.4 (2022-02-11)
----------------

- Fix WAT definition
  `#31 <https://github.com/zopefoundation/DateTime/issues/31>`_.

- Add support for Python 3.8, 3.9, and 3.10.

- Drop support for Python 3.4.

4.3 (2018-10-05)
----------------

- Add support for Python 3.7.

4.2 (2017-04-26)
----------------

- Add support for Python 3.6, drop support for Python 3.3.

4.1.1 (2016-04-30)
------------------

- Support unpickling instances having a numeric timezone like `+0430`.

4.1 (2016-04-03)
----------------

- Add support for Python 3.4 and 3.5.

- Drop support for Python 2.6 and 3.2.

4.0.1 (2013-10-15)
------------------

- Provide more backward compatible timezones.
  [vangheem]

4.0 (2013-02-23)
----------------

- Added support for Python 3.2 and 3.3 in addition to 2.6 and 2.7.

- Removed unused legacy pytz tests and the DateTimeZone module and renamed
  some test internals.

3.0.3 (2013-01-22)
------------------

- Allow timezone argument to be a Unicode string while creating a DateTime
  object using two arguments.

3.0.2 (2012-10-21)
------------------

- LP #1045233: Respect date format setting for parsing dates like `11-01-2001`.

3.0.1 (2012-09-23)
------------------

- Add `_dt_reconstructor` function introduced in DateTime 2.12.7 to provide
  forward compatibility with pickles that might reference this function.

3.0 (2011-12-09)
----------------

- No changes.

Backwards compatibility of DateTime 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DateTime 3 changes its pickle representation. DateTime instances pickled with
former versions of DateTime can be read, but older DateTime versions cannot read
DateTime instances pickled with version 3.

DateTime 3 changes DateTime to be a new-style class with slots instead of being
an old-style class.

DateTime 3 tries to preserve microsecond resolution throughout most of its API's
while former versions were often only accurate to millisecond resolution. Due to
the representation of float values in Python versions before Python 2.7 you
shouldn't compare string or float representations of DateTime instances if you
want high accuracy. The same is true for calculated values returned by methods
like `timeTime()`. You get the highest accuracy of comparing DateTime values by
calling its `micros()` methods. DateTime is not particular well suited to be
used in comparing timestamps of file systems - use the time and datetime objects
from the Python standard library instead.

3.0b3 (2011-10-19)
------------------

- Allow comparison of DateTime objects against None.

3.0b2 (2011-10-19)
------------------

- Reverted the single argument `None` special case handling for unpickling and
  continue to treat it as meaning `now`.

3.0b1 (2011-05-07)
------------------

- Restored `strftimeFormatter` as a class.

- Added tests for read-only class attributes and interface.

3.0a2 (2011-05-07)
------------------

- Added back support for reading old DateTime pickles without a `_micros` value.

- Avoid storing `_t` representing the time as a float in seconds since the
  epoch, as we already have `_micros` doing the same as a long. Memory use is
  down to about 300 bytes per DateTime instance.

- Updated exception raising syntax to current style.

- Avoid storing `_aday`, `_fday`, `_pday`, `_amon`, `_fmon`, `_pmon`, `_pmhour`
  and `_pm` in memory for every instance but look them up dynamically based on
  `_dayoffset`, `_month` and `_hour`. This saves another 150 bytes of memory
  per DateTime instance.

- Moved various internal parsing related class variables to module constants.

- No longer provide the `DateError`, `DateTimeError`, `SyntaxError` and
  `TimeError` exceptions as class attributes, import them from their canonical
  `DateTime.interfaces` location instead.

- Removed deprecated `_isDST` and `_localzone` class variables.

- Moved pytz cache from `DateTime._tzinfo` to a module global `_TZINFO`.

- Make DateTime a new-style class and limit its available attributes via a
  slots definition. The pickle size increases to 110 bytes thanks to the
  `ccopy_reg\n_reconstructor` stanza. But the memory size drops from 3kb to
  500 bytes for each instance.

3.0a1 (2011-05-06)
------------------

- Reordered some calculations in `_calcIndependentSecondEtc` to preserve more
  floating point precision.

- Optimized the pickled data, by only storing a tuple of `_micros` and time
  zone information - this reduces the pickle size from an average of 300 bytes
  to just 60 bytes.

- Optimized un-pickling, by avoiding the creation of an intermediate DateTime
  value representing the current time.

- Removed in-place migration of old DateTime pickles without a `_micros` value.

- Removed deprecated support for using `DateTime.__cmp__`.

- Take time zone settings into account when comparing two date times for
  (non-) equality.

- Fixed (possibly unused) _parse_iso8601 function.

- Removed unused import of legacy DateTimeZone, strftime and re.
  Remove trailing whitespace.

- Removed reference to missing version section from buildout.

2.12.7 (2012-08-11)
-------------------

- Added forward compatibility with DateTime 3 pickle format. DateTime
  instances constructed under version 3 can be read and unpickled by this
  version. The pickled data is converted to the current versions format
  (old-style class / no slots). Once converted it will be stored again in the
  old format. This should allow for a transparent upgrade/downgrade path
  between DateTime 2 and 3.

2.12.6 (2010-10-17)
-------------------

- Changed ``testDayOfWeek`` test to be independent of OS locale.

2.12.5 (2010-07-29)
-------------------

- Launchpad #143269: Corrected the documentation for year value
  behavior when constructing a DateTime object with three numeric
  arguments.

- Launchpad #142521: Removed confusing special case in
  DateTime.__str__ where DateTime instances for midnight
  (e.g. '2010-07-27 00:00:00 US/Eastern') values would
  render only their date and nothing else.

2.12.4 (2010-07-12)
-------------------

- Fixed mapping of EDT (was -> 'GMT-0400', now 'GMT-4').

2.12.3 (2010-07-09)
-------------------

- Added EDT timezone support. Addresses bug #599856.
  [vangheem]

2.12.2 (2010-05-05)
-------------------

- Launchpad #572715:  Relaxed pin on pytz, after applying a patch from
  Marius Gedminus which fixes the apparent API breakage.

2.12.1 (2010-04-30)
-------------------

- Removed an undeclared testing dependency on zope.testing.doctest in favor of
  the standard libraries doctest module.

- Added a maximum version requirement on pytz <= 2010b. Later versions produce
  test failures related to timezone changes.

2.12.0 (2009-03-04)
-------------------

- Launchpad #290254: Forward-ported fix for '_micros'-less pickles from
  the Zope 2.11 branch version.

2.11.2 (2009-02-02)
-------------------

- Include *all* pytz zone names, not just "common" ones.

- Fix one fragile doctest, band-aid another.

- Fix for launchpad #267545: DateTime(DateTime()) should preserve the
  correct hour.

2.11.1 (2008-08-05)
-------------------

- DateTime conversion of datetime objects with non-pytz tzinfo. Timezones()
  returns a copy of the timezone list (allows tests to run).

- Merged the slinkp-datetime-200007 branch: fix the DateTime(anotherDateTime)
  constructor to preserve timezones.

2.11.0b1 (2008-01-06)
---------------------

- Split off from the Zope2 main source code tree.
