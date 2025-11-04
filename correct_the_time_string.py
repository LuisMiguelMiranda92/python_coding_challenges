"""
A new task for you!

You have to create a method, that corrects a given time string.
There was a problem in addition, so many of the time strings are broken.
Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.
Examples
"09:10:01" -> "09:10:01"  
"11:70:10" -> "12:10:10"  
"19:99:99" -> "20:40:39"  
"24:01:01" -> "00:01:01"  
If the input-string is null or empty return exactly this value! 
(empty string for C++) If the time-string-format is invalid, return null. (empty string for C++)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
"""
def time_correct(t):
    # 1. Handle null or empty string
    if not t: 
        return t

    # 2. Check for "H:M:S" structure
    parts = t.split(':')
    if len(parts) != 3:
        return None

    # --- NEW VALIDATION BLOCK ---
    # 3. Check if each part is exactly 2 digits
    for part in parts:
        # Fails for '6' (len != 2)
        # Fails for '+4' (not isdigit())
        # Fails for 'aa' (not isdigit())
        if len(part) != 2 or not part.isdigit():
            return None
    # --- END NEW VALIDATION ---
    
    # 4. If we get here, format is valid. Now we can safely convert and calculate.
    try:
        h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
        
        # Correct seconds and add extra minutes
        m += s // 60
        s = s % 60
        
        # Correct minutes and add extra hours
        h += m // 60
        m = m % 60
        
        # Correct hours
        h = h % 24
        
        return '%02d:%02d:%02d' % (h, m, s)
        
    except:
        # This will now only catch truly bizarre inputs
        return None