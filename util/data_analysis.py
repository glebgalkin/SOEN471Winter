from util.helpers import display_piechart_of_column


#todo in our cleanup for wind direction we will merge north and N etc. South and S
def display_ratios(total_accidents_data):
    display_piechart_of_column(total_accidents_data, 'Civil_Twilight')
    display_piechart_of_column(total_accidents_data, 'Nautical_Twilight')
    display_piechart_of_column(total_accidents_data, 'Astronomical_Twilight')
    display_piechart_of_column(total_accidents_data, 'Severity')
    display_piechart_of_column(total_accidents_data, 'State')
    display_piechart_of_column(total_accidents_data, 'Side')
    display_piechart_of_column(total_accidents_data, 'Wind_Direction')
    display_piechart_of_column(total_accidents_data, 'Precipitation(in)')
    display_piechart_of_column(total_accidents_data, 'Weather_Condition')
    display_piechart_of_column(total_accidents_data, 'Amenity')
    display_piechart_of_column(total_accidents_data, 'Bump')
    display_piechart_of_column(total_accidents_data, 'Crossing')
    display_piechart_of_column(total_accidents_data, 'Give_Way')
    display_piechart_of_column(total_accidents_data, 'Junction')
    display_piechart_of_column(total_accidents_data, 'No_Exit')
    display_piechart_of_column(total_accidents_data, 'Railway')
    display_piechart_of_column(total_accidents_data, 'Roundabout')
    display_piechart_of_column(total_accidents_data, 'Station')
    display_piechart_of_column(total_accidents_data, 'Stop')
    display_piechart_of_column(total_accidents_data, 'Traffic_Calming')
    display_piechart_of_column(total_accidents_data, 'Traffic_Signal')
    display_piechart_of_column(total_accidents_data, 'Turning_Loop')
    display_piechart_of_column(total_accidents_data, 'Sunrise_Sunset')
