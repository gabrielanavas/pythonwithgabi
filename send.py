# prueba aja
import pywhatkit as kit

names ="estimado emprendedor"
numbers= ["96738587"]


texts = []
for name in names:
    texts.append('''Hola {fname}!  Le saluda Gabriela N. de Impact Hub Tegucigalpa.\n Es de nuestro agrado poder compartir contigo el programa Propulsión de Impacto. 
\nPropulsión de Impacto  es un programa de incubación de 10 semanas y 12 meses de acompañamiento facilitado por  Impact Hub Tegucigalpa, con el apoyo del Proyecto Transformando Sistemas de Mercado (TMS) de USAID, y aliados 
\nEl programa está compuesto por cinco componentes: desarrollo de capacidades, acompañamiento, acceso a recursos, conexiones y visibilización con el objetivo de potenciar el crecimiento y ampliar las oportunidades de negocios de 100 MiPymes en Honduras. 
\nEl siguiente paso en el proceso es la firma de un acuerdo de compromiso, que podrás descargar adjunto a el correo electronico o me lo puedes solicitar y deberás enviarnos firmado a más tardar el día 4 de  Enero del 2022. Tenga en cuenta que el comienzo del programa sera en Enero.'''.format(fname=name))

hour = 4
minute = 37
for i, number in enumerate(corrected):
    kit.sendwhatmsg(corrected, texts[i], hour, minute)
    minute = minute + 2

