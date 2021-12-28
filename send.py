# prueba aja
import pywhatkit as kit

names =["estimado emprendedor","estimado emprendedor","estimado emprendedor", "estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor","estimado emprendedor"]
phones = ["+50497267596","+50494749475","+50496364978","+50499757293","+5049972-9241"]


texts = []
for name in names:
    texts.append("Hola {fname}!  Le saluda Gabriela N. de Impact Hub Tegucigalpa.\n  Es de nuestro agrado poder compartir contigo el programa Propulsión de Impacto. \n El programa está compuesto por cinco componentes: desarrollo de capacidades, acompañamiento, acceso a recursos, conexiones y visibilización con el objetivo de potenciar el crecimiento y ampliar las oportunidades de negocios de 100 MiPymes en Honduras. \n Por lo cual nos gustaría saber ¿Cuantas son sus ventas ANUALES para los siguientes años?\n \n  Total ventas anuales 2019:\n Total ventas anuales 2020:\n Total ventas anuales 2021:".format(fname=name))

hour = 9
minute = 50
for i, phone in enumerate(phones):
    kit.sendwhatmsg(phone, texts[i], hour, minute)
    minute = minute + 2

