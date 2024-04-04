T = np.array([[0, 0], [1, 0], [0, 1], [0.00001, 0], [0.002, 0], [0.001, 0]])
I_polynomial = np.zeros(I.shape , I.dtype)
x, y = np.meshgrid(np.arange(cols), np.arange(rows))
xnew = np.round(T[0, 0] + x * T[1, 0] + y * T[2, 0] + x * x * T[3, 0] + x * y * T[4, 0] + y * y * T[5, 0]).astype(np.float32)
ynew = np.round(T[0, 1] + x * T[1, 1] + y * T[2,1] + x * x * T[3,1]+ x * y * T[4,1]+ y * y * T[5, 1]).astype(np.float32)
mask = np.logical_and( np.logical_and(xnew >= 0, xnew < cols), np.logical_and(ynew >= 0, ynew < rows))
if I.ndim == 2:
  I_polynomial[ynew[mask].astype(int), xnew[mask].astype(int)] = I[y[mask], x[mask]]
else:
  I_polynomial[ynew[mask].astype(int), xnew[mask].astype(int), :] = I[y[mask], x[mask], :]
plt.imshow(cv.cvtColor(I_polynomial, cv.COLOR_BGR2RGB))
plt.axis('off')