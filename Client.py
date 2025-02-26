import tkinter as tk
import datetime
import paho.mqtt.client as mqtt
import socket

# fungsi callback untuk tombol "Kirim"
def send_message():
    message = message_input.get()  # ambil input dari textbox
    # kirim pesan ke topik "coba/user"
    client.on_publish=on_publish
    client.connect(broker, port)
    client.loop_start()
    client.publish(topic2, str(client._client_id.decode("utf-8"))+f" sent \"{message}\"")
    client.loop_stop()
#fungsi callback untuk tombol send your information data    
def send_message2():
    ip_address = socket.gethostbyname(socket.gethostname())
    client.on_publish=on_publish
    client.connect(broker, port)
    client.loop_start()
    client.publish(topic2, str(client._client_id.decode("utf-8"))+f" sent \"{ip_address}\"")
    client.loop_stop()
    
#fungsi callback    
def on_publish(client, userdata, result):
    print(str(datetime.datetime.now()) + f" pesan berhasil dipublish ")
    
def on_message(client, userdata, message):
    # ambil pesan yang diterima
    message_received = message.payload.decode("utf-8")

    # tambahkan pesan ke textbox log_text
    log_text.insert("end", message_received + "\n")

# fungsi callback untuk tombol "Refresh"
def refresh_log():
     # sambungkan ke broker MQTT
    connect_mqtt()
    
    # terdaftar untuk topik "coba/server"
    client.subscribe("coba/server")
    
    # terdaftar untuk fungsi on_publish()
    client.on_publish = on_publish
    
    # jalankan client MQTT
    client.loop_start()
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(str(datetime.datetime.now()), "Server berhasil terhubung ke MQTT Broker!1")
        else:
            print(client.connect(broker, port), "Server gagal terhubung, mengebalikan kode %d", rc)
            
    client.on_connect = on_connect
    client.connect(broker, port)

#inisiasi variable
broker = "test.mosquitto.org"
port = 1883
client = mqtt.Client("C1")
topic1 = "coba/server"
topic2 = "coba/user"

# membuat window utama
window = tk.Tk()
window.title("Aplikasi MQTT")
'''
# membuat label untuk menampilkan log aktivitas
log_label = tk.Label(master=window, text="Log Aktivitas:")
log_label.pack()

# membuat textbox untuk menampilkan log aktivitas
log_text = tk.Text(master=window)
log_text.pack()
client.on_message = on_message
client.subscribe(topic1)
'''
#membuat isi textbox yang menampilkan log aktivitas

# membuat label untuk input pesan
message_label = tk.Label(master=window, text="Pesan:")
message_label.pack()

# membuat textbox untuk input pesan
message_input = tk.Entry(master=window)
message_input.pack()

# membuat tombol "Kirim"
send_button = tk.Button(master=window, text="Send data", command=send_message)
send_button.pack()

# membuat tombol "kirim informasi address"
send_button2 = tk.Button(master = window, text="Send your information Address", command=send_message2)
send_button2.pack()

# membuat tombol "Refresh"
refresh_button = tk.Button(master=window, text="Refresh", command=refresh_log)
refresh_button.pack()

# menjalankan window utama
window.mainloop()
