import textfsm
from netmiko import ConnectHandler
from credenciales import usuario_olt, password_olt

def information_board(olt_connection):
    display_board_0 = olt_connection.send_command(f'display board 0')
    template_display_board_0 = open('templates\huawei_olt_display_board_0.textfsm')
    display_board_0_table = textfsm.TextFSM(template_display_board_0)
    fsm_result_display_board_0 = display_board_0_table.ParseText(display_board_0)
    return fsm_result_display_board_0

def ont_info_summary(olt_connection):
        display_ont_info = olt_connection.send_command('display ont info summary 0 | include "the total"',read_timeout=90)
        return display_ont_info

with open('test_olt.txt', 'r') as equipos:
#with open('Lista_OLTs.txt', 'r') as equipos:
    device_list = equipos.read().splitlines()

for device in device_list:
    device_config = {
        "device_type": "huawei_olt",
        "ip":device,
        "username":usuario_olt, 
        "password":password_olt,
        "global_delay_factor": 10,
    }
    Connection_OLT = ConnectHandler(**device_config)
    Connection_OLT.enable()
    info_board = information_board(Connection_OLT)
    info_ont = ont_info_summary(Connection_OLT)

    with open('list_ont_info.txt', 'w') as grabar:
        grabar1 = grabar.write(info_ont)

    lines = []
    archivo = 'list_ont_info.txt'
    with open(archivo, 'r') as fp:
        lines = fp.readlines()

    with open(archivo, 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [0, 1]:
                fp.write(line)

    with open(archivo, 'r') as w:
        lineas = w.readlines()

    lista_final = []
    tarjeta_olt = []
    tarjeta_instalada = []
    temp_tarjetas = []
    for i in lineas:
        as_list = i.split(" ")
        interfaz = as_list[4]
        total_usuario = as_list[10]
        online_usuario = as_list[12]
        #lista_final = interfaz + total_usuario + online_usuario
        filtro =interfaz.split("/")
        tarjeta_olt.append(filtro[1])
        #print(f'{device}","{interfaz}{total_usuario}{online_usuario}')
        #temp_tarjetas = {device}+{interfaz}+{total_usuario}+{online_usuario}
        #temp_tarjetas.extend([{device},{interfaz},{total_usuario},{online_usuario},"\n"])
        temp_tarjetas = [str(device),interfaz+total_usuario+online_usuario]
        #print(temp_tarjetas)

    tarjeta_olt = list(dict.fromkeys(tarjeta_olt))
    tarjeta_olt = [int(x) for x in tarjeta_olt]
    tarjeta_olt.sort()
    slot_free = []
    for elements in info_board:
        if elements[2] == 'Normal' and 'HF' in elements[1]:
            tarjeta_instalada.append(elements[0])
   
    for items in info_board:
        if len(items[1]) == 0:
            slot_free.append(items[0])

    #  slot_free.remove('0')
    for ii in slot_free:
        print(f'{device},0/{ii.split("/")}/#')

    tarjeta_instalada = [int(x) for  x in tarjeta_instalada]
    tarjeta_instalada.sort()
    # print(tarjeta_instalada)
    # print(tarjeta_olt)
    elemento_no_comun = set(tarjeta_instalada).difference(tarjeta_olt)
    #print(f'Para la OLT {device} la tarjeta sin usuarios es :{elemento_no_comun}')
