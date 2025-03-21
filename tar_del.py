
import tar_del


# 创建一个 TrackedTarget 实例

N = 8
targets_score = [10, -1, 0, 100, 0, -1, 100, 0]


print("Targets Info:")
for i in range(N):
    target = tar_del.TrackedTarget(i,targets_score[i])
    print(f"UUID: {target.uuid}, Life Cycle: {target.life_cycle}")

print("\nDelete Invalid Targets:")
for i in range(N):
    target = tar_del.TrackedTarget(i,targets_score[i])
    # 调用 delete_invalid_targets 函数
    tar_del.delete_invalid_targets(target)
    if target.life_cycle <= 0:
        print(f"Delete target UUID:{target.uuid}, Life Cycle: {target.life_cycle}")

print("\nAfter Delete:")
for i in range(N):
    target = tar_del.TrackedTarget(i,targets_score[i])
    # 调用 delete_invalid_targets 函数
    tar_del.delete_invalid_targets(target)
    if target.life_cycle > 0:
        print(f" UUID:{target.uuid}, Life Cycle: {target.life_cycle}")



# 定义 N 的值
N = 5

# 假设的分数列表，可根据实际情况修改
targets_score = [10, -1, 0, 100, 0]

# 创建一个包含 N 个 TrackedTarget 实例的列表
targets = []
for i in range(N):
    # 创建 TrackedTarget 实例并添加到列表中
    target = tar_del.TrackedTarget(i, targets_score[i])
    targets.append(target)

print("Targets Info:")
for target in targets:
    print(f"UUID: {target.uuid}, Life Cycle: {target.life_cycle}")

print("\nDelete Invalid Targets:")
for target in targets:
    # 调用 delete_invalid_targets 函数
    tar_del.delete_invalid_targets(target)
    if target.life_cycle <= 0:
        print(f"Delete target UUID:{target.uuid}, Life Cycle: {target.life_cycle}")