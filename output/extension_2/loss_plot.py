from matplotlib import pyplot as plt

# INFO:train:Train loss: 1.05

def extract_training_losses(file_name):
  with open(file_name, "r") as f:
    return [float(line.split(' ')[2].rstrip('\n')) for line in f.readlines() if "INFO:train:Train loss: " in line]

our_y = extract_training_losses('output_ours.log')
their_y = extract_training_losses('output_theirs.log')
xs = [x for x in range(50)]

print(len(our_y), len(xs))
plt.plot(xs, our_y, label='Modified Data Aug', color='fuchsia')
plt.plot(xs, their_y, label='Original Data Aug', color='k')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
# plt.title('Training Loss Comparison')
plt.show()