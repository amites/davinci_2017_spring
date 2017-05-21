# https://www.codewars.com/kata/simple-fun-number-270-evil-code-medal/train/python

def evil_code_medal(user_time, gold, silver, bronze):
    user_time, gold, silver, bronze = "00:30:00", "00:15:00", "00:45:00",  "01:15:00"
    user_list = user_time.split(':')
    gold_list = gold.split(':')
    silver_list = silver.split(':')
    bronze_list = bronze.split(':')

    # List Comprehension
    user_list = [int(n) for n in user_time.split(':')]

    # The long way
    # user_list = []
    # user_string_list = user_time.split(':')
    # for n in user_string_list:
    #     user_list.append(int(n))


    gold_list = [int(n) for n in gold.split(':')]
    silver_list = [int(n) for n in silver.split(':')]
    bronze_list = [int(n) for n in bronze.split(':')]


    # Brute force method 1

    # if user_list[0] > bronze_list[0]:
    #     logger.debug('you suck')
    #     return 'None'
    # elif user_list[1] > bronze_list[1]:
    #     logger.debug('you suck')
    #     return 'None'
    # condensed for sanity

    # Brute force Method 2
    user_seconds = (user_list[0] * 60 * 60) + (user_list[1] * 60) + user_list[2]
    gold_seconds = (gold_list[0] * 60 * 60) + (gold_list[1] * 60) + gold_list[2]
    silver_seconds = (silver_list[0] * 60 * 60) + (silver_list[1] * 60) + silver_list[2]
    bronze_seconds = (bronze_list[0] * 60 * 60) + (bronze_list[1] * 60) + bronze_list[2]

    # See below for alternative implementation
    if user_seconds > bronze_seconds:
        print 'You suck'
        return 'None'
    elif user_seconds >= silver_seconds:
        print 'You kinda suck'
        return 'Bronze'
    elif user_seconds >= gold_seconds:
        print "You're ok"
        return 'Silver'
    else:
        print 'You rock'
        return 'Gold'


    # Brute Force 3
    for medal, seconds in [["Gold", gold_seconds], ["Silver", silver_seconds], ["Bronze", bronze_seconds]]:
        if user_seconds < seconds:
            return medal
    return "None"


    # Brute Force 3
    for medal, seconds, message in [["Gold", gold_seconds, 'hurray'], ["Silver", silver_seconds, 'you ok'], ["Bronze", bronze_seconds, 'better luck next time']]:
        if user_seconds < seconds:
            print message
            return medal
    print 'You suck a lot'
    return "None"


# Cloned from answers -- yes this actually works
def evil_code_medal(user_time, gold, silver, bronze):
    for medal, time in [["Gold", gold], ["Silver", silver], ["Bronze", bronze]]:
        if user_time < time:
            return medal
    return "None"
