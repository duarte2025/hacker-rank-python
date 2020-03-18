def merge_the_tools(string, k):
    for i in range(int(len(string) / k)):
        u = ''
        for t in string[i * k : (i + 1) * k]:
            if t in u:
                continue
            u += c
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
