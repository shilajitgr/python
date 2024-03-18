The Solution to the "fair-billing" problem has been provided in the fair-billing-solution.py 
file which can be executed as follows:

    python3 fair-billing-solution.py <path of the log file>


All the methods have been annotated and so have been the critical code blocks.

The assumption employed to code the solution is specified right after the import statements.

Detailed Explanation of the code:

1) Structural:

The "CheckInput()" class has been created to extract and verify the commandline input received.

The "SummarizeInput()" class, which inherits and expands upon the functionalities of 
"CheckInput()" class by parsing the log file, validating each line in the file and summarizing 
the details of each user's session details.

The global variable "USER_INFO_TEMPLATE" is providing the template for storing information 
relation to each user's sessions.

2) Behavioural:

On executing the program, at first the "__init__()" method of "CheckInput()" checks if total 
cmdline args is equal to 2, if so then extracts the 
commandline argument else sets "print_help" instance variable to True.

Then "print_help_text()" method prints help text if "print_help" instance variable to set True
or the path provided in the cmdline args is not a file, in either of the stated cases True is 
returned otherwise False is returned. In this function, the boolean value returned acts as an 
indicator for the operations to proceed or stop based on whether a help text was printed or not.

After the cmdline argument is validated, "create_summary()" method is called to read each line
from the given path one line at a line. I decided to read lines one by one considering large
log files that may have millions of lines, as reading the entire file in one go will not work well
as the file size increases.

Each line that is read is split using space(" ") as delimiter, is passed to "line_valid()" 
method, which checks in the following order and returns false if any of the checks pass:

    a) length of list of items is not equal to 3
    b) if time in the list is not convertible into a datetime.time object
    c) if the 2nd element in the list is not alphanumeric
    d) if the last item in the list is not equal to "Start" or "End"

if none of the above checks pass, then the line is considered valid.

Whatever time is specified in the first valid line, that time is used as the absolute start time.
Then the "setdefault()" sets the deep-copied value of "USER_INFO_TEMPLATE" as the value for 
the user mentioned in the line. If the user already exists in the "summary" instance variable 
then, the currently stored information related to user is returned.

The reason why deep-copied value of "USER_INFO_TEMPLATE" is being set as value for new users is
that without deep copying the global variable, all users' details will point to the same memory
location, resulting in an incorrect output.

Then the absolute end time is updated each time a valid line is read from the log file since 
each valid line is chronologically ordered.

Now based on session status 3 flows are created:

    a) Add 'Start' time to the user's timestamp list.
                    
    b) If 'End' time is found then pop the first entry from user's timestamp list 
       and get timedelta between the end time and the popped value and add it to the 
       'session_length', then increment 'session_count'.
                    
    c) If 'End' time is found when user's timestamp list is empty then use 
       absolute start time to get the timedelta then add it to 'session_length' 
       and increment 'session_count'.

Now, in "close_in_progress_sessions()" method, first it is checked if the "summary" instance 
variable is empty, if so then the operation for this method is stopped right there, since no 
valid session details were registed in the mentioned variable.

If any "Start" times remain in timestamp list for any user, the timedelta is calculated with
absolute end time and then this time is added to "session_length" and "session_count" is 
incremented.

Then finally, "print_result()" is called to print the output in the required format.


Conclusion:

This solution has been written keeping in mind:

1) Scalability - Hence the reading is performed line by line
2) Performace - Hence the time complexity of the solution is O(n).
3) Separation of Responsibilities principle - Hence grouping the set of Responsibilities into two classes -

                                              CheckInput - which reads and verifies the commandline argument
                                              SummarizeInput - which operates on the data present in the log file

