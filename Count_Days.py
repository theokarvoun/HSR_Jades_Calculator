import datetime
import math

class Calc_Days:
    def current_date():
        return datetime.datetime.today()
    def calc_delta(date_str):
        date = datetime.datetime.strptime(date_str,"%Y-%m-%d")
        return (date - Calc_Days.current_date()).days
    def calculate_days_difference(date1_str, date2_str, date_format="%Y-%m-%d"):
    # Convert the date strings to datetime objects
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
    
    # Calculate the difference between the two dates
        difference = date2 - date1
    
    # Return the difference in days
        return difference.days

class Calc_Weeks:
    def current():
        return datetime.datetime.today()
    def get_end_date(end_date):
        end_date = str(end_date)
        end_date_tokens = end_date.split('-')
        #print(end_date_tokens)
        return datetime.datetime(int(end_date_tokens[0]),int(end_date_tokens[1]),int(end_date_tokens[2]))
    def calc_delta(end_date) -> int:
        #print(Calc_Weeks.current())
        return math.floor((Calc_Weeks.get_end_date(end_date)-Calc_Weeks.current()).days/7)

if __name__ == "__main__":
    test = Calc_Days
    print(Calc_Weeks.calc_delta('2024-08-30'))
    print(Calc_Days.calculate_days_difference(date1_str='2024-08-12',date2_str='2024-08-30'))
    #print(test.calc_delta('2024-08-30'))