import sys
import os
import copy
from datetime import datetime

"""
    Assumptions:
    1) The following line is referring to first and last valid record in the 
    logs as the absolute "Start" time and "End" time respectively:
    
        Where there is an “End” with no possible matching start, the start time should be
    assumed to be the earliest time of any record in the file. Where there is a “Start” with no possible matching “End”, the end time
    should be assumed to be the latest time of any record in the file.
"""

USER_INFO_TEMPLATE = {
    'timestamp': [],
    'session_count': 0,
    'session_length': 0
}

    
class CheckInput():
    
    def __init__(self):
        self.print_help = False
        self.log_path = ""
        if len(sys.argv) == 2:
            self.log_path = sys.argv[1]
        else:
            self.print_help = True
            
    def print_help_text(self) -> bool:
        """
        Prints help text for the program if incorrect cmdline args passed
        """
        return_val = False
        if self.print_help:
            print(
            """
            Please execute the program in the following format:
            
            ./fair-billing-solution.py <absolute path of log file>
            """
                  )
            return_val = True
            
        elif not os.path.isfile(self.log_path):
            
            print(
            """
            Please pass path of a file as argument.
            """
                  )
            
            return_val = True
        
        return return_val


class SummarizeInput(CheckInput):
    
    def __init__(self):
        super().__init__()
        self.summary = {}
        self.absolute_start_time = None
        self.absolute_end_time = None
        
        
    def create_summary(self) -> None:
        """
        Iterates over each line in log file, validates it and if valid updates/creates 
        the user session info
        """        
        with open(self.log_path, 'r') as logfd:
            for line in logfd:
                line = line.strip().split(" ")
                if self.line_valid(line):
                    
                    """
                    Add 'Start' time to the timestamp list.
                    
                    If 'End' time is found then get the first entry in timestamp 
                    and get timedelta then add it to the 'session_length' and 
                    increment 'session_count'.
                    
                    If 'End' time is found when timestamp list is empty then use 
                    absolute_start_time to get the timedelta then add it to 'session_length' 
                    and increment 'session_count'.
                    """
                    
                    if not self.absolute_start_time:
                        self.absolute_start_time = line[0]
                        
                    user_data = self.summary.setdefault(line[1], copy.deepcopy(USER_INFO_TEMPLATE))
                    
                    self.absolute_end_time = line[0]
                    
                    if line[2] == "Start":
                        user_data["timestamp"].append(line[0])
                        
                    if line[2] == "End":
                        if user_data["timestamp"]:
                            start_time = user_data["timestamp"].pop(0)
                        else:
                            start_time = self.absolute_start_time
                        
                        start_time_obj = datetime.strptime(start_time, '%H:%M:%S').time()
                        end_time_obj = datetime.strptime(line[0], '%H:%M:%S').time()
                        user_data['session_length'] +=(datetime.combine(datetime.now().date(), end_time_obj)
                                                        - datetime.combine(datetime.now().date(), start_time_obj)).seconds
                        user_data['session_count'] += 1
        
        
    def close_in_progress_sessions(self) -> None:
        """
        Iterates over all users information to find and calculate usage for
        any in-progress sessions
        """
        if not self.summary:
            return
        
        end_time_obj = datetime.strptime(self.absolute_end_time, '%H:%M:%S').time()
        for _, info in self.summary.items():
            """
            close in-progress sessions using the latest valid time record and 
            get the timedelta then it to 'session_length' and increment 'session_count'
            """
            # if info['timestamp']:
            for time in info['timestamp']:
                time_obj = datetime.strptime(time, '%H:%M:%S').time()
                info['session_length'] += (datetime.combine(datetime.now().date(), end_time_obj)
                                           - datetime.combine(datetime.now().date(), time_obj)).seconds
                info['session_count'] += 1
                
    
    def print_result(self) -> None:
        """
        Prints the summary in the prescribed output format
        """
        if not self.summary:
            return
        
        for user, info in self.summary.items():
            print(f"{user} {info['session_count']} {info['session_length']}")
    
    
    def line_valid(self, line: list) -> bool:
        """
        Checks if the passed list is valid as per the defined format

        Args:
            line (list): List of items in any line read from the log file

        Returns:
            bool: True if the line is valid as per the defined format else False
        """
        if len(line) != 3:
            
            return False
        
        time = line[0]
        if not self.time_valid(time):
            
            return False
        
        if not line[1].isalnum():
            
            return False
            
        if not (line[-1] == "Start" or line[-1] == "End"):
            
            return False
        
        return True
        
    def time_valid(self, line: str) -> bool:
        """
        Checks if the passed string is representing a valid time

        Args:
            line (str): String to be checked

        Returns:
            bool: True if the time represented by line is valid else False
        """
        try:
            datetime.strptime(line, '%H:%M:%S').time()
            return True
        except ValueError:
            return False


si_obj = SummarizeInput()

if not si_obj.print_help_text():
    
    si_obj.create_summary()
    si_obj.close_in_progress_sessions()
    si_obj.print_result()
