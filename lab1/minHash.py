from Import import *

def minhash(hash_num, c, data_handler, set_loaded, data_loaded):
    # print("all data loaded ...")
    hash_handler = Hash(hash_num, set_loaded, data_loaded)
    answer_list = []

    for x in data_handler.set_group:
        if x.head.next is None:
            continue
        else:
            x.matrix = get_matrix(data_handler, x.index, data_loaded)

    for h in hash_handler.hash_group:
        for i in range(1, data_handler.set_group[0].head.value + 1):
            h.matrix[i - 1].value = h.get_label(data_handler.set_group[i].matrix)

    for i in range(1, len(data_handler.set_group)):
        answer = SimList(hash_handler).find_sim(data_handler.set_group[i].index, c)
        if len(answer) != 0:
            for q in answer:
                answer_list.append(q)

    # print(answer_list)
    np.save("./output/minHash.npy", np.array(answer_list))
    return answer_list


if __name__ == "__main__":
    data_handler, set_loaded, data_loaded = load_data()
    minhash(100, 0.2, data_handler, set_loaded, data_loaded)
