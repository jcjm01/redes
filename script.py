def format_vcloud_number(number):
    """ Formatea el número de vCloud para asegurarse de que tenga el formato correcto (p.ej., '001', '065'). """
    return f"vCloud{int(number):03}"

# Datos simulados para los vClouds
dhci_data = {
    'vCloud001': {'Nombre': 'vCloud001', 'Vlan ID': '1101', 'Segmento': '10.100.1.0/28', 'Gateway': '10.100.1.1', 'Peer ID': 'vl1101','PSK':'vl1101p0cs'},
    'vCloud002': {'Nombre': 'vCloud002', 'Vlan ID': '1102', 'Segmento': '10.100.1.16/28', 'Gateway': '10.100.1.17', 'Peer ID': 'vl1102','PSK':'vl1102p0cs'},
    'vCloud003': {'Nombre': 'vCloud003', 'Vlan ID': '1103', 'Segmento': '10.100.1.32/28', 'Gateway': '10.100.1.33', 'Peer ID': 'vl1103','PSK':'vl1103p0cs'},
    'vCloud004': {'Nombre': 'vCloud004', 'Vlan ID': '1104', 'Segmento': '10.100.1.48/28', 'Gateway': '10.100.1.49', 'Peer ID': 'vl1104','PSK':'vl1104p0cs'},
    'vCloud005': {'Nombre': 'vCloud005', 'Vlan ID': '1105', 'Segmento': '10.100.1.64/28', 'Gateway': '10.100.1.65', 'Peer ID': 'vl1105','PSK':'vl1105p0cs'},
    'vCloud006': {'Nombre': 'vCloud006', 'Vlan ID': '1106', 'Segmento': '10.100.1.80/28', 'Gateway': '10.100.1.81', 'Peer ID': 'vl1106','PSK':'vl1106p0cs'},
    'vCloud007': {'Nombre': 'vCloud007', 'Vlan ID': '1107', 'Segmento': '10.100.1.96/28', 'Gateway': '10.100.1.97', 'Peer ID': 'vl1107','PSK':'vl1107vC1oud'},
    'vCloud008': {'Nombre': 'vCloud008', 'Vlan ID': '1108', 'Segmento': '10.100.1.112/28', 'Gateway': '10.100.1.113', 'Peer ID': 'vl1108','PSK':'vl1108vC1oud'},
    'vCloud009': {'Nombre': 'vCloud009', 'Vlan ID': '1109', 'Segmento': '10.100.1.128/28', 'Gateway': '10.100.1.129', 'Peer ID': 'vl1109','PSK':'vl1109vC1oud'},
    'vCloud010': {'Nombre': 'vCloud010', 'Vlan ID': '1110', 'Segmento': '10.100.1.144/28', 'Gateway': '10.100.1.145', 'Peer ID': 'vl1110','PSK':'vl1110vC1oud'},
    'vCloud011': {'Nombre': 'vCloud011', 'Vlan ID': '1111', 'Segmento': '10.100.1.160/28', 'Gateway': '10.100.1.161', 'Peer ID': 'vl1111','PSK':'vl1111vCloud'},
    'vCloud012': {'Nombre': 'vCloud012', 'Vlan ID': '1112', 'Segmento': '10.100.1.176/28', 'Gateway': '10.100.1.177', 'Peer ID': 'vl1112','PSK':'vl1112vCloud'},
    'vCloud013': {'Nombre': 'vCloud013', 'Vlan ID': '1113', 'Segmento': '10.100.1.192/28', 'Gateway': '10.100.1.193', 'Peer ID': 'vl1113','PSK':'vl1113vCloud'},
    'vCloud014': {'Nombre': 'vCloud014', 'Vlan ID': '1114', 'Segmento': '10.100.1.208/28', 'Gateway': '10.100.1.209', 'Peer ID': 'vl1114','PSK':'vl114vCloud'},
    'vCloud015': {'Nombre': 'vCloud015', 'Vlan ID': '1115', 'Segmento': '10.100.1.224/28', 'Gateway': '10.100.1.225', 'Peer ID': 'vl1115','PSK':'vl1115vCloud'},
    'vCloud016': {'Nombre': 'vCloud016', 'Vlan ID': '1116', 'Segmento': '10.100.1.240/28', 'Gateway': '10.100.1.241', 'Peer ID': 'vl1116','PSK':'vl1116vCloud'},
    'vCloud017': {'Nombre': 'vCloud017', 'Vlan ID': '1117', 'Segmento': '10.100.2.0/28', 'Gateway': '10.100.2.1', 'Peer ID': 'vl1117','PSK':'vl1117vC1oud'},
    'vCloud018': {'Nombre': 'vCloud018', 'Vlan ID': '1118', 'Segmento': '10.100.2.16/28', 'Gateway': '10.100.2.17', 'Peer ID': 'vl1118','PSK':'vl1118vC1oud'},
    'vCloud019': {'Nombre': 'vCloud019', 'Vlan ID': '1119', 'Segmento': '10.100.2.32/28', 'Gateway': '10.100.2.33', 'Peer ID': 'vl1119','PSK':'vl1119vC1oud'},
    'vCloud020': {'Nombre': 'vCloud020', 'Vlan ID': '1120', 'Segmento': '10.100.2.48/28', 'Gateway': '10.100.2.49', 'Peer ID': 'vl1120','PSK':'vl1120vC1oud'},
    'vCloud021': {'Nombre': 'vCloud021', 'Vlan ID': '1121', 'Segmento': '10.100.2.64/28', 'Gateway': '10.100.2.65', 'Peer ID': 'vl1121','PSK':'vl1121vCloud'},
    'vCloud022': {'Nombre': 'vCloud022', 'Vlan ID': '1122', 'Segmento': '10.100.2.80/28', 'Gateway': '10.100.2.81', 'Peer ID': 'vl1122','PSK':'vl1122vCloud'},
    'vCloud023': {'Nombre': 'vCloud023', 'Vlan ID': '1123', 'Segmento': '10.100.2.96/28', 'Gateway': '10.100.2.97', 'Peer ID': 'vl1123','PSK':'vl1123vCloud'},
    'vCloud024': {'Nombre': 'vCloud024', 'Vlan ID': '1124', 'Segmento': '10.100.2.112/28', 'Gateway': '10.100.2.113', 'Peer ID': 'vl1124','PSK':'vl1124vCloud'},
    'vCloud025': {'Nombre': 'vCloud025', 'Vlan ID': '1125', 'Segmento': '10.100.2.128/28', 'Gateway': '10.100.2.129', 'Peer ID': 'vl1125','PSK':'vl1125vCloud'},
    'vCloud026': {'Nombre': 'vCloud026', 'Vlan ID': '1126', 'Segmento': '10.100.2.144/28', 'Gateway': '10.100.2.145', 'Peer ID': 'vl1126','PSK':'vl1126vCloud'},
    'vCloud027': {'Nombre': 'vCloud027', 'Vlan ID': '1127', 'Segmento': '10.100.2.160/28', 'Gateway': '10.100.2.161', 'Peer ID': 'vl1127','PSK':'vl1127vC1oud'},
    'vCloud028': {'Nombre': 'vCloud028', 'Vlan ID': '1128', 'Segmento': '10.100.2.176/28', 'Gateway': '10.100.2.177', 'Peer ID': 'vl1128','PSK':'vl1128vC1oud'},
    'vCloud029': {'Nombre': 'vCloud029', 'Vlan ID': '1129', 'Segmento': '10.100.2.192/28', 'Gateway': '10.100.2.193', 'Peer ID': 'vl1129','PSK':'vl1129vC1oud'},
    'vCloud030': {'Nombre': 'vCloud030', 'Vlan ID': '1130', 'Segmento': '10.100.2.208/28', 'Gateway': '10.100.2.209', 'Peer ID': 'vl1130','PSK':'vl1130vC1oud'},
    'vCloud031': {'Nombre': 'vCloud031', 'Vlan ID': '1131', 'Segmento': '10.100.2.224/28', 'Gateway': '10.100.2.225', 'Peer ID': 'vl1131','PSK':'vl1131vCloud'},
    'vCloud032': {'Nombre': 'vCloud032', 'Vlan ID': '1132', 'Segmento': '10.100.2.240/28', 'Gateway': '10.100.2.241', 'Peer ID': 'vl1132','PSK':'vl1132vCloud'},
    'vCloud033': {'Nombre': 'vCloud033', 'Vlan ID': '1133', 'Segmento': '10.100.3.0/28', 'Gateway': '10.100.3.1', 'Peer ID': 'vl1133','PSK':'vl1133vCloud'},
    'vCloud034': {'Nombre': 'vCloud034', 'Vlan ID': '1134', 'Segmento': '10.100.3.16/28', 'Gateway': '10.100.3.17', 'Peer ID': 'vl1134','PSK':'vl1134vCloud'},
    'vCloud035': {'Nombre': 'vCloud035', 'Vlan ID': '1135', 'Segmento': '10.100.3.32/28', 'Gateway': '10.100.3.33', 'Peer ID': 'vl1135','PSK':'vl1135vCloud'},
    'vCloud036': {'Nombre': 'vCloud036', 'Vlan ID': '1136', 'Segmento': '10.100.3.48/28', 'Gateway': '10.100.3.49', 'Peer ID': 'vl1136','PSK':'vl1136vCloud'},
    'vCloud037': {'Nombre': 'vCloud037', 'Vlan ID': '1137', 'Segmento': '10.100.3.64/28', 'Gateway': '10.100.3.65', 'Peer ID': 'vl1137','PSK':'vl1137vCloud'},
    'vCloud038': {'Nombre': 'vCloud038', 'Vlan ID': '1138', 'Segmento': '10.100.3.80/28', 'Gateway': '10.100.3.81', 'Peer ID': 'vl1138','PSK':'T/0XbkQnVxfImUoGi#'},
    'vCloud039': {'Nombre': 'vCloud039', 'Vlan ID': '1139', 'Segmento': '10.100.3.96/28', 'Gateway': '10.100.3.97', 'Peer ID': 'vl1139','PSK':'vl1139vC11oud'},
    'vCloud040': {'Nombre': 'vCloud040', 'Vlan ID': '1140', 'Segmento': '10.100.3.112/28', 'Gateway': '10.100.3.113', 'Peer ID': 'vl1140','PSK':'vl1140vC1oud'},
    'vCloud041': {'Nombre': 'vCloud041', 'Vlan ID': '1141', 'Segmento': '10.100.3.128/28', 'Gateway': '10.100.3.129', 'Peer ID': 'vl1141','PSK':'vl1141vCloud'},
    'vCloud042': {'Nombre': 'vCloud042', 'Vlan ID': '1142', 'Segmento': '10.100.3.144/28', 'Gateway': '10.100.3.145', 'Peer ID': 'vl1142','PSK':'vl1142vC1oud'},
    'vCloud043': {'Nombre': 'vCloud043', 'Vlan ID': '1143', 'Segmento': '10.100.3.160/28', 'Gateway': '10.100.3.161', 'Peer ID': 'vl1143','PSK':'vl1143vC1oud'},
    'vCloud044': {'Nombre': 'vCloud044', 'Vlan ID': '1144', 'Segmento': '10.100.3.176/28', 'Gateway': '10.100.3.177', 'Peer ID': 'vl1144','PSK':'vl1144vC1oud'},
    'vCloud045': {'Nombre': 'vCloud045', 'Vlan ID': '1145', 'Segmento': '10.100.3.192/28', 'Gateway': '10.100.3.193', 'Peer ID': 'vl1145','PSK':'vl1145vC1oud'},
    'vCloud046': {'Nombre': 'vCloud046', 'Vlan ID': '1146', 'Segmento': '10.100.5.16/28', 'Gateway': '10.100.5.17', 'Peer ID': 'vl1146','PSK':'vl1146vC1oud'},
    'vCloud047': {'Nombre': 'vCloud047', 'Vlan ID': '1147', 'Segmento': '10.100.5.32/28', 'Gateway': '10.100.5.33', 'Peer ID': 'vl1147','PSK':'vl1147vC1oud'},
    'vCloud048': {'Nombre': 'vCloud048', 'Vlan ID': '1148', 'Segmento': '10.100.5.48/28', 'Gateway': '10.100.5.49', 'Peer ID': 'vl1148','PSK':'vl1148vC1oud'},
    'vCloud049': {'Nombre': 'vCloud049', 'Vlan ID': '1149', 'Segmento': '10.100.5.64/28', 'Gateway': '10.100.4.1', 'Peer ID': 'vl1149','PSK':'vl1149vC1oud'},
    'vCloud050': {'Nombre': 'vCloud050', 'Vlan ID': '1150', 'Segmento': '10.100.4.0/28', 'Gateway': '10.100.4.17', 'Peer ID': 'vl1150','PSK':'vl1150vC1oud'},
    'vCloud051': {'Nombre': 'vCloud051', 'Vlan ID': '1151', 'Segmento': '10.100.4.16/28', 'Gateway': '10.100.4.33', 'Peer ID': 'vl1151','PSK':'vl1151vC1oud'},
    'vCloud052': {'Nombre': 'vCloud052', 'Vlan ID': '1152', 'Segmento': '10.100.4.32/28', 'Gateway': '10.100.4.49', 'Peer ID': 'vl1152','PSK':'vl1152vC1oud'},
    'vCloud053': {'Nombre': 'vCloud053', 'Vlan ID': '1153', 'Segmento': '10.100.4.48/28', 'Gateway': '10.100.4.65', 'Peer ID': 'vl1153','PSK':'vl1153vC1oud'},
    'vCloud054': {'Nombre': 'vCloud054', 'Vlan ID': '1154', 'Segmento': '10.100.4.64/28', 'Gateway': '10.100.4.81', 'Peer ID': 'vl1154','PSK':'vl1154vC1oud'},
    'vCloud055': {'Nombre': 'vCloud055', 'Vlan ID': '1155', 'Segmento': '10.100.4.80/28', 'Gateway': '10.100.4.97', 'Peer ID': 'vl1155','PSK':'vl1155vC1oud'},
    'vCloud056': {'Nombre': 'vCloud056', 'Vlan ID': '1156', 'Segmento': '10.100.4.96/28', 'Gateway': '10.100.4.113', 'Peer ID': 'vl1156','PSK':'vl1156vC1oud'},
    'vCloud057': {'Nombre': 'vCloud057', 'Vlan ID': '1157', 'Segmento': '10.100.4.112/28', 'Gateway': '10.100.4.129', 'Peer ID': 'vl1157','PSK':'vl1157vC1oud'},
    'vCloud058': {'Nombre': 'vCloud058', 'Vlan ID': '1158', 'Segmento': '10.100.4.128/28', 'Gateway': '10.100.4.145', 'Peer ID': 'vl1158','PSK':'vl1158vC1oud'},
    'vCloud059': {'Nombre': 'vCloud059', 'Vlan ID': '1159', 'Segmento': '10.100.4.144/28', 'Gateway': '10.100.4.161', 'Peer ID': 'vl1159','PSK':'vl1159vC1oud'},
    'vCloud060': {'Nombre': 'vCloud060', 'Vlan ID': '1160', 'Segmento': '10.100.4.160/28', 'Gateway': '10.100.4.177', 'Peer ID': 'vl1160','PSK':'vl1160vC1oud'},
    'vCloud061': {'Nombre': 'vCloud061', 'Vlan ID': '1161', 'Segmento': '10.100.4.176/28', 'Gateway': '10.100.4.193', 'Peer ID': 'vl1161','PSK':'vl1161vC1oud'},
    'vCloud062': {'Nombre': 'vCloud062', 'Vlan ID': '1162', 'Segmento': '10.100.4.192/28', 'Gateway': '10.100.4.209', 'Peer ID': 'vl1162','PSK':'vl1162vC1oud'},
    'vCloud063': {'Nombre': 'vCloud063', 'Vlan ID': '1163', 'Segmento': '10.100.4.208/28', 'Gateway': '10.100.4.225', 'Peer ID': 'vl1163','PSK':'vl1163vC1oud'},
    'vCloud064': {'Nombre': 'vCloud064', 'Vlan ID': '1164', 'Segmento': '10.100.4.240/28', 'Gateway': '10.100.4.241', 'Peer ID': 'vl1164','PSK':'vl1164vC1oud'},
    'vCloud065': {'Nombre': 'vCloud065', 'Vlan ID': '1165', 'Segmento': '10.100.5.0/28', 'Gateway': '10.100.5.1', 'Peer ID': 'vl1165','PSK':'vl1165vC1oud'},
    
}

usuarios_data = {
    'vCloud001': {'Usuario': 'vCloud001', 'Contraseña': ')CZSPV_5#LqD', 'IP Default': '10.252.1.1-10.252.1.5'},
    'vCloud002': {'Usuario': 'vCloud002', 'Contraseña': '$VDS93+.q4k0', 'IP Default': '10.252.1.6-10.252.1.10'},
    'vCloud003': {'Usuario': 'vCloud003', 'Contraseña': 'Vz0+8s+i5LBn', 'IP Default': '10.252.1.11-10.252.1.15'},
    'vCloud004': {'Usuario': 'vCloud004', 'Contraseña': '_8vGcrM;LQNC', 'IP Default': '10.252.1.16-10.252.1.20'},
    'vCloud005': {'Usuario': 'vCloud005', 'Contraseña': "XK'vFC_eX)U!", 'IP Default': '10.252.1.21-10.252.1.25'},
    'vCloud006': {'Usuario': 'vCloud006', 'Contraseña': 'o~3&tm~8Dv3m', 'IP Default': '10.252.1.26-10.252.1.30'},
    'vCloud007': {'Usuario': 'vCloud007', 'Contraseña': '){8_R7ZGEOZ~', 'IP Default': '10.252.1.31-10.252.1.35'},
    'vCloud008': {'Usuario': 'vCloud008', 'Contraseña': 'wF$3fw7i5,K8', 'IP Default': '10.252.1.36-10.252.1.40'},
    'vCloud009': {'Usuario': 'vCloud009', 'Contraseña': 'WCDq$TQJ@W-g', 'IP Default': '10.252.1.41-10.252.1.45'},
    'vCloud010': {'Usuario': 'vCloud010', 'Contraseña': 'J3^La@6U]]E7', 'IP Default': '10.252.1.46-10.252.1.50'},
    'vCloud011': {'Usuario': 'vCloud011', 'Contraseña': 'xE$rg6gsb6qe', 'IP Default': '10.252.1.51-10.252.1.55'},
    'vCloud012': {'Usuario': 'vCloud012', 'Contraseña': 'I)p[aEp9pA-B', 'IP Default': '10.252.1.56-10.252.1.60'},
    'vCloud013': {'Usuario': 'vCloud013', 'Contraseña': 'gduo56x=RMnc', 'IP Default': '10.252.1.61-10.252.1.65'},
    'vCloud014': {'Usuario': 'vCloud014', 'Contraseña': 'LUqr~J-J^vN6', 'IP Default': '10.252.1.66-10.252.1.70'},
    'vCloud015': {'Usuario': 'vCloud015', 'Contraseña': '4j5NA[[YF#gQ', 'IP Default': '10.252.1.71-10.252.1.75'},
    'vCloud016': {'Usuario': 'vCloud016', 'Contraseña': 'ju}$XGUXd.Em', 'IP Default': '10.252.1.76-10.252.1.80'},
    'vCloud017': {'Usuario': 'vCloud017', 'Contraseña': '$Oi6qZ&BTZo$', 'IP Default': '10.252.1.81-10.252.1.85'},
    'vCloud018': {'Usuario': 'vCloud018', 'Contraseña': 'A1{[Dy-5fESA', 'IP Default': '10.252.1.86-10.252.1.90'},
    'vCloud019': {'Usuario': 'vCloud019', 'Contraseña': "e{%C$(heZ!'m", 'IP Default': '10.252.1.91-10.252.1.95'},
    'vCloud020': {'Usuario': 'vCloud020', 'Contraseña': 'MBjetYenH5^]', 'IP Default': '10.252.1.96-10.252.1.100'},
    'vCloud021': {'Usuario': 'vCloud021', 'Contraseña': 'TToh~_5JG^HW', 'IP Default': '10.252.1.101-10.252.1.105'},
    'vCloud022': {'Usuario': 'vCloud022', 'Contraseña': 'YK=znaLWMwS,', 'IP Default': '10.252.1.106-10.252.1.110'},
    'vCloud023': {'Usuario': 'vCloud023', 'Contraseña': 'w1dW$mJmUn.M', 'IP Default': '10.252.1.111-10.252.1.115'},
    'vCloud024': {'Usuario': 'vCloud024', 'Contraseña': '&9UU%OSVBezH', 'IP Default': '10.252.1.116-10.252.1.120'},
    'vCloud025': {'Usuario': 'vCloud025', 'Contraseña': "(i9unP-As2&p", 'IP Default': '10.252.1.121-10.252.1.125'},
    'vCloud026': {'Usuario': 'vCloud026', 'Contraseña': '&Nrm0&Z=)TY9', 'IP Default': '10.252.1.126-10.252.1.130'},
    'vCloud027': {'Usuario': 'vCloud027', 'Contraseña': ']&%pe1,mN87q', 'IP Default': '10.252.1.131-10.252.1.135'},
    'vCloud028': {'Usuario': 'vCloud028', 'Contraseña': 'yqC)2E1ePHWw', 'IP Default': '10.252.1.136-10.252.1.140'},
    'vCloud029': {'Usuario': 'vCloud029', 'Contraseña': "P5=v#QnR!e%X", 'IP Default': '10.252.1.141-10.252.1.145'},
    'vCloud030': {'Usuario': 'vCloud030', 'Contraseña': '$kiA]_YXDV9X', 'IP Default': '10.252.1.146-10.252.1.150'},
    'vCloud031': {'Usuario': 'vCloud031', 'Contraseña': '{GpEsv)fGUHK', 'IP Default': '10.252.1.151-10.252.1.155'},
    'vCloud032': {'Usuario': 'vCloud032', 'Contraseña': 'CXaYFH8]gpuM', 'IP Default': '10.252.1.156-10.252.1.160'},
    'vCloud033': {'Usuario': 'vCloud033', 'Contraseña': "w%E;2znro3K'", 'IP Default': '10.252.1.161-10.252.1.165'},
    'vCloud034': {'Usuario': 'vCloud034', 'Contraseña': 'MJ[K]ySNQ;(I', 'IP Default': '10.252.1.166-10.252.1.170'},
    'vCloud035': {'Usuario': 'vCloud035', 'Contraseña': "HT}]s+$o%'n)", 'IP Default': '10.252.1.171-10.252.1.175'},
    'vCloud036': {'Usuario': 'vCloud036', 'Contraseña': 'XCXHu_X%z-pY', 'IP Default': '10.252.1.176-10.252.1.180'},
    'vCloud037': {'Usuario': 'vCloud037', 'Contraseña': 'O$+Vb#WUh!d=', 'IP Default': '10.252.1.181-10.252.1.185'},
    'vCloud038': {'Usuario': 'vCloud038', 'Contraseña': 'T/0XbkQnVxfImUoGi#', 'IP Default': '10.252.1.186-10.252.1.190'},
    'vCloud039': {'Usuario': 'vCloud039', 'Contraseña': '&F~Q,P_O8yvs', 'IP Default': '10.252.1.191-10.252.1.195'},
    'vCloud040': {'Usuario': 'vCloud040', 'Contraseña': 'FETF(XU]oNjS', 'IP Default': '10.252.1.196-10.252.1.200'},
    'vCloud041': {'Usuario': 'vCloud041', 'Contraseña': "3]Pp,,A'+ply", 'IP Default': '10.252.1.201-10.252.1.205'},
    'vCloud042': {'Usuario': 'vCloud042', 'Contraseña': 'cabL7uRKzl9M', 'IP Default': '10.252.1.206-10.252.1.210'},
    'vCloud043': {'Usuario': 'vCloud043', 'Contraseña': 'D9%6HT(y{MvV', 'IP Default': '10.252.1.211-10.252.1.215'},
    'vCloud044': {'Usuario': 'vCloud044', 'Contraseña': '~4-g%-h-u8h8', 'IP Default': '10.252.1.216-10.252.1.220'},
    'vCloud045': {'Usuario': 'vCloud045', 'Contraseña': "wgO@D+!}x'cd", 'IP Default': '10.252.1.221-10.252.1.225'},
    'vCloud046': {'Usuario': 'vCloud046', 'Contraseña': 'Ib[2)rY40t_6', 'IP Default': '10.252.1.226-10.252.1.230'},
    'vCloud047': {'Usuario': 'vCloud047', 'Contraseña': 'iP7.B9f/uFSt', 'IP Default': '10.252.1.231-10.252.1.235'},
    'vCloud048': {'Usuario': 'vCloud048', 'Contraseña': 'fqi)Fu_hhX@2', 'IP Default': '10.252.1.236-10.252.1.240'},
    'vCloud049': {'Usuario': 'vCloud049', 'Contraseña': '%Qk,I0,T5E,W', 'IP Default': '10.252.1.241-10.252.1.245'},
    'vCloud050': {'Usuario': 'vCloud050', 'Contraseña': '0d44jFhpX&Ma', 'IP Default': '10.252.1.246-10.252.1.250'},
    'vCloud051': {'Usuario': 'vCloud051', 'Contraseña': '2B3jF8Ww#rd4', 'IP Default': '10.252.1.251-10.252.1.255'},
    'vCloud052': {'Usuario': 'vCloud052', 'Contraseña': 'nsYV&{d~_=04', 'IP Default': '10.252.2.1-10.252.2.5'},
    'vCloud053': {'Usuario': 'vCloud053', 'Contraseña': ']Ms9F~}yK3lo', 'IP Default': '10.252.2.6-10.252.2.10'},
    'vCloud054': {'Usuario': 'vCloud054', 'Contraseña': 'Iyu]lVS0c[yH', 'IP Default': '10.252.2.11-10.252.2.15'},
    'vCloud055': {'Usuario': 'vCloud055', 'Contraseña': "xb&Ghq7&xN}y", 'IP Default': '10.252.2.16-10.252.2.20'},
    'vCloud056': {'Usuario': 'vCloud056', 'Contraseña': 't(@,FQTR(ZNM', 'IP Default': '10.252.2.21-10.252.2.25'},
    'vCloud057': {'Usuario': 'vCloud057', 'Contraseña': '}BEVe$(iPo!9', 'IP Default': '10.252.2.26-10.252.2.30'},
    'vCloud058': {'Usuario': 'vCloud058', 'Contraseña': 'R($vTKOWRZfI', 'IP Default': '10.252.2.31-10.252.2.35'},
    'vCloud059': {'Usuario': 'vCloud059', 'Contraseña': 'cIrzNvUFW_$o', 'IP Default': '10.252.2.36-10.252.2.40'},
    'vCloud060': {'Usuario': 'vCloud060', 'Contraseña': 'iI3qav{.O=q}', 'IP Default': '10.252.2.41-10.252.2.45'},
    'vCloud061': {'Usuario': 'vCloud061', 'Contraseña': '6Ktnr.s=#.Yj', 'IP Default': '10.252.2.46-10.252.2.50'},
    'vCloud062': {'Usuario': 'vCloud062', 'Contraseña': '4O=ZebIs_Cmq', 'IP Default': '10.252.2.51-10.252.2.55'},
    'vCloud063': {'Usuario': 'vCloud063', 'Contraseña': "0&CW&L'+61Q'", 'IP Default': '10.252.2.56-10.252.2.60'},
    'vCloud064': {'Usuario': 'vCloud064', 'Contraseña': '3f,f-e^ostB;', 'IP Default': '10.252.2.61-10.252.2.65'},
    'vCloud065': {'Usuario': 'vCloud065', 'Contraseña': "HWVj]uDdJppW", 'IP Default': '10.252.2.66-10.252.2.70'},
}

def generar_script_configuracion(vcloud_number):
    vcloud_name = format_vcloud_number(vcloud_number)
    dhci_info = dhci_data.get(vcloud_name, {})
    usuario_info = usuarios_data.get(vcloud_name, {})

    if dhci_info and usuario_info:
        ip_default_start, ip_default_end = usuario_info['IP Default'].split('-')
        
        script = f"""
config system interface
    edit "{vcloud_name}"
        set vdom "root"
        set ip {dhci_info['Gateway']} 255.255.255.240
        set allowaccess ping
        set interface "Abiquo"
        set vlanid {dhci_info['Vlan ID']}
    next
end

config user local
    edit "{vcloud_name}"
    set type password
    set auth-concurrent-override enable
    set auth-concurrent-value 5
    set passwd {usuario_info['Contraseña']}
    next
end

config user group
    edit "{vcloud_name}"
    set member "{vcloud_name}"
    next
end

config firewall address
    edit "{vcloud_name}"
    set subnet {dhci_info['Segmento']} 255.255.255.240
    next
end

config firewall addrgrp
    edit "{vcloud_name}vpn_split"
    set member "{vcloud_name}"
    next
end

config firewall address
    edit "{vcloud_name}vpn_range"
    set type iprange
    set start-ip {ip_default_start}
    set end-ip {ip_default_end}
    next
end

config vpn ipsec phase1-interface
    edit "{vcloud_name}vpn"
    set type dynamic
    set interface "WAN"
    set mode aggressive
    set peertype one
    set net-device disable
    set mode-cfg enable
    set proposal aes128-sha1 aes256-sha256
    set dpd on-idle
    set dhgrp 5
    set xauthtype auto
    set authusrgrp "{vcloud_name}"
    set peerid "{dhci_info['Peer ID']}"
    set ipv4-start-ip {ip_default_start}
    set ipv4-end-ip {ip_default_end}
    set dns-mode auto
    set ipv4-split-include "{vcloud_name}vpn_split"
    set save-password enable
    set psksecret "{dhci_info['PSK']}"
    set dpd-retryinterval 60
    next
end

config vpn ipsec phase2-interface
    edit "{vcloud_name}vpn"
    set phase1name "{vcloud_name}vpn"
    set proposal aes128-sha1 aes256-sha1
    set dhgrp 5
    next
end

config firewall policy
    edit 0
    set name "{vcloud_name}vpn"
    set srcintf "{vcloud_name}vpn"
    set dstintf "{vcloud_name}"
    set action accept
    set srcaddr "{vcloud_name}vpn_range"
    set dstaddr "{vcloud_name}"
    set schedule "always"
    set service "ALL"
    set nat enable
    next
end

config firewall policy
    edit 0
    set name "Internet {vcloud_name}"
    set srcintf "{vcloud_name}"
    set dstintf "WAN"
    set action accept
    set srcaddr "{vcloud_name}"
    set dstaddr "all"
    set schedule "always"
    set service "ALL"
    set utm-status enable
    set ssl-ssh-profile "certificate-inspection"
    set av-profile "default"
    set dnsfilter-profile "default"
    set logtraffic all
    set nat enable
    next
end
"""
        print(script)
    else:
        print(f"No se encontró información completa para {vcloud_name}.")

# Solicitar al usuario el número de vCloud
vcloud_number = input("Introduce el número de vCloud (1-65): ")
generar_script_configuracion(vcloud_number)
