import os

# open login.html directly
os.system("start login_gui.html")
import monitoring_engine

admin_name = textBox1.get()
admin_password = textBox2.get()
mobile = textBox3.get()

monitoring_engine.read_thingspeak_data(admin_name, admin_password, mobile)