"""
Importing pandas and matplotlib.pyplot modules help in 
read the excel file and plot the graphs using the required 
data
"""
import pandas as pd 
import matplotlib.pyplot as plt

# read file into dataframe and printing the DataFrame
df_gdp = pd.read_excel("Industry.xlsx")
print(df_gdp)

#Defining the Function for plotting Line plot.
def LinePlot(Country1,Country2,Country3,Country4) :

    """"Plotting four countries with labels"""
    plt.figure()
    # plot the four countries with labels
    plt.plot(df_gdp["YEAR"], df_gdp[Country1], label=Country1)
    plt.plot(df_gdp["YEAR"], df_gdp[Country2], label=Country2)
    plt.plot(df_gdp["YEAR"], df_gdp[Country3], label=Country3)
    plt.plot(df_gdp["YEAR"], df_gdp[Country4], label=Country4)
    
    #Setting labels and showing the legends
    plt.xlim(2006,2015)
    plt.ylim(17,85)
    plt.xlabel("% of GDP from 2006 to 2015")
    plt.ylabel("% of GDP")
    plt.title("Percentage of GDP through Industry") 
    plt.legend(title="COUNTRIRS",edgecolor = "brown")#coloring the boundary
    plt.savefig("LinePlot.png")#Saving the line plot
    plt.show()
    return #returing the function

#Function for plotting Bar Graph
def BarPlot(Width,Height):
    
    Ex_goods_services = pd.read_excel("Export_goods_Services.xlsx")
    print(Ex_goods_services)
    """Plotting countries with labels"""
    plt.figure(figsize=(Width,Height))# here height and width can be called by the function
    Ex_goods_services.plot(x='Year', kind='bar')
    
    #Setting labels and showing the legends
    plt.ylim(0,87)
    plt.title('Export Of Goods and Services In %GDP')
    plt.xlabel("Years From 2011 to 2015")
    plt.ylabel("% of GDP")
    plt.legend(title="COUNTRIRS",edgecolor = "Black",loc = "upper right")
    plt.show()
    return #returing the function

#Function for plotting Pie Chart
def PieGraph(GDP,YEAR):

    Gross_Cap= pd.read_excel("Gross_Capital_Formation.xlsx")
    print(Gross_Cap)
    
    # pie chart for the seven countries
    """Plotting pie chart for with for the countries"""
    plt.figure()
    plt.pie(Gross_Cap[GDP], labels = Gross_Cap['country'], autopct='%1.1f%%' , pctdistance = 0.5 , 
       labeldistance = 1.1,wedgeprops = {'linewidth' : 1.0,'edgecolor' : 'white'} )
    
    plt.title("Gross Capital Formation In % of GDP " + YEAR)
    plt.show()
    return  #returing the function


LinePlot("Azerbaijan","Botswana","Canada","Ireland") #Calling the defined function for Line Plot
BarPlot(10,8) # Calling the defined function for Bar Plot
PieGraph("GDP in 2005","2005")#Calling defined function for Pie Chart of the Year 2005
PieGraph("GDP in 2015","2015")#Calling defined function for Pie Chart of the Year 2015

