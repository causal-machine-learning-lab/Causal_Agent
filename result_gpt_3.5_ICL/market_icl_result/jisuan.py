import json

json_list = []
# prefix = 'marketing_elements_'
prefix = ''
for name_list in ["IT","CIT","MULTCIT","Has-Collider","Has-Confounder","CAUSE","CAUSALKG","PARTIAL_CG"]:
    name = prefix+f'{name_list}.jsonl'
    with open(name,'r') as f:
        for line in f:
            json_list.append(json.loads(line))

    node_num = {

    }
    node_num['name'] = name
    zong_c = 0
    zong_s = 0
    # for line in json_list:
    #     if line['node num'] not in node_num.keys():
    #         node_num[line['node num']] = [0,0]
    #     if line['label'] == 1:
    #         node_num[line['node num']][0] += 1
    #         zong_c += 1
    #     node_num[line['node num']][1] += 1
    #     zong_s += 1

    for line in json_list:
        if line['node_num'] not in node_num.keys():
            node_num[line['node_num']] = [0,0]
        if line['label'] == 1:
            node_num[line['node_num']][0] += 1
            zong_c += 1
        node_num[line['node_num']][1] += 1
        zong_s += 1

    for key in node_num.keys():
        if key != 'name':
            node_num[key].append(node_num[key][0]/node_num[key][1])

    node_num[-1] = [zong_s,zong_c,zong_c/zong_s]
    with open("market_icl_result/tongji.json", "a+") as f:
        json.dump(node_num,f)
        f.write('\n')