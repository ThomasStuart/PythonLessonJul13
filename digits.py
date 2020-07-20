def getRidOfLastNum( n ):
    return n // 10

def getLastNumber( n ):
    return n % 10

# What operator and number do the job
n = 2342
print ( getRidOfLastNum( n ) )   #  234
print ( getLastNumber( n ) )     #  2

m = 41
print ( getRidOfLastNum( m ) )   #  4
print ( getLastNumber( m ) )     #  1

k = 128
print ( getRidOfLastNum( k ) )   #  12
print ( getLastNumber( k ) )     #  8



def digits( number ):
    nums = []

    # Process that we repeat,  when do we stop ??
    while number > 0:
        # take off the last number
        nums.append( getLastNumber( number ) )
        # get ride of the last number
        number = getRidOfLastNum( number )

    # before we return nums, we have to reverse the list
    nums.reverse()
    
    return nums


print( digits(2342) ) # [2, 3, 4, 2]
print( digits(1234) ) # [1 , 2, 3, 4]
print( digits(12))    # [1 , 2]
print( digits(9) )    # [ 9 ]
