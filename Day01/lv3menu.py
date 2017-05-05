#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: PanFei Liu

menu_dict = {
    '家用电器': {
        '电视': {
            '合资品牌': {
                '夏普': 'LCD-70SU665A 70寸',
                '索尼': 'KD-55X7000SD 50寸',
                '三星': 'UA55KUF30ZJXXZ 55寸'
            },
            '国产品牌': {
                '海信': 'LED55EC520UA 55寸',
                'TCL': 'D50A810 50寸',
                '康佳': 'S55U 55寸'
            },
            '互联网品牌': {
                '小米': 'L43M5-AZ 32寸',
                '乐视': '超4 X50 50寸'
            }
        },
        '空调': {
            '壁挂式': {
                '美的': '美的正1.5匹 变频',
                '格力': '格力正1.5匹 变频'
            },
            '柜式': {
                '美的': '美的正3匹 变频',
                '格力': '格力正3匹 变频'
            }
        }
    },
    '电脑': {
        '笔记本': {
            '联想': {
                '联想G480': '￥4880',
                '联想Y480': '￥5480'
            },
            '华硕': {
                '华硕顽石四代': '￥4699'
            }
        },
        '台式': {
            '品牌': {
                '联想': '￥4180'
            },
            '组装机': {
                '组装': '￥3880'
            }
        }
    }
}

main_menu = menu_dict.keys()
menu = menu_dict
str = []
while True:
    for m in main_menu: #菜单列表
        print(m)
    if menu.keys():
        name = input("Please select（up level: B/b）:")
        if name not in "Bb" and name in main_menu: #判断输入是否为 菜单
            str.append(name)
            print(str)
            val = menu[name]
        elif name in "Bb": #返回上一层判断
            if len(str):
                up_level = str.pop()
                print(str)
                if len(str) == 1:
                    menu = menu_dict[str[0]]
                    main_menu = menu_dict[str[0]].keys()
                    continue
                elif len(str) > 1:
                    for i in range(len(str)-1):
                        menu = menu_dict[str[i]]
                    main_menu = menu[str[len(str)-1]].keys()
                    continue
                else:
                    main_menu = menu_dict.keys()
                    menu = menu_dict
                    continue
            else:
                main_menu = menu_dict.keys()
                menu = menu_dict
                continue
        elif name in "Qq": #退出程序
            print("-----END-----")
            break
        else:
            print("The menu  what you choice does not exist")
            continue
    else:
        print("error")

    if isinstance(val, dict): # 进入下一层菜单
        if name in menu.keys():
            main_menu = menu[name].keys()
            menu = menu[name]

        else:
            name = input("The menu $s what you choice does not exist, Please select again:"% name)
    else:
        print(menu)
        result = input("Back at the next higher level or quit?(quit: Q/q)")
        if result in "Qq":
            break
        else: #退回到首层菜单
            main_menu = menu_dict.keys()
            menu = menu_dict

