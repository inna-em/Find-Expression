import itertools

def conv_func(nums, ops):
    res_nums, res_ops = [nums[0]], []
    for i, op in enumerate(ops):
        if op:
            res_nums.append(nums[i + 1])
            res_ops.append(op)
        else:
            res_nums[-1] = res_nums[-1] * 10 + nums[i + 1]
    return res_nums, res_ops

def find_expression():
    nums = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    results = []
    for ops in itertools.product(["+", "-", ""], repeat=9):
        conv_nums, conv_ops = conv_func(nums, ops)
        result = conv_nums[0]
        for num, op in zip(conv_nums[1:], conv_ops):
            if op == "+":
                result += num
            else:
                result -= num
        if result == 200:
            result_str = str(conv_nums[0])
            for num, op in zip(conv_nums[1:], conv_ops):
                result_str += str(op) + str(num)
            results.append(result_str)
    return results

print(find_expression())