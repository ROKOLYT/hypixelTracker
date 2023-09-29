import sqlite3
import requests
from datetime import datetime

# Ensure that table exists
connection = sqlite3.connect('bazaar.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lastUpdated TEXT,
    productId TEXT NOT NULL,
    sellPrice FLOAT,
    sellVolume INT,
    sellMovingWeek INT,
    sellOrders INT,
    buyPrice FLOAT,
    buyVolume INT,
    buyMovingWeek INT,
    buyOrders INT
    )""")

connection.commit()
connection.close()

"""
STRUCTURE
api.hypixel.net/skyblock.bazaar

success: bool,
lastUpdated: int,
products: {
    productId: {
        sell_summary: [],
        buy_summary: [],
        quick_status: {
            productId: str,
            sellPrice: float,
            sellVolume: int,
            sellMovingWeek: int,
            sellOrders: int,
            buyPrice: float,
            buyVolume: int,
            buyMovingWeek: int,
            buyOrders: int
        }
    }
}
"""
class bazaar_api():
    def __init__(self):
        self.last_updated = None
        self.url = "https://api.hypixel.net/"
        
    def update_data(self) -> bool:
        # Call API
        endpoint = "skyblock/bazaar"
        res = requests.get(self.url + endpoint)
        res = res.json()
        
        # Check for success
        if res["success"] is True:
            
            self.update_data_base(products_data=res["products"])
            return True
        return False
                     
    def update_data_base(self, products_data: dict) -> None:
        # Connect database
        connection = sqlite3.connect("bazaar.db")
        cursor = connection.cursor()
        
        # Get current time and date
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
        # Update database
        for product in products_data.values():
            data = product["quick_status"]
            
            cursor.execute("""INSERT INTO data(
                lastUpdated,
                productId,
                sellPrice,
                sellVolume,
                sellMovingWeek,
                sellOrders,
                buyPrice,
                buyVolume,
                buyMovingWeek,
                buyOrders)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (dt_string,
                str(data["productId"]).strip(),
                float(data["sellPrice"]),
                int(data["sellVolume"]),
                int(data["sellMovingWeek"]),
                int(data["sellOrders"]),
                float(data["buyPrice"]),
                int(data["buyVolume"]),
                int(data["buyMovingWeek"]),
                int(data["buyOrders"])))
    
        connection.commit()
        connection.close()
       