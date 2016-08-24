Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")



def make_readable(seconds):
    HH = int(seconds / 3600)
    HS = HH * 3600
    MM = int((seconds - HS) / 60)
    MS = MM * 60
    SS = int(seconds - HS - MS)
    return "%s:%s:%s" % (str(HH).zfill(2), str(MM).zfill(2), str(SS).zfill(2))

    
