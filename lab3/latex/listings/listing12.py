xi, yi = np.meshgrid(np.arange(cols), np.arange(rows))
xmid = cols / 2.0
ymid = rows / 2.0
xi = xi - xmid
yi = yi - ymid
r, theta = cv.cartToPolar(xi / xmid, yi / ymid)
F3 = -0.1
r = r + F3 * r ** 3
u, v = cv.polarToCart(r, theta)
u = u * xmid + xmid
v = v * ymid + ymid
I_pincushion = cv.remap(I, u.astype(np.float32), v.astype(np.float32), cv.INTER_LINEAR)
plt.imshow(cv.cvtColor(I_pincushion, cv.COLOR_BGR2RGB))
plt.axis('off')