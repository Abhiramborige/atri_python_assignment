from .atri import Atri
from fastapi import Request, Response
from atri_utils import *
from backend.mongo_adapter import MongoDbAdapter

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    adapter=MongoDbAdapter()
    bar_data=adapter.get_data()
    at.unique_view_chart.custom.xAxis = {"key": "Site name", "show": True}
    at.unique_view_chart.custom.yAxis = {"key": "Unique view", "show": True}
    filtered_bar_data=[]
    for i in bar_data:
        filtered_bar_data.append({"x":i["site"],"category1":i["unique_views"]})
    print(filtered_bar_data)
    at.unique_view_chart.custom.data=filtered_bar_data
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    # Add your code here to insert data in the Bar chart
    # Show site name on the x-axis of bar chart and unique view on y axis
    # You can access the bar chart by at.unique_view_chart
    adapter=MongoDbAdapter()
    bar_data=adapter.get_data()
    at.unique_view_chart.custom.xAxis = {"key": "Site name", "show": True}
    at.unique_view_chart.custom.yAxis = {"key": "Unique view", "show": True}
    filtered_bar_data=[]
    for i in bar_data:
        filtered_bar_data.append({"x":i["site"],"category1":i["unique_views"]})
    print(filtered_bar_data)
    
    at.unique_view_chart.custom.data=filtered_bar_data
    pass