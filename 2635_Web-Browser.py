while True:
    try:
        n = int(input())
        word_list = []
        for i in range(n):
            word = input().lower()
            word_list.append(word)
        q = int(input())
        for i in range(q):
            search_word = input().lower()
            count = 0
            for j in range(len(word_list)):
                if word_list[j].startswith(search_word):
                    count += 1
            length = 0
            for j in range(len(word_list)):
                if word_list[j].startswith(search_word):
                    length = len(word_list[j])
                    break
            for j in range(len(word_list)):
                if word_list[j].startswith(search_word):
                    if len(word_list[j]) > length:
                        length = len(word_list[j])
            if count > 0:
                print(count, length)
            else:
                print(-1)
    except EOFError:
        break