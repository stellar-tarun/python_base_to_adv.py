import time
# code-1
# print(time.time())

# code-2 Pauses the program for the given number of seconds.
# print("Wait for 2 seconds...")
# time.sleep(2)
# print("Done!")


#code-3 Converts a time expressed in seconds to a readable string.

# print(time.ctime())  # Current time
# Example: 'Mon Jun 23 10:30:15 2025'


# code-4 Returns the current time as a struct_time (like a named tuple).

# t = time.localtime()
# print(t)
# print("Year:", t.tm_year)



#code-5 High-resolution timer for measuring performance.

# start = time.perf_counter()
# # some code
# time.sleep(1)
# end = time.perf_counter()
# print("Elapsed:", end - start)



# code-6 Formats a struct_time into a readable string.

# now = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S", now))  # 2025-06-23 10:45:00


# code-7 Parses a string into a struct_time.
# t = time.strptime("2025-06-23", "%Y-%m-%d")
# print(t)

