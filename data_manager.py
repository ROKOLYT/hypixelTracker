import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

def plot_graph(item: str) -> bool:
    res = fetch_data(item)
    
    dates_raw = [row[1] for row in res]
    prices = [int(row[7]) for row in res]
    
    dates = [datetime.strptime(date, "%d/%m/%Y %H:%M:%S") for date in dates_raw]
    
    fig = plt.figure()
    timer = fig.canvas.new_timer(interval=10000)
    timer.add_callback(plt.close)
    
    plt.plot(dates, prices, marker='o', linestyle='-')

    # Customize the x-axis to show dates nicely
    plt.gcf().autofmt_xdate()

    # Add labels and a title
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price vs. Date')
    
    timer.start()

    # Display the plot
    plt.show()
    return True
    
def fetch_data(item: str) -> list:
    connection = sqlite3.connect("bazaar.db")
    cursor = connection.cursor()
    
    cursor.execute("""SELECT * FROM data WHERE productId=?""", (item,))
    res = cursor.fetchall()
    connection.close()
    
    return res

def clean_tests() -> bool:
    connection = sqlite3.connect("bazaar.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE * FROM data WHERE productId=Dummy")
    connection.commit()
    connection.close()
    
    return True
    
if __name__ == "__main__":
    res = fetch_data("Dummy")
    
    for row in res:
        for column in row:
            print(column, end="   ")
            
        print("")