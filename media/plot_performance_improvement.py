import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

labels = ['before refactoring', 'after refactoring']
runtimes = {
    'other': np.array([61.9668 - 58.1838, 2.97468 - 0.278544]),
    'comms': np.array([58.1838, 0.278544])
}

fig, ax = plt.subplots()
left = np.zeros(len(labels))

for key, runtime in runtimes.items():
    ax.barh(labels, runtime, label=key, left=left)
    left += runtime

ax.set_xlabel('Runtime (s)')
ax.invert_yaxis()
ax.set_title("\n".join(wrap("Runtime of a single PROMPI step before and after refactoring MPI communication of a $512^3$ simulation on 2 Tursa nodes (8 Nvidia A100 GPUs)", 40)))
ax.legend(loc='lower right', reverse=True)

fig.set_figwidth(5)
fig.set_figheight(3)

plt.tight_layout()
# plt.show()
plt.savefig('performance_improvement.svg', bbox_inches='tight', dpi=300)
