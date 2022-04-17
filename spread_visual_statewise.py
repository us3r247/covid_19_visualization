import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation
import pandas as pd

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.options.display.width = None

# huge db with daily covid data for all indian states
data = pd.read_csv('covid_19_ india.csv')

# user input
state = input("enter state name: ")

# part of data set i.e. only the part containing info for user's input
subset = data[data['Name of State / UT'] == state]

# constants###########################################
# pixels per
xfac = 262.1/(77.1055-66.307)
yfac = 605.2/(28.654-5.902)
left_lim = 66.307
bott_lim = 5.902
ratio1 = (1600/data['Size'].max())  #(max mappable/size of largest state)
######################################################

long = list(subset['Longitude'])[1]
lat = list(subset['Latitude'])[1]
dates = list(subset['Date'])
cases = list(subset['Total Confirmed cases'])


img = mpimg.imread("india base map.gif")

x = (long-left_lim)*xfac
y = (lat-bott_lim)*yfac


# returns list of areas over period of time

def area_of_circle(curr_cases_list):

    max_cases = subset['Total Confirmed cases'].max()
    state_area = list(subset['Size'])[1]

    ###constant################################

    ratio2 = (state_area/max_cases)  #curr_state size / max cases in curr_state

    ###########################################

    curr_area_list = []  # empty list

    for x in curr_cases_list:
        curr_area_list.append(x*ratio1*ratio2)

    return curr_area_list

area_wrt_cases = area_of_circle(cases)


def animate(counter):
    plt.cla()
    plt.imshow(img[::-1], origin="lower")
    area = area_wrt_cases[counter]
    plt.title(f'Covid cases ({cases[counter]}) in {state} on {dates[counter]}')
    plt.scatter(x,y,s=area, color='red', alpha=.5)

animator = FuncAnimation(plt.gcf(),animate,interval=1,frames=len(area_wrt_cases) ,repeat=False)


plt.show()



