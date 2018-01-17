
class Clock:

    def __init__(self,hrs=0,mins=0,secs=0):

        self.setClock(hrs,mins,secs)

    def setClock(self,hrs,mins,secs):

        if type(hrs)==int and 0<= hrs <24:
            self._clock_hours=hrs
        else:
            raise TypeError('Hours should be in between 0 and 24.')

        if type(mins)==int and 0<= mins <60:
            self.__clock_mins=mins
        else:
            raise TypeError('Minutes must be between 0 and 60.')

        if type(secs)==int and 0<= secs <60:
            self.__clock_secs= secs
        else:
            raise TypeError('Seconds must be between 0 and 60.')

    def __str__(self):
        return ':'.join([str(self._clock_hours),str(self.__clock_mins),str(self.__clock_secs)])

    def increment_clock(self):

        if self.__clock_secs==59:
            self.__clock_secs=0
            if self.__clock_mins==59:
                self.__clock_mins=0
                if self._clock_hours==23:
                    self._clock_hours=0
                else:
                    self._clock_hours+=1
            else:
                self.__clock_mins+=1
        else:
            self.__clock_secs+=1
            


class Calender:

    __max_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    
    @staticmethod
    def leapYear_or_not(year):
        return year%400==0 or (year%4==0 and year%100!=0)
    
    
    
    @staticmethod
    def valid_calender(date,month,year):
        #date_check=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        if type(date)!=int or type(month)!=int or type(year)!=int:
            return False
        
        if date<1 or ( 12 < month or month < 1) or year<1:
            return False

        if month==2 and Calender.leapYear_or_not(year) and date>29:
            return False
        
        if date>Calender.__max_days[month]:
            return False

        return True

    def __init__(self,date,month,year):

        if (self.valid_calender(date,month,year)):
            self.setCalender(date,month,year)
        else:
            raise TypeError('Enter valid entries')

    
    
    def setCalender(self,date,month,year):
        self.__calender_date=date
        self.__calender_month=month
        self.__calender_year=year


    def increment_calender(self):
        #max_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        max_days_of_month = Calender.__max_days[self.__calender_month]
        
        if self.__calender_month ==2 and Calender.leapYear_or_not(self.__calender_year):
            max_days_of_month += 1
        
        if self.__calender_date==max_days_of_month:
            self.__calender_date=1
            if self.__calender_month==12:
                self.__calender_month=1
                self.__calender_year+=1
            else:
                self.__calender_month+=1
        else:
            self.__calender_date+=1
            
    def __str__(self):
        return '-'.join([str(self.__calender_date),str(self.__calender_month),str(self.__calender_year)])


class CalenderClock(Clock,Calender):

    def __init__(self,date,month,year,hour,mins,sec):
        Clock.__init__(self,hour,mins,sec)
        Calender.__init__(self,date,month,year)

    def increment_clock(self):
        prev_hr = self._clock_hours
        Clock.increment_clock(self)
        now_hr=self._clock_hours

        if (now_hr<prev_hr):
            self.increment_calender()

    def __str__(self):
        return ' '.join([Calender.__str__(self),Clock.__str__(self)])


   
cc1=CalenderClock(17,1,2018,23,59,59)
print(cc1)
cc1.increment_clock()
print(cc1)

        
















            
    
