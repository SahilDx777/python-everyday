# text: str = "TanKKK"

# text_asd = list(text)

# print(text)
# print(text_asd)


result = []


def check_two():
    for i in range(1, 16):
        if i % 2 == 0:
            result.append("Hi")
            # print(result)
        else:
            result.append(i)
            # print(result)
    return result


print(check_two())

# for i in range(1, 16):
#     result = []
#     if i % 2 == 0:
#         result.append("Hi")
#     else:
#         result.append(i)
#     print(result)
