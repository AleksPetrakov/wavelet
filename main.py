# import numpy as np
# import matplotlib.pyplot as plt
#
# import pywt.data
#
# from PIL import Image
#
# img = Image.open('candle.png')
# original = np.asarray(img)
#
# # Wavelet transform of image, and plot approximation and details
# titles = ['Approximation', ' Horizontal detail',
#           'Vertical detail', 'Diagonal detail']
# coeffs2 = pywt.dwt2(original, 'bior1.3')
# LL, (LH, HL, HH) = coeffs2
# fig = plt.figure(figsize=(12, 3))
# # for i, a in enumerate([LL, LH, HL, HH]):
# for i, a in enumerate([LL, LH, HL, HH]):
#     ax = fig.add_subplot(1, 4, i + 1)
#     ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
#     ax.set_title(titles[i], fontsize=10)
#     ax.set_xticks([])
#     ax.set_yticks([])
#
# fig.tight_layout()
# plt.show()

import pandas as pd
import pywt
import matplotlib.pyplot as plt

# Загрузка данных о ценах на акции ЛУКОЙЛ из файла
data = pd.read_csv('LKOH.ME.csv')

# Отображение исходных данных
plt.plot(data['Date'], data['Close'], label='Original')

# wavelist = pywt.wavelist(kind='discrete')
wavelist = ['bior1.3', 'coif3', 'db5', 'rbio3.5', 'sym8']
for wavelet in wavelist:
    coeff = pywt.wavedec(data['Close'], wavelet, mode="per", level=1)
    plt.plot(data['Date'], pywt.upcoef('d', coeff[1], wavelet, level=1, take=len(data)), label=wavelet)

# wavelet = 'sym4'

# coeff = pywt.wavedec(data['Close'], wavelet, mode="per", level=1)

# for i in range(1, level + 1):
#     plt.plot(data['Date'], pywt.upcoef('d', coeff[i], wavelet, level=i, take=len(data)), label='Level %d' % i)
# print(wavelet)
# plt.plot(data['Date'], pywt.upcoef('d', coeff[1], wavelet, level=1, take=len(data)), label='Вейвлет %s' % wavelet)

# Настройка отображения графика
plt.xlabel('Дни')
plt.ylabel('Цена')
plt.title('Вейвлет-анализ акций ЛУКОЙЛ')
plt.legend()
plt.show()
