# Description
A functional API that uses regular expressions to parse replay (.roa) files from Rivals of Aether.

# Explanations

## Replay data

A string buffer containing the entire contents of a replay (.roa) file.

```
001030521211831072018SAMPLE REPLAY                   This is a replay I recorded to use as a sample in my replay parser.                                                                         0000022740
11501082000000000
HPlayer 1                              10000010004F2EAFCFCEDFC45FF405CCBF0FFC72038                  
1Z101zy327R102y333103y338I104y341I105y344106y345108y346109y349110y354111y358112y359115y  0119y  6120Zy 90r121y  0128zRI129I130y360I131y354I132y346133y344142y345143y346148C150y345151y344152y350153y  2154Zy  0rc181y180182y166183zy162L184y160186y156187y153U188y155189y156u190y157191y159C192y163193y176194y182195Zy192l196y  0c213A221a242y 78243y 75244zy 83UM245PM246y 79PM247y 78M248y 77249y 76251A257a281y 69282Zy 73u283y  0298y237299y252300zy258DO301O302y252LO303y250A310y252311y253a312y255l313y256317y257318y258319y259321y260323y261324y263325y264326y266327y267328y269329y270331y267332Zy201d333y180334y  0352zR353y346I354y345I355y344I356y342357y339359C360y341361y342362y343363y344364c365y345366y347367y358368Zy 28r369y 90370y  0412y 57413zy 69RUPM414y 67PM415y 65PM416PAM426y 63427y 59428y 54429y 46430y 37431y 23u432y  8433y360434y350435y344436y340437y339444y343445y351446y  0a447y 17448y 68rU449y 90450Zu451y  0479zy341R480y334DI481y340dI482y343I483y344484B490b492y342493y354494Zy  0r525y 69526zy 66U527y 69RPBM528y 66PM529y 64PM530M533b538y 65539y 68542y 69550y 70B551y 71553y 72555y 74r556y 87b557y 91558y107L559y121560y129561y135E562y140563y144564y145565y147567y148568y149569y151570y156u571y161572y170573y180574Zl575y  0604y219605y247606zy261DO607y262O608y259OB609y258O614y260615y263b616y264620B626b633B635y266637y267b643y268644y269649y270655C663c670C677c692C699c709C711y273712y275713Zy285d714y 76c715zy 73UM716y 76PM717y 69RPM718y 68PM723C730y 63c731y 59732y 54733y 52734y 49735y 48740y 49741y 50742y 52743y 53748C755c760y 52765y 38766y 10u767y353768Zy  0r780y270781zD782O783O784y263O785y258786y256788y255791y257792y260793y263796y262802y261813y262814y263815y262816Zy224d817zy180L818Zl819y  0826zy 67U827y 71RPCM828y 69PM829PM830M833y 63834y 32u835y  2c836Zy360r837y  0886y265887zy267DO888O889y263O916y265917y268918y270921y266922Zy247d923y192924y  0929zy 82U930y 79PM931y 73PCM932y 74PM933y 73M935y 74936y 73938y 72Rc940Zy  0ru1018y2701019zy278D1020y285O1021y284O1022y276O1023y2721024y2711026y2731027y2801028y289R1029y2971030y3071031y317I1032y3251033y3341034y340d1035y3421038y3431067y3421068y3391069y336D1070y3331071y3321075y3331076y3341077y337d1078y3411079y3461080y3511081y  01082y 101083y 26U1084y 39M1085y 45PM1086y 49PM1087y 50M1088y 531089y 541090y 571091y 631092y 711093y 721094y 701095y 63J1103y 60j1104y 551105y 531106y 491107y 431108y 391109y 381112y 391114y 401118y 381119y 311120y 22u1121y 111122y  31123y  01124y3571125y3541126y3511127y3501129y3491132y  01133y159Lr1134y156E1135y162E1136E1138C1142y1611143y1581144y1571145y155Uc1146y1521147y1481148y1441149y1411150y1401151y1451152y1491153y156u1154y1621155y174C1156Zy180l1158y  01161c1172C1175c1192y3601193zy340R1194y335DI1195y342dI1196y346I1199A1203a1205y3451206y3431207y3441208y  01209Zy 81r1210y  01234zy180L1235y162E1236y159E1237E1243y1601244y162C1245y1651246y1661247Zy  0l1251c1262C1266zy150L1267y1521268y1511269c1270y1501271y1511273y1551274y1601275Zy  0l1292y1491293zy143LU1294y146EM1295y151E1296y154E1297y156u1298y1571299y1601300y1631301y1661302y1711303y1801305y1791306y1681307y1621315y1691316Zy180l1317y  01319zy359R1320y342I1321y344I1322y341I1323y3361324y334D1325y333C1328y3341329y3351331y3361333d1335y353c1336Zy  0r1350C1354c1381y1751382zy156L1383y151UE1384y152E1385E1386y1541388y1561389y157uB1392y158A1393y1641394y1691395y1731396y180a1397Zlb1398y  01421zy351R1422y344I1423y342I1424y344I1428y3431430y3421440y3411442y3401443y3391444y3381446y3371450y3361452D1453y3341454y3321455y3341456Zy353rd1457zy158L1458y153UE1459y154E1460y153E1461y147M1462y1411463y129BM1464y115M1465y 98lM1466y 901467y 881468y 871475b1482y 881483y 901485Zu1486y  01495y2701496zD1497y284O1498O1499y279O1500y2761501A1503y2751504y2731505y2721509a1511y2731512y2751513y2781514y2831515y2851516y290R1517y2961518y2991519y3061520y3131521y3211522y3251523y3271525y3291526y343d1527y 221528Zy 59r1529y 521530zy 35R1531y 211532I1533y 221534y 26U1535y 36M1536y 39M1537y 40M1538y 41M1539y 441540y 48A1541y 531542y 571543y 611544y 631548a1562y 651563y 731564y 90r1565y114L1566y135E1567y146E1568y150E1569y1541570y157u1571y1591572y1601574y1611575y1601576y1611577y1621578y1631587C1592y1681593y1801594Zy  0lc1624zy179L1625y159E1626y160E1627y161E1645y1681646y1761647Zy  0l1651zy169L1652y154UE1653y161uE1654y162E1659y1601660y1591663y1621664y1631665Zy180l1666y  01669zy360R1670y345I1671y350I1672y349I1674y3481677y3491678JC1679y3471680y  01681Zrj1685c1701y1801702zy158L1703y153UE1704y154E1705y156E1706y157u1727y1561730U1731y1551733y1541734y1521735y1501736y148u1737Zy125l1738y  01739y 291740zy 11R1741y  51742y  01743y3541744y3421745y3311746Zy  0r1754zy162L1755y1591756y156E1757y157E1758y1581768y1571769y1561771Zy  0l1773zy  2R1774y360I1775y353I1776I1777y3511778y3491780y3591781Zy  0r1790C1848y1801849zL1850y1751853y174c1854y1781855Zy180l1856y  01880y1801881zy170L1882y1691884y1701885y1691915y1681916y1651917y1631918y1621924y1661927y1651928y1631938y1661939y1671943y1661949y1651950Zy170l1951y  01953y  61954C1955y  01962c1998y1801999zy165L2000y162E2001EC2002E2003y1652004y1752005Zy  0l2008c2041zR2042y357I2043y354I2044I2046y3512049Zy  0rC2056c2071zR2072y349I2073y342I2074I2075y3412076y3422077y351C2078Zy  0r2085c2129y1802130zy205L2131y237D2132y255lO2133y257O2134O2143C2146y259Ac2147y2632148y2652149y2662150y2672154a2158y2662243y2652244y2642249y2632250y2622251y2572252y2442253y227Ld2254Zy195l2255y  02258y 902262y 852263zU2264y 86M2265y 87PM2266y 86PM2267y 84M2268y 832272y 88C2273y 902274y1012275y1052276y1062279y107L2280y1122281y1162282y1172287y1182288y1222289y1252290y1302291y1342292y1362293y1382295y1392297c2299y1442300Zy  0lu2363y2702366zD2384Zy180d2385y  0
5Player 2                              060101100043170907F5F1BA9FFDA3FB1EA002F770E3043FFFFE456      

5Player 3                              02020220004CE2F2FFCF623FFB986FF5E5EA0012979                  

0
```
## Player data

A string buffer extracted from replay data, consisting of a singular player's information.

```
HPlayer 1                              10000010004F2EAFCFCEDFC45FF405CCBF0FFC72038                  
1Z101zy327R102y333103y338I104y341I105y344106y345108y346109y349110y354111y358112y359115y  0119y  6120Zy 90r121y  0128zRI129I130y360I131y354I132y346133y344142y345143y346148C150y345151y344152y350153y  2154Zy  0rc181y180182y166183zy162L184y160186y156187y153U188y155189y156u190y157191y159C192y163193y176194y182195Zy192l196y  0c213A221a242y 78243y 75244zy 83UM245PM246y 79PM247y 78M248y 77249y 76251A257a281y 69282Zy 73u283y  0298y237299y252300zy258DO301O302y252LO303y250A310y252311y253a312y255l313y256317y257318y258319y259321y260323y261324y263325y264326y266327y267328y269329y270331y267332Zy201d333y180334y  0352zR353y346I354y345I355y344I356y342357y339359C360y341361y342362y343363y344364c365y345366y347367y358368Zy 28r369y 90370y  0412y 57413zy 69RUPM414y 67PM415y 65PM416PAM426y 63427y 59428y 54429y 46430y 37431y 23u432y  8433y360434y350435y344436y340437y339444y343445y351446y  0a447y 17448y 68rU449y 90450Zu451y  0479zy341R480y334DI481y340dI482y343I483y344484B490b492y342493y354494Zy  0r525y 69526zy 66U527y 69RPBM528y 66PM529y 64PM530M533b538y 65539y 68542y 69550y 70B551y 71553y 72555y 74r556y 87b557y 91558y107L559y121560y129561y135E562y140563y144564y145565y147567y148568y149569y151570y156u571y161572y170573y180574Zl575y  0604y219605y247606zy261DO607y262O608y259OB609y258O614y260615y263b616y264620B626b633B635y266637y267b643y268644y269649y270655C663c670C677c692C699c709C711y273712y275713Zy285d714y 76c715zy 73UM716y 76PM717y 69RPM718y 68PM723C730y 63c731y 59732y 54733y 52734y 49735y 48740y 49741y 50742y 52743y 53748C755c760y 52765y 38766y 10u767y353768Zy  0r780y270781zD782O783O784y263O785y258786y256788y255791y257792y260793y263796y262802y261813y262814y263815y262816Zy224d817zy180L818Zl819y  0826zy 67U827y 71RPCM828y 69PM829PM830M833y 63834y 32u835y  2c836Zy360r837y  0886y265887zy267DO888O889y263O916y265917y268918y270921y266922Zy247d923y192924y  0929zy 82U930y 79PM931y 73PCM932y 74PM933y 73M935y 74936y 73938y 72Rc940Zy  0ru1018y2701019zy278D1020y285O1021y284O1022y276O1023y2721024y2711026y2731027y2801028y289R1029y2971030y3071031y317I1032y3251033y3341034y340d1035y3421038y3431067y3421068y3391069y336D1070y3331071y3321075y3331076y3341077y337d1078y3411079y3461080y3511081y  01082y 101083y 26U1084y 39M1085y 45PM1086y 49PM1087y 50M1088y 531089y 541090y 571091y 631092y 711093y 721094y 701095y 63J1103y 60j1104y 551105y 531106y 491107y 431108y 391109y 381112y 391114y 401118y 381119y 311120y 22u1121y 111122y  31123y  01124y3571125y3541126y3511127y3501129y3491132y  01133y159Lr1134y156E1135y162E1136E1138C1142y1611143y1581144y1571145y155Uc1146y1521147y1481148y1441149y1411150y1401151y1451152y1491153y156u1154y1621155y174C1156Zy180l1158y  01161c1172C1175c1192y3601193zy340R1194y335DI1195y342dI1196y346I1199A1203a1205y3451206y3431207y3441208y  01209Zy 81r1210y  01234zy180L1235y162E1236y159E1237E1243y1601244y162C1245y1651246y1661247Zy  0l1251c1262C1266zy150L1267y1521268y1511269c1270y1501271y1511273y1551274y1601275Zy  0l1292y1491293zy143LU1294y146EM1295y151E1296y154E1297y156u1298y1571299y1601300y1631301y1661302y1711303y1801305y1791306y1681307y1621315y1691316Zy180l1317y  01319zy359R1320y342I1321y344I1322y341I1323y3361324y334D1325y333C1328y3341329y3351331y3361333d1335y353c1336Zy  0r1350C1354c1381y1751382zy156L1383y151UE1384y152E1385E1386y1541388y1561389y157uB1392y158A1393y1641394y1691395y1731396y180a1397Zlb1398y  01421zy351R1422y344I1423y342I1424y344I1428y3431430y3421440y3411442y3401443y3391444y3381446y3371450y3361452D1453y3341454y3321455y3341456Zy353rd1457zy158L1458y153UE1459y154E1460y153E1461y147M1462y1411463y129BM1464y115M1465y 98lM1466y 901467y 881468y 871475b1482y 881483y 901485Zu1486y  01495y2701496zD1497y284O1498O1499y279O1500y2761501A1503y2751504y2731505y2721509a1511y2731512y2751513y2781514y2831515y2851516y290R1517y2961518y2991519y3061520y3131521y3211522y3251523y3271525y3291526y343d1527y 221528Zy 59r1529y 521530zy 35R1531y 211532I1533y 221534y 26U1535y 36M1536y 39M1537y 40M1538y 41M1539y 441540y 48A1541y 531542y 571543y 611544y 631548a1562y 651563y 731564y 90r1565y114L1566y135E1567y146E1568y150E1569y1541570y157u1571y1591572y1601574y1611575y1601576y1611577y1621578y1631587C1592y1681593y1801594Zy  0lc1624zy179L1625y159E1626y160E1627y161E1645y1681646y1761647Zy  0l1651zy169L1652y154UE1653y161uE1654y162E1659y1601660y1591663y1621664y1631665Zy180l1666y  01669zy360R1670y345I1671y350I1672y349I1674y3481677y3491678JC1679y3471680y  01681Zrj1685c1701y1801702zy158L1703y153UE1704y154E1705y156E1706y157u1727y1561730U1731y1551733y1541734y1521735y1501736y148u1737Zy125l1738y  01739y 291740zy 11R1741y  51742y  01743y3541744y3421745y3311746Zy  0r1754zy162L1755y1591756y156E1757y157E1758y1581768y1571769y1561771Zy  0l1773zy  2R1774y360I1775y353I1776I1777y3511778y3491780y3591781Zy  0r1790C1848y1801849zL1850y1751853y174c1854y1781855Zy180l1856y  01880y1801881zy170L1882y1691884y1701885y1691915y1681916y1651917y1631918y1621924y1661927y1651928y1631938y1661939y1671943y1661949y1651950Zy170l1951y  01953y  61954C1955y  01962c1998y1801999zy165L2000y162E2001EC2002E2003y1652004y1752005Zy  0l2008c2041zR2042y357I2043y354I2044I2046y3512049Zy  0rC2056c2071zR2072y349I2073y342I2074I2075y3412076y3422077y351C2078Zy  0r2085c2129y1802130zy205L2131y237D2132y255lO2133y257O2134O2143C2146y259Ac2147y2632148y2652149y2662150y2672154a2158y2662243y2652244y2642249y2632250y2622251y2572252y2442253y227Ld2254Zy195l2255y  02258y 902262y 852263zU2264y 86M2265y 87PM2266y 86PM2267y 84M2268y 832272y 88C2273y 902274y1012275y1052276y1062279y107L2280y1122281y1162282y1172287y1182288y1222289y1252290y1302291y1342292y1362293y1382295y1392297c2299y1442300Zy  0lu2363y2702366zD2384Zy180d2385y  0
```

## Frame data

A string buffer extracted from player data, enumerating that player's inputs by frame number.

```
1Z101zy327R102y333103y338I104y341I105y344106y345108y346109y349110y354111y358112y359115y  0119y  6120Zy 90r121y  0128zRI129I130y360I131y354I132y346133y344142y345143y346148C150y345151y344152y350153y  2154Zy  0rc181y180182y166183zy162L184y160186y156187y153U188y155189y156u190y157191y159C192y163193y176194y182195Zy192l196y  0c213A221a242y 78243y 75244zy 83UM245PM246y 79PM247y 78M248y 77249y 76251A257a281y 69282Zy 73u283y  0298y237299y252300zy258DO301O302y252LO303y250A310y252311y253a312y255l313y256317y257318y258319y259321y260323y261324y263325y264326y266327y267328y269329y270331y267332Zy201d333y180334y  0352zR353y346I354y345I355y344I356y342357y339359C360y341361y342362y343363y344364c365y345366y347367y358368Zy 28r369y 90370y  0412y 57413zy 69RUPM414y 67PM415y 65PM416PAM426y 63427y 59428y 54429y 46430y 37431y 23u432y  8433y360434y350435y344436y340437y339444y343445y351446y  0a447y 17448y 68rU449y 90450Zu451y  0479zy341R480y334DI481y340dI482y343I483y344484B490b492y342493y354494Zy  0r525y 69526zy 66U527y 69RPBM528y 66PM529y 64PM530M533b538y 65539y 68542y 69550y 70B551y 71553y 72555y 74r556y 87b557y 91558y107L559y121560y129561y135E562y140563y144564y145565y147567y148568y149569y151570y156u571y161572y170573y180574Zl575y  0604y219605y247606zy261DO607y262O608y259OB609y258O614y260615y263b616y264620B626b633B635y266637y267b643y268644y269649y270655C663c670C677c692C699c709C711y273712y275713Zy285d714y 76c715zy 73UM716y 76PM717y 69RPM718y 68PM723C730y 63c731y 59732y 54733y 52734y 49735y 48740y 49741y 50742y 52743y 53748C755c760y 52765y 38766y 10u767y353768Zy  0r780y270781zD782O783O784y263O785y258786y256788y255791y257792y260793y263796y262802y261813y262814y263815y262816Zy224d817zy180L818Zl819y  0826zy 67U827y 71RPCM828y 69PM829PM830M833y 63834y 32u835y  2c836Zy360r837y  0886y265887zy267DO888O889y263O916y265917y268918y270921y266922Zy247d923y192924y  0929zy 82U930y 79PM931y 73PCM932y 74PM933y 73M935y 74936y 73938y 72Rc940Zy  0ru1018y2701019zy278D1020y285O1021y284O1022y276O1023y2721024y2711026y2731027y2801028y289R1029y2971030y3071031y317I1032y3251033y3341034y340d1035y3421038y3431067y3421068y3391069y336D1070y3331071y3321075y3331076y3341077y337d1078y3411079y3461080y3511081y  01082y 101083y 26U1084y 39M1085y 45PM1086y 49PM1087y 50M1088y 531089y 541090y 571091y 631092y 711093y 721094y 701095y 63J1103y 60j1104y 551105y 531106y 491107y 431108y 391109y 381112y 391114y 401118y 381119y 311120y 22u1121y 111122y  31123y  01124y3571125y3541126y3511127y3501129y3491132y  01133y159Lr1134y156E1135y162E1136E1138C1142y1611143y1581144y1571145y155Uc1146y1521147y1481148y1441149y1411150y1401151y1451152y1491153y156u1154y1621155y174C1156Zy180l1158y  01161c1172C1175c1192y3601193zy340R1194y335DI1195y342dI1196y346I1199A1203a1205y3451206y3431207y3441208y  01209Zy 81r1210y  01234zy180L1235y162E1236y159E1237E1243y1601244y162C1245y1651246y1661247Zy  0l1251c1262C1266zy150L1267y1521268y1511269c1270y1501271y1511273y1551274y1601275Zy  0l1292y1491293zy143LU1294y146EM1295y151E1296y154E1297y156u1298y1571299y1601300y1631301y1661302y1711303y1801305y1791306y1681307y1621315y1691316Zy180l1317y  01319zy359R1320y342I1321y344I1322y341I1323y3361324y334D1325y333C1328y3341329y3351331y3361333d1335y353c1336Zy  0r1350C1354c1381y1751382zy156L1383y151UE1384y152E1385E1386y1541388y1561389y157uB1392y158A1393y1641394y1691395y1731396y180a1397Zlb1398y  01421zy351R1422y344I1423y342I1424y344I1428y3431430y3421440y3411442y3401443y3391444y3381446y3371450y3361452D1453y3341454y3321455y3341456Zy353rd1457zy158L1458y153UE1459y154E1460y153E1461y147M1462y1411463y129BM1464y115M1465y 98lM1466y 901467y 881468y 871475b1482y 881483y 901485Zu1486y  01495y2701496zD1497y284O1498O1499y279O1500y2761501A1503y2751504y2731505y2721509a1511y2731512y2751513y2781514y2831515y2851516y290R1517y2961518y2991519y3061520y3131521y3211522y3251523y3271525y3291526y343d1527y 221528Zy 59r1529y 521530zy 35R1531y 211532I1533y 221534y 26U1535y 36M1536y 39M1537y 40M1538y 41M1539y 441540y 48A1541y 531542y 571543y 611544y 631548a1562y 651563y 731564y 90r1565y114L1566y135E1567y146E1568y150E1569y1541570y157u1571y1591572y1601574y1611575y1601576y1611577y1621578y1631587C1592y1681593y1801594Zy  0lc1624zy179L1625y159E1626y160E1627y161E1645y1681646y1761647Zy  0l1651zy169L1652y154UE1653y161uE1654y162E1659y1601660y1591663y1621664y1631665Zy180l1666y  01669zy360R1670y345I1671y350I1672y349I1674y3481677y3491678JC1679y3471680y  01681Zrj1685c1701y1801702zy158L1703y153UE1704y154E1705y156E1706y157u1727y1561730U1731y1551733y1541734y1521735y1501736y148u1737Zy125l1738y  01739y 291740zy 11R1741y  51742y  01743y3541744y3421745y3311746Zy  0r1754zy162L1755y1591756y156E1757y157E1758y1581768y1571769y1561771Zy  0l1773zy  2R1774y360I1775y353I1776I1777y3511778y3491780y3591781Zy  0r1790C1848y1801849zL1850y1751853y174c1854y1781855Zy180l1856y  01880y1801881zy170L1882y1691884y1701885y1691915y1681916y1651917y1631918y1621924y1661927y1651928y1631938y1661939y1671943y1661949y1651950Zy170l1951y  01953y  61954C1955y  01962c1998y1801999zy165L2000y162E2001EC2002E2003y1652004y1752005Zy  0l2008c2041zR2042y357I2043y354I2044I2046y3512049Zy  0rC2056c2071zR2072y349I2073y342I2074I2075y3412076y3422077y351C2078Zy  0r2085c2129y1802130zy205L2131y237D2132y255lO2133y257O2134O2143C2146y259Ac2147y2632148y2652149y2662150y2672154a2158y2662243y2652244y2642249y2632250y2622251y2572252y2442253y227Ld2254Zy195l2255y  02258y 902262y 852263zU2264y 86M2265y 87PM2266y 86PM2267y 84M2268y 832272y 88C2273y 902274y1012275y1052276y1062279y107L2280y1122281y1162282y1172287y1182288y1222289y1252290y1302291y1342292y1362293y1382295y1392297c2299y1442300Zy  0lu2363y2702366zD2384Zy180d2385y  0
```

## Action table

A dictionary representation of frame data, in which the keys are frame numbers and the values are the player's inputs.

```
player1_lookup[1293] == [Action.ANGLES_DISABLED, 143, Action.LEFT_PRESS, Action.UP_PRESS]
```

Player inputs are represented either as Actions or, in the case of angles, integer values between 0 and 359.

## State table

A more complicated variation of the action table, in which the keys are frame numbers and the values are lists of Boolean flags representing the current state for each type of input.

```
player1_state_lookup[101] == [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, True]
```

The Boolean flag indices correspond with ActionTypes.

## Action and ActionType

Actions, which are used by action tables, represent possible player inputs, such as JUMP_PRESS, JUMP_RELEASE, LEFT_PRESS, LEFT_TAP, LEFT_RELEASE, STRONG_PRESS, STRONG_RELEASE, etcetera. ActionTypes, which are used by state tables, condense Actions into classes like JUMP, LEFT, STRONG, etcetera. Actions are Enums and ActionTypes are IntEnums.

Angles are treated differently by lookup tables and state tables. The former leaves them as normal integers (e.g. 180, 233, 47, etc), while the latter rounds them to the nearest 45 degree increment and then converts them into ANGLE_UP, ANGLE_DOWN, ANGLE_LEFT, ANGLE_RIGHT, or any pair of those that represents a diagonal.

## (Optional) Replay, Player, and LookupTable

Replay and Player objects can be used instead of the aforementioned ReplayData and PlayerData static classes in order to accomodate an object-oriented coding style (see below for an example). They use LRU caching to provide lazy evaluation for some of their more demanding attributes (e.g. for state tables). Otherwise, implementation details are unchanged. 

Lookup tables are generic wrappers for both action and state tables. The _get_ method of a lookup table provides automatic snapping. Thus, whereas the PlayerData static class returns a collection which can be used to generate a state or action table, a Player object simply returns an lookup table of the requested type.

# Example

## Functional Style

```
from replay import FrameData, PlayerData, ReplayData

with open('test.roa') as f:
    replay_data = f.read()
    game_version = ReplayData.get_version(replay_data)
    match_duration = ReplayData.get_duration(ReplayData.get_all_frame_data(replay_data))
    player_data = ReplayData.get_player_data(replay_data)
    state_table = FrameData.get_state_table(PlayerData.get_frame_data(player_data[0]))
    x = state_table[FrameData.snap_frame(100)]
```

## Object-Oriented Style

```
from replay import Replay, Player, ActionTable

with open('test.roa') as f:
    replay = Replay(f.read())
    game_version = replay.version
    match_duration = replay.duration
    players = replay.players
    states = players[0].states
    x = states.get(100)
```

# Credits

[lazerzes](https://github.com/ContentsMayBeHot/RivalsofAetherReplayParser)

[MatthewMJV](https://www.reddit.com/r/RivalsOfAether/comments/5sxvw2/what_i_have_learned_from_looking_through_replays/)

[SerpentAI](https://github.com/SerpentAI/SerpentAI)
