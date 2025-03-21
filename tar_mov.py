import tar_mov



N = 8
targets_score = [3000,3001,2999,5000,500,100,3098,0,1500]
targets = []
for i in range(N):
    target = tar_mov.TrackedTarget(i,targets_score[i])
    targets.append(target)
print("Targets Info:")
for target in targets:
    print(f"UUID: {target.uuid}, target_score: {target.target_score}")

print("\nMove Targets:")

a = 0
for target in targets:
    a  = tar_mov.move_confirmed_targets(target)
    if a == 1:
        print(f"Move target UUID:{target.uuid}, target_score: {target.target_score}")

