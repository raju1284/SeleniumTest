""" This Class is used for Test Data configuration """
import os

class TestData:

    chrom_driver_exe = os.path.join(os.path.dirname(__file__), '..',)+"/Drivers/chromedriver_win32/chromedriver.exe"
    ie_driver_exe = os.path.join(os.path.dirname(__file__), '..',)+"/Drivers/IEDriverServer_Win32_4.0.0/IEDriverServer.exe"
    base_url = "http://moat.com/"
    SearchText = "Krux"
    SearchSaturn = "Saturn"
    SearchSaturdayMarker = "Saturday’s Market"
    SearchKrux = "Krux"
    NoofIteratons = 5
    SearchTextList = ["Saturn","Saturday's Market","Krux"]