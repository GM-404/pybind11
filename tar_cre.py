import tar_cre 


# 定义 N 的值
N = 6

# 假设的分数列表，可根据实际情况修改
targets_speed = [10, 0.1, 0.02, -1, 3,0]

targets = []
for i in range(N):
    # 创建 Measurement 实例并添加到列表中
    target = tar_cre.Measurement(targets_speed[i])
    targets.append(target)
print(" Measurements Info:")
for target in targets:
    print(f"speed: {target.speed}")

uuid = 0
print("\nDelete Invalid Measurements:")
for target in targets:
    # 调用 delete_invalid_measurements 函数
    tar_cre.creat_targets(target)
    if target.speed <= 0:
        print(f"Delete target speed:{target.speed}")
    else:
        uuid = uuid + 1

print(f"\nnew add uuid:{uuid}")
