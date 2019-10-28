import time
import datetime
import pandas as pd
import numpy as np
import statistics as st
import calendar


def AskForCity():
# Asks user to choose analyze it data   
    
    # get user input for city
    #lower if the input was in any format
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Wich city would you like to see its data\nChicago, New York, or Washington?\n').title()
    
    # call each city data from the csv files
    if city == 'Chicago':
        return 'chicago.csv'
    elif city == 'New York' :
        return 'new_york_city.csv'
    elif city == 'Washington' :
        return 'washington.csv'
    else:
        print("\nI'm sorry, I'm not sure which city you're referring to. Let's try again.")
        return AskForCity()
        
def AskForTime():
   # Asks the user for a time period
        
    TimePeriod = input('\nWould you like to filter the data by Month, Day, or None for no time filtering.\n').lower()

    # if user choose filtring by month
    if TimePeriod == 'month' :
        return ['month', AskForMonth()]
    
    # if user choose filtring by day    
    elif TimePeriod == 'day':
        return ['day', AskForDay()]

    # if user didnot choose filtring way    
    elif TimePeriod == 'none' :
        return ['none', 'no filter']
        
    else:
        print('\nSorry you ask for data wich is not avilable.\nLet\'s try again.')
        return AskForTime()


def AskForMonth():
    # Asks the user for a month

    month = input('\nWhich month you are looking for?\nJanuary, February, March, April, May, or June?\n').title()

    if month == 'January' or month == 'Jan':
        return '01'

    elif month == 'February' or month == 'Feb':
        return '02'

    elif month == 'March' or month == 'Mar':
        return '03'

    elif month == 'April' or month == 'Apr':
        return '04'

    elif month == 'May' :
        return '05'

    elif month == 'June' or month == 'Jun':
        return '06'

    else:
        print('\nSorry you ask for data wich is not avilable.\nLet\'s try again.')
        return AskForMonth()

def AskForDay():
    # Asks the user for a day of the week
     
    DayOfTheWeek = input('\nWhich day of the week? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday?\n').title()
    if DayOfTheWeek == 'Sunday' or DayOfTheWeek == 'Sun':
        return 0

    elif DayOfTheWeek == 'Monday' or Day OfTheWeek == 'Mon':
        return 1

    elif DayOfTheWeek == 'Tuesday' or DayOfTheWeek == 'Tue':
        return 2

    elif DayOfTheWeek == 'Wednesday' or DayOfTheWeek =='Wed':
        return 3

    elif DayOfTheWeek == 'Thursday' or DayOfTheWeek == 'Thu':
        return 4

    elif DayOfTheWeek == 'Friday' or DayOfTheWeek == 'Fri':
        return 5

    elif DayOfTheWeek == 'Saturday' or DayOfTheWeek == 'Sat':
        return 6

    else:
        print('\n Sorry you ask for data wich is not avilable. \nLet\'s try again.')
        return AskForDay()

def PopularMonth(df):
   #This function returns the month with the most trips.

    #Count the number of trips in each month
    TripsByMonth = df.groupby('Month')['Start Time'].count()
    return "Most popular month for starting time: " + calendar.month_name[int(TripsByMonth.sort_values(ascending=False).index[0])]
    #Sort the results from highest to lowest

def PopularDay(df):
    #This function returns the day with the most trips.

    #Count the number of trips in each day
    TripsByDay = df.groupby('Day of Week')['Start Time'].count()
    return "Most popular day of the week for starting time: " + calendar.day_name[int(TripsByDay.sort_values(ascending=False).index[0])]
    #Sort the results from highest to lowest

def PopularHour(df):
   #This function returns the month with the most trips.

    #Count the number of trips in each hour
    TripsByHourOfTheDay = df.groupby('Hour of Day')['Start Time'].count()

    MostPopularHourInt = TripsByHourOfTheDay.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(MostPopularHourInt, "%H")
    return "Most popular hour of the day for starting time: " + d.strftime("%I %p")
    #Sort the results from highest to lowest  

def TripDuration(df):
    #This function returns the total trip duration and average trip duration

    #Count the numbers of trips
    TotalTripDuration = df['Trip Duration'].sum()
   
    #Count the avrege of trips
    AvgTripDuration = df['Trip Duration'].mean()
    
    #Count all trips duration 
    m, s = divmod(TotalTripDuration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    TotalTripDuration = "\nTotal trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)

    #Count avrege of trips duration 
    m, s = divmod(AvgTripDuration, 60)
    h, m = divmod(m, 60)
    AvgTripDuration = "Average trip duration: %d hrs %02d min %02d sec" % (h, m, s)
    return [TotalTripDuration, AvgTripDuration]

def PopularStations(df):
    #This function returns the most popular start and end stations
   
    #Count star and End stations
    CountStartStation = df.groupby('Start Station')['Start Station'].count()
    CountEndtStation = df.groupby('End Station')['End Station'].count()
    
    #Sort star and End stations
    SortStartStation = CountStartStation.sort_values(ascending=False)
    SortEndtStation = CountEndtStation.sort_values(ascending=False)
     
    #Count all the trips are in
    TotalTrips = df['Start Station'].count()
    
    #Calculat the mod for the end and start station
    MostPopularStartStation = "\nMost popular start station: " + SortStartStation.index[0] + " (" + str(SortStartStation[0]) + " trips, " + '{0:.2f}%'.format(((SortStartStation[0]/TotalTrips) * 100)) + " of trips)"
    MostPopularEndStation = "Most popular end station: " + SortEndtStation.index[0] + " (" + str(SortEndtStation[0]) + " trips, " + '{0:.2f}%'.format(((SortEndtStation[0]/TotalTrips) * 100)) + " of trips)"
    
    return [MostPopularStartStation, MostPopularEndStation]

def PopularTrip(df):
    #This function returns the most popular trip the combination of start station and end station
    
    #Count the most popular combination of start and end
    TripCounts = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    
    #Sort the trip numbersSort
    SortTripStations = TripCounts.sort_values(ascending=False)
    
    #Count all the trips are in 
    TotalTrips = df['Start Station'].count()
    
    return "Most popular trip: " + "\n  Start station: " + str(SortTripStations.index[0][0]) + "\n  End station: " + str(SortTripStations.index[0][1]) + "\n  (" + str(SortTripStations[0]) +  " trips, " + '{0:.2f}%'.format(((SortTripStations[0]/TotalTrips) * 100)) + " of trips)"

def Users(df):
    #This function returns the number of trips by user type
   
    CountUsersType = df.groupby('User Type')['User Type'].count()
    return CountUsersType

def Gender(df):
    #This function returns the number of trips by gender
    
    CountGender = df.groupby('Gender')['Gender'].count()
    return CountGender

def YearOfBirth(df):
     #This function returns the oldest birth year, the most recent birth year, and the most common birth year

    #Count the earlist year of birth
    EarliestBirthYear = "Earliest birth year: " + str(int(df['Birth Year'].min()))
    
    #Count the year of birth
    MostRecentBirthYear = "Most recent birth year: " + str(int(df['Birth Year'].max()))
    CountYearOfBirth = df.groupby('Birth Year')['Birth Year'].count()
    
    #Sort the years of birth
    SortYearsOfBirth = CountYearOfBirth.sort_values(ascending=False)
    
    #Count all the trips are in 
    TotalTrips = df['Birth Year'].count()

    MostCommonYearOfBirth = "Most common birth year: " + str(int(SortYearsOfBirth.index[0])) + " (" + str(SortYearsOfBirth.iloc[0]) + " trips, " + '{0:.2f}%'.format(((SortYearsOfBirth.iloc[0]/TotalTrips) * 100)) + " of trips)"
    return [EarliestBirthYear, MostRecentBirthYear, MostCommonYearOfBirth]


def DisplayData(df, CurrentLine):
    #Displays five lines of data if the user specifies that they would like to.
    
    Display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    Display = Display.lower()

    #After displaying five lines, ask the user if they would like to see five more.
    if Display == 'yes' or Display == 'y' :

        print(df.iloc[CurrentLine:CurrentLine+5])
        CurrentLine += 5
        return DisplayData(df, CurrentLine)
    
    #Continues asking until they say stop.    
    else:
        print('I hope you enjoy it. see you next tim')
    
def Statistics():
   #Calculates and prints out the descriptive statistics about a city and time period
    
    # Filter by city (Chicago, New York, Washington)
    City = AskForCity()
    City_df = pd.read_csv(City)
    
    def GetDayOfWeek(str_date):
       #Takes a date in the format yyyy-mm-dd and returns an integer
          
    
        DateObj = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        #parse string in format yyyy-mm-dd and create date object based on those values.

        return DateObj.weekday() 
        #return the day of the week that that date was

    City_df['Day of Week'] = City_df['Start Time'].apply(GetDayOfWeek)
    City_df['Month'] = City_df['Start Time'].str[5:7]
    City_df['Hour of Day'] = City_df['Start Time'].str[11:13]
    #store day of week, month, and hour of day values for each

    TimePeriod = AskForTime()
    FilterPeriod = TimePeriod[0]
    FilterPeriodValue = TimePeriod[1]
    FilterPeriodLabel = 'No filter'
    # Filter by time period that the user specifies (month, day, none)


    if FilterPeriod == 'none':
       Filtered_df = City_df

    elif FilterPeriod == 'month':
         Filtered_df = City_df.loc[City_df['Month'] == FilterPeriodValue]
         FilterPeriodLabel = calendar.month_name[int(FilterPeriodValue)]

    elif FilterPeriod == 'day':
         Filtered_df = City_df.loc[City_df['Day of Week'] == FilterPeriodValue]
         FilterPeriodLabel = calendar.day_name[int(FilterPeriodValue)]

    #Print a heading that specifies which city this data is for and any filters that were applied
    print('\n')
    print(City[:-4].upper().replace("_", " ") + ' -- ' + FilterPeriodLabel.upper())
    print('-------------------------------------')

    #To give some context, print the total number of trips for this city and filter
    print('Total trips: ' + "{:,}".format(Filtered_df['Start Time'].count()))

    #What is the most popular month for start time?
    if FilterPeriod == 'none' or FilterPeriod == 'day':
        print(PopularMonth(Filtered_df))

    #What is the most popular day of week for starting time?
    if FilterPeriod == 'none' or FilterPeriod == 'month':
        print(PopularDay(Filtered_df))

    #What is the most popular hour of day for starting time?
    print(PopularHour(Filtered_df))

    #What is the total trip duration and average trip duration?
    TripDurationStats = TripDuration(Filtered_df)
    print(TripDurationStats[0])
    print(TripDurationStats[1])

    #What is the most popular start station and most popular end station?
    MostPopularStations = PopularStations(Filtered_df)
    print(MostPopularStations[0])
    print(MostPopularStations[1])

    #What is the most popular trip?
    print(PopularTrip(Filtered_df))

    # What are the counts of each user type?
    print('')
    print(Users(Filtered_df))

    if City == 'chicago.csv' or City == 'new_york_city.csv': #only those two files have this data
        #What are the counts of gender?
        print('')
        print(Gender(Filtered_df))

        #What are the earliest, most recent and most popular birth years?
        BirthYearsData = YearOfBirth(Filtered_df)
        print('')
        print(BirthYearsData[0])
        print(BirthYearsData[1])
        print(BirthYearsData[2])

    #Display five lines of data at a time if user specifies that they would like to
    DisplayData(Filtered_df, 0)

    #Restart
    def RestartQuestion():
        #Asks the user for restarting

        Restart = input('\nWould you like to restart? Type \'yes\' or \'no\'. (If you say no it will end the program.)\n')

        if Restart.lower() == 'yes':
            Statistics()

        elif Restart.lower() == 'no':
            return

        else:
            print("\nI'm not sure if you wanted to restart or not. Let's try again.")
            return RestartQuestion()

    RestartQuestion()


if __name__ == "__main__":
    Statistics()
#This is The Main function
