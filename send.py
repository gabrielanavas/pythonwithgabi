# prueba aja
import pywhatkit as kit

names =["estimado emprendedor","estimado emprendedor","estimado emprendedor", "estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor"]
phones = ["+50487999925",
"+50497672273",
"+50495010001",
"+50432443451"]


texts = []
for name in names:
    texts.append("Hola {fname}!  Le saluda Gabriela N. de Impact Hub Tegucigalpa.\n Recordarle que está pendiente la agenda de la reunión del Programa \n Favor si puede agendarla el día de hoy a través de este link: https://calendly.com/innovaccion/levantamiento-de-linea-base".format(fname=name))


hour = 15
minute = 33
for i, phone in enumerate(phones):
    kit.sendwhatmsg(phone, texts[i], hour, minute)
    minute = minute + 2

