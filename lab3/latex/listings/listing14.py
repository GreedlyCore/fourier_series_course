topPart = cv.imread('/content/drive/MyDrive/top.jpg', cv.IMREAD_COLOR)
botPart = cv.imread('/content/drive/MyDrive/bot.jpg', cv.IMREAD_COLOR)

templ_size = 10
templ = topPart[-templ_size:, :botPart.shape[1], :]
res = cv.matchTemplate(botPart, templ, cv.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
result_img = np.zeros((topPart.shape[0] + botPart.shape[0] - max_loc[1] - templ_size , topPart.shape[1],topPart.shape[2]), dtype = np.uint8)
result_img[0:topPart.shape[0], :, :] = topPart
result_img[topPart.shape[0]:, :botPart.shape[1], :] = botPart[max_loc[1] + templ_size:, :, :]

fig, axs = plt.subplots(1, 3)
plt.sca(axs[0])
plt.imshow(cv.cvtColor(botPart, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.sca(axs[1])
plt.imshow(cv.cvtColor(topPart, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.sca(axs[2])
plt.imshow(cv.cvtColor(result_img, cv.COLOR_BGR2RGB))
plt.axis('off')