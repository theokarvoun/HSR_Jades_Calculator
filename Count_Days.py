import datetime

class Calc_Days:
    def current_date():
        return datetime.datetime.today()
    def calc_delta(date_str):
        date = datetime.datetime.strptime(date_str,"%Y-%m-%d")
        return (date - Calc_Days.current_date()).days

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
        return int((Calc_Weeks.get_end_date(end_date)-Calc_Weeks.current()).days/7)

if __name__ == "__main__":
    test = Calc_Days
    print(Calc_Weeks.calc_delta('2024-08-30'))
    #print(test.calc_delta('2024-08-30'))