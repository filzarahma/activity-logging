#import tkinter for ui
import tkinter as tk

# import paho
import paho.mqtt.client as mqtt

# import time
import time

#import datetime
import datetime

# fungsi callback
def on_message(client, userdata, message):
 print(str(datetime.datetime.now()),
 str(message.payload.decode("utf-8")), "in topic", str(message.topic))

# buat koneksi ke broker
def connect_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(str(datetime.datetime.now()), "Server berhasil terhubung ke MQTT Broker!1")
            
        else:
            print(client.connect(broker, port), "Server gagal terhubung, mengebalikan kode %d", rc)

    client.on_connect = on_connect
    client.connect(broker, port)
    return client
def show_log():
    connect_mqtt()
    # jalankan loop client
    client.loop_start()
    topic1 = "coba/server"
    topic2 = "coba/user"
    # loop forever
    while True:
        #client.subscribe(topic1)
        client.subscribe(topic2)
        time.sleep(1)
                
        client.on_message = on_message

    #stop loop
    client.loop_stop()
    
def exit_app():
    # stop loop client
    client.loop_stop()
    # close the window
    app.destroy()
# membuat window aplikasi
app = tk.Tk()
app.title("MQTT Server")

# inisiasi broker
broker = "test.mosquitto.org"
port = 1883

# buat client S sebagai server
client=mqtt.Client("S")

# membuat frame untuk layout UI
frame = tk.Frame(app)
frame.pack()

# membuat label untuk menampilkan topik yang tersedia
topics_label = tk.Label(frame, text="Topik yang tersedia:")
topics_label.pack()

# membuat listbox untuk menampilkan topik yang tersedia
topics_listbox = tk.Listbox(frame, width=30)
topics_listbox.pack()
topics_listbox.insert(1, "coba/server")
topics_listbox.insert(2, "coba/user")

# membuat button untuk menampilkan log aktivitas
log_button = tk.Button(frame, text="Tampilkan Log Aktivitas", command=show_log)
log_button.pack()

# membuat label untuk menampilkan log aktivitas
log_label = tk.Label(frame, text="")
log_label.pack()

# membuat button keluar
exit_button = tk.Button(frame, text="Keluar", command=exit_app)
exit_button.pack()

# menjalankan aplikasi
app.mainloop()
